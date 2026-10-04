#!/usr/bin/env python3
"""Registra uma leitura da apuração em dados/snapshots.csv.

Uso:
  python3 registrar.py URNAS_PCT LULA_PCT FLAVIO_PCT [--lula-votos N] [--flavio-votos N] [--hora HH:MM] [--nota "texto"]

Exemplo:
  python3 registrar.py 12 45.3 48.1 --nota "começo da apuração"
"""
import argparse
import csv
from datetime import datetime
from pathlib import Path

ARQUIVO = Path(__file__).parent / "dados" / "snapshots.csv"
COLUNAS = ["horario", "urnas_pct", "lula_pct", "flavio_pct", "lula_votos", "flavio_votos", "nota"]


def main():
    p = argparse.ArgumentParser(description="Registra uma leitura da apuração")
    p.add_argument("urnas_pct", type=float, help="%% de urnas apuradas")
    p.add_argument("lula_pct", type=float, help="%% de votos válidos do Lula")
    p.add_argument("flavio_pct", type=float, help="%% de votos válidos do Flávio")
    p.add_argument("--lula-votos", type=int, default=None)
    p.add_argument("--flavio-votos", type=int, default=None)
    p.add_argument("--hora", default=None, help="HH:MM (padrão: agora)")
    p.add_argument("--nota", default="")
    a = p.parse_args()

    hoje = datetime.now().strftime("%Y-%m-%d")
    horario = f"{hoje} {a.hora}" if a.hora else datetime.now().strftime("%Y-%m-%d %H:%M")

    novo = not ARQUIVO.exists()
    ARQUIVO.parent.mkdir(exist_ok=True)
    with ARQUIVO.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(COLUNAS)
        w.writerow([horario, a.urnas_pct, a.lula_pct, a.flavio_pct,
                    a.lula_votos or "", a.flavio_votos or "", a.nota])
    dif = a.flavio_pct - a.lula_pct
    lider = "Flávio" if dif > 0 else "Lula"
    print(f"✔ {horario} | {a.urnas_pct}% urnas | Lula {a.lula_pct}% x Flávio {a.flavio_pct}% | {lider} +{abs(dif):.2f} p.p.")


if __name__ == "__main__":
    main()
