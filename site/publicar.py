#!/usr/bin/env python3
"""Monta a versão pública do site em docs/ (servida pelo GitHub Pages).

Uso: python3 site/publicar.py

Copia o site, o painel e os gráficos para docs/, ajustando os caminhos para que tudo
funcione a partir da raiz publicada. Os prints dos sites (telas de terceiros, só locais)
ficam de fora. docs/preview.png (imagem de compartilhamento) é gerada à parte.
"""
import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SITE = RAIZ / "site"
DOCS = RAIZ / "docs"
URL = "https://arrualuiz.github.io/noite-do-primeiro-turno-2026/"
REPO = "https://github.com/arrualuiz/noite-do-primeiro-turno-2026"

TITULO = "A noite do primeiro turno · Eleições 2026"
DESCRICAO = ("A apuração do 1º turno de 2026 contada com dados: coleta automática do TSE, "
             "projeção por estado, o que cada atualização mudou e 20 análises feitas ao vivo.")


def main():
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")  # servir os arquivos como estão, sem Jekyll

    # site
    html = (SITE / "index.html").read_text(encoding="utf-8")
    html = re.sub(r"<!--.*?-->\n?", "", html, count=1, flags=re.S)           # comentário de desenvolvimento
    html = re.sub(r'\s*<figure class="print">.*?</figure>', "", html, flags=re.S)  # prints só locais
    html = html.replace('href="../painel/painel.html"', 'href="painel.html"')
    html = html.replace('href="../CONTEXTO.md"', f'href="{REPO}/blob/main/CONTEXTO.md"')
    meta = f'''<meta name="description" content="{DESCRICAO}">
<meta property="og:type" content="website">
<meta property="og:title" content="{TITULO}">
<meta property="og:description" content="{DESCRICAO}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23fcfcfb'/%3E%3Cpath d='M5 24 L13 15 L19 19 L27 8' fill='none' stroke='%232a78d6' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<title>'''
    html = html.replace("<title>", meta, 1)
    (DOCS / "index.html").write_text(html, encoding="utf-8")
    for nome in ("estilo.css", "dados.js"):
        shutil.copy(SITE / nome, DOCS / nome)
    casos = (SITE / "cases.js").read_text(encoding="utf-8").replace("](../cases/graficos/", "](graficos/")
    (DOCS / "cases.js").write_text(casos, encoding="utf-8")

    # gráficos dos cases
    if (DOCS / "graficos").exists():
        shutil.rmtree(DOCS / "graficos")
    shutil.copytree(RAIZ / "cases" / "graficos", DOCS / "graficos")

    # painel (versão estática: sem recarregar sozinho)
    painel = (RAIZ / "painel" / "painel.html").read_text(encoding="utf-8")
    painel = painel.replace('<meta http-equiv="refresh" content="60">\n', "")
    painel = painel.replace(" · atualiza sozinho a cada minuto", "")
    painel = painel.replace("<title>Painel da Apuração</title>",
                            f'<title>Painel da Apuração · 1º turno 2026</title>\n<meta property="og:image" content="{URL}preview.png">')
    (DOCS / "painel.html").write_text(painel, encoding="utf-8")

    n = len(list((DOCS / "graficos").glob("*.svg")))
    print(f"publicar: docs/ pronto (index.html, painel.html, {n} gráficos) → {URL}")


if __name__ == "__main__":
    main()
