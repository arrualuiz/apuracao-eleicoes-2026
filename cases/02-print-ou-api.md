---
numero: 02
titulo: "Print ou API? Achando a fonte oficial"
hora: "18:16"
tipo: bastidor
manchete: "O TSE publica tudo em JSON: eleição 6257, um arquivo por estado"
status: fechado
---

## A pergunta
Dá para automatizar: fazer scraping, tirar print, ler o print e preencher o registro sozinho, ao longo do tempo?

## O que os dados mostraram
- **UOL:** bloqueia acesso automático (HTTP 403).
- **g1:** carrega os dados via JavaScript depois da página.
- **TSE:** a fonte oficial é aberta. O arquivo `resultados.tse.jus.br/oficial/comum/config/ele-c.json` lista as eleições, e a de **Presidente 1º turno 2026 é a 6257**. Cada UF tem um arquivo de resultados:
  - `.../ele2026/6257/dados/<uf>/<uf>-c0001-e006257-u.json`: votos por candidato, seções apuradas, eleitorado, brancos, nulos e abstenção.
  - `.../dados/br/br-e006257-ab.json`: andamento por UF.

## Como calculei
Testei variações de URL seguindo os modelos de caminho que o próprio `ele-c.json` descreve (`<base>/<ambiente>/<ciclo>/<cd_eleicao>/dados/<uf>`) até achar os arquivos que respondiam 200.

## Conclusão
Ler print com OCR seria mais frágil e menos exato que a API. Os prints ficaram como **evidência visual** (placar e mapa do g1, via Puppeteer), e os números vêm do TSE. O coletor (`coletar.py`) roda a cada 3 min e guarda os JSON brutos de cada coleta.

## Desfecho
A coleta rodou a noite toda. Guardar os JSON brutos salvou o projeto duas vezes (cases 04 e 10).
