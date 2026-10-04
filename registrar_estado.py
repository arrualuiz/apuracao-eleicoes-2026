#!/usr/bin/env python3
"""Registra o andamento de um estado em dados/estados.csv.

Uso:
  python3 registrar_estado.py UF URNAS_PCT ELEITORADO [--flavio PCT] [--lula PCT] [--hora HH:MM] [--fonte TXT]

Exemplo:
  python3 registrar_estado.py MG 13.05 14323875 --flavio 49.12 --lula 41.48 --fonte g1
"""
import argparse
import csv
from datetime import datetime
from pathlib import Path

ARQUIVO = Path(__file__).parent / "dados" / "estados.csv"
COLUNAS = ["horario", "uf", "urnas_pct", "eleitorado", "flavio_pct", "lula_pct", "fonte"]


def main():
    p = argparse.ArgumentParser(description="Registra o andamento de um estado")
    p.add_argument("uf")
    p.add_argument("urnas_pct", type=float)
    p.add_argument("eleitorado", type=int, help="votos em disputa no estado")
    p.add_argument("--flavio", type=float, default=None)
    p.add_argument("--lula", type=float, default=None)
    p.add_argument("--hora", default=None)
    p.add_argument("--fonte", default="")
    a = p.parse_args()

    hoje = datetime.now().strftime("%Y-%m-%d")
    horario = f"{hoje} {a.hora}" if a.hora else datetime.now().strftime("%Y-%m-%d %H:%M")

    novo = not ARQUIVO.exists()
    ARQUIVO.parent.mkdir(exist_ok=True)
    with ARQUIVO.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(COLUNAS)
        w.writerow([horario, a.uf.upper(), a.urnas_pct, a.eleitorado,
                    "" if a.flavio is None else a.flavio,
                    "" if a.lula is None else a.lula, a.fonte])
    print(f"✔ {horario} | {a.uf.upper()} {a.urnas_pct}% apurado")


if __name__ == "__main__":
    main()
