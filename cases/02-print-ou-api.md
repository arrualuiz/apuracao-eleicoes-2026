---
numero: 02
titulo: "Print ou API? Achando a fonte oficial"
hora: "18:16"
tipo: bastidor
manchete: "O TSE publica tudo em JSON aberto: eleição 6257, um arquivo por estado. Melhor que ler prints"
status: fechado
---

## Em resumo
- A primeira ideia era tirar prints dos sites e ler os números das imagens.
- Investigando as páginas, cheguei à **fonte oficial**: o TSE publica a apuração em arquivos JSON abertos, um por estado, atualizados ao longo da noite.
- Os números passaram a vir direto do TSE; os prints ficaram só como registro visual.

## A pergunta
Dá para automatizar: fazer scraping, tirar print, ler o print e preencher o registro sozinho, ao longo do tempo?

## Para entender
- **Scraping:** extrair dados do HTML de uma página.
- **API / JSON:** arquivos de dados estruturados que um programa lê diretamente, sem interpretar imagem nem layout.
- **OCR:** ler texto de uma imagem. Funciona, mas erra números e quebra quando o layout muda.

## O que os dados mostraram
| Fonte testada | Resultado |
|---|---|
| UOL (página) | Bloqueia acesso automatizado (HTTP 403). Não insisti |
| g1 (página) | Carrega os números via JavaScript depois que a página abre |
| UOL (arquivos de dados) | Curvas de evolução de 2026 e 2022 acessíveis em JSON |
| **TSE** | **Arquivos oficiais abertos**, um por estado |

Como cheguei aos arquivos do TSE:
1. `resultados.tse.jus.br/oficial/comum/config/ele-c.json` lista as eleições. A de **Presidente, 1º turno de 2026, é a 6257** (o 2º turno será a 6258).
2. O próprio arquivo de configuração descreve o modelo dos caminhos: `<base>/<ambiente>/<ciclo>/<cd_eleicao>/dados/<uf>`.
3. Testando variações, os arquivos que respondiam eram:

| Arquivo | O que tem |
|---|---|
| `.../ele2026/6257/dados/<uf>/<uf>-c0001-e006257-u.json` | Votos por candidato, seções apuradas, eleitorado, comparecimento, abstenção, brancos, nulos |
| `.../ele2026/6257/dados/br/br-e006257-ab.json` | Andamento da apuração por UF |

`<uf>` = `br` (nacional), `ac` … `to`, e `zz` (exterior): 29 arquivos.

## Como calculei
Testei as URLs com `curl` até achar as que respondiam 200 e inspecionei a estrutura dos JSON. Depois escrevi o coletor (`coleta/coletar.py`): a cada 3 minutos baixa os 29 arquivos, guarda tudo como veio em `dados/brutos/<horário>/` e monta as tabelas. Os prints do g1 são tirados com Puppeteer (`coleta/prints.js`).

## Conclusão
Ler print com OCR seria mais frágil e menos exato que a fonte original. A regra que ficou: **números vêm da fonte oficial; prints servem como evidência do que os sites mostravam**. Guardar o JSON bruto de cada coleta permitiu corrigir erros depois sem perder nada (cases 04 e 10).

## Desfecho
A coleta rodou a noite toda. Guardar os JSON brutos salvou o projeto duas vezes (cases 04 e 10).
