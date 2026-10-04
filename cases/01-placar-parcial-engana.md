---
numero: 01
titulo: O placar parcial engana
hora: "18:13"
tipo: analise
manchete: "Com 12% apurado, o Sul já tinha ~40% contado e o Nordeste ~5%"
status: aberto
---

## A pergunta
Às 18:07, com 12% das urnas apuradas, o Flávio estava na frente. Dá para tirar alguma conclusão já, ou é cedo?

## O que os dados mostraram
Às 18:13 (UOL, 12,45% apurado): **Flávio 51,09% x Lula 40,71%**. A apuração estava bem desigual entre os estados:

| Estado | Apurado | Tendência histórica |
|---|---|---|
| Paraná | ~39% | Flávio |
| Rio Grande do Sul | ~24% | Flávio |
| São Paulo | ~4% | Flávio |
| Rio de Janeiro | ~3% | Flávio |
| Bahia | ~5% | Lula |
| Pernambuco / Ceará | ~6% | Lula |

Bahia, Pernambuco e Ceará sozinhos tinham **~23 milhões de eleitores** ainda fora da conta.

## Como calculei
No começo foi manual: prints do UOL e do g1, com o % por estado estimado pela largura das barras (marcado como `uol-barra-estimada` em `dados/estados.csv`). Ranking de "onde ainda faltam votos" = eleitorado × (1 − % apurado), em `analisar.py`.

## Conclusão
O placar com 12% mostrava sobretudo **quais regiões foram apuradas primeiro**, não o resultado. Em 2022 aconteceu o mesmo: o Bolsonaro liderou até ~67% das urnas e o Lula passou quando o Nordeste entrou.

## Desfecho
_a preencher no fim da apuração_
