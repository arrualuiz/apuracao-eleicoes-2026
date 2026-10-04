#!/usr/bin/env python3
"""Coleta automática da apuração direto do TSE (resultados.tse.jus.br).

Cada coleta:
  - salva os JSON brutos em dados/brutos/<horário>/ (para auditoria)
  - adiciona o placar nacional em dados/snapshots.csv
  - adiciona o andamento de cada UF em dados/estados.csv
  - adiciona todos os candidatos em dados/candidatos.csv
  - baixa a curva de evolução do UOL (2026 e 2022) e regenera painel.html
  - opcionalmente tira prints recortados do UOL e do g1 (--print, via prints.js)

Uso:
  python3 coletar.py                 # uma coleta
  python3 coletar.py --a-cada 180    # repete a cada 180 s até Ctrl+C
  python3 coletar.py --a-cada 180 --print
"""
import argparse
import csv
import json
import subprocess
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

BASE = "https://resultados.tse.jus.br/oficial/ele2026/6257/dados"
ELEICAO = "006257"
UFS = ["br", "ac", "al", "am", "ap", "ba", "ce", "df", "es", "go", "ma", "mg", "ms", "mt",
       "pa", "pb", "pe", "pi", "pr", "rj", "rn", "ro", "rr", "rs", "sc", "se", "sp", "to", "zz"]
UOL_EV_2026 = "https://stc.eleicoes2026.uol.com/2026/1turno/br/br-c1-ev.json"
UOL_EV_2022 = "https://stc.eleicoes2026.uol.com/2026/historical/2022/br-c1-t1-ev.json"

PASTA = Path(__file__).parent / "dados"
SNAPSHOTS = PASTA / "snapshots.csv"
ESTADOS = PASTA / "estados.csv"
CANDIDATOS = PASTA / "candidatos.csv"
ULTIMA = PASTA / ".ultima_coleta_tse"


def f(s):
    return float(s.replace(",", "."))


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def anexar(arquivo, colunas, linhas):
    novo = not arquivo.exists()
    with arquivo.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if novo:
            w.writerow(colunas)
        w.writerows(linhas)


def candidatos(dados_u):
    out = []
    for agr in dados_u["carg"][0]["agr"]:
        for par in agr["par"]:
            for c in par["cand"]:
                out.append({"nome": c["nmu"], "numero": c["n"], "votos": int(c["vap"]), "pct": f(c["pvapn"])})
    return sorted(out, key=lambda c: -c["votos"])


def tirar_prints(pasta):
    """Prints recortados (placar/evolução/estados/regiões do UOL e mapa do g1) via prints.js."""
    try:
        r = subprocess.run(["node", str(Path(__file__).parent / "prints.js"), str(pasta)],
                           timeout=150, capture_output=True, text=True)
        return len(list(pasta.glob("*.png")))
    except Exception:
        return 0


def baixar_uol():
    """Curvas de evolução do UOL: 2026 (desde o início da apuração) e histórico 2022."""
    for nome, url in [("uol-evolucao-2026.json", UOL_EV_2026), ("uol-historico-2022.json", UOL_EV_2022)]:
        if nome.endswith("2022.json") and (PASTA / nome).exists():
            continue  # histórico não muda
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://noticias.uol.com.br/"})
            with urllib.request.urlopen(req, timeout=20) as r:
                (PASTA / nome).write_bytes(r.read())
        except Exception as e:
            print(f"  ! UOL {nome}: {e}")


def gerar_painel():
    try:
        subprocess.run([sys.executable, str(Path(__file__).parent / "painel.py")], timeout=60, capture_output=True)
    except Exception as e:
        print(f"  ! painel: {e}")


def coletar(com_print=False):
    agora = datetime.now()
    horario = agora.strftime("%Y-%m-%d %H:%M")

    ab = baixar(f"{BASE}/br/br-e{ELEICAO}-ab.json")
    u_br = baixar(f"{BASE}/br/br-c0001-e{ELEICAO}-u.json")
    versao_tse = f"{u_br['dg']} {u_br['hg']}"
    if ULTIMA.exists() and ULTIMA.read_text().strip() == versao_tse:
        print(f"{horario} | TSE sem atualização desde {versao_tse}, nada gravado")
        return

    pasta_bruta = PASTA / "brutos" / agora.strftime("%Y%m%d-%H%M%S")
    pasta_bruta.mkdir(parents=True, exist_ok=True)
    (pasta_bruta / "br-ab.json").write_text(json.dumps(ab, ensure_ascii=False), encoding="utf-8")

    linhas_estados, linhas_cand = [], []
    nacional = None

    for uf in UFS:
        try:
            u = u_br if uf == "br" else baixar(f"{BASE}/{uf}/{uf}-c0001-e{ELEICAO}-u.json")
        except Exception as e:
            print(f"  ! falha em {uf}: {e}")
            continue
        (pasta_bruta / f"{uf}-u.json").write_text(json.dumps(u, ensure_ascii=False), encoding="utf-8")
        cands = candidatos(u)
        por_num = {c["numero"]: c for c in cands}
        flavio, lula = por_num.get("22"), por_num.get("13")
        # % de seções do PRÓPRIO arquivo de votos: o -ab.json fica minutos à frente dos votos
        urnas = f(u["s"]["pstn"])
        eleitorado = int(u["e"]["te"])

        for c in cands:
            linhas_cand.append([horario, uf.upper(), c["numero"], c["nome"], c["votos"], c["pct"]])

        if uf == "br":
            nacional = (urnas, lula, flavio)
        else:
            linhas_estados.append([horario, uf.upper(), urnas, eleitorado,
                                   flavio["pct"] if flavio else "", lula["pct"] if lula else "", "tse"])

    urnas, lula, flavio = nacional
    anexar(SNAPSHOTS, ["horario", "urnas_pct", "lula_pct", "flavio_pct", "lula_votos", "flavio_votos", "nota"],
           [[horario, round(urnas, 2), round(lula["pct"], 2), round(flavio["pct"], 2),
             lula["votos"], flavio["votos"], f"TSE {versao_tse}"]])
    anexar(ESTADOS, ["horario", "uf", "urnas_pct", "eleitorado", "flavio_pct", "lula_pct", "fonte"], linhas_estados)
    anexar(CANDIDATOS, ["horario", "abrangencia", "numero", "candidato", "votos", "pct"], linhas_cand)
    ULTIMA.write_text(versao_tse)

    msg = f"✔ {horario} | {urnas:.2f}% urnas | Flávio {flavio['pct']:.2f}% x Lula {lula['pct']:.2f}% | TSE {versao_tse}"
    baixar_uol()
    gerar_painel()
    msg += " | painel ok"
    if com_print:
        n = tirar_prints(pasta_bruta)
        msg += f" | {n} prints"
    print(msg, flush=True)


def main():
    p = argparse.ArgumentParser(description="Coleta a apuração direto do TSE")
    p.add_argument("--a-cada", type=int, default=0, help="segundos entre coletas (0 = só uma)")
    p.add_argument("--print", action="store_true", help="salva print da página do g1 em cada coleta")
    a = p.parse_args()
    while True:
        try:
            coletar(a.print)
        except Exception as e:
            print(f"{datetime.now():%H:%M} | erro na coleta: {e}", flush=True)
        if not a.a_cada:
            break
        time.sleep(a.a_cada)


if __name__ == "__main__":
    main()
