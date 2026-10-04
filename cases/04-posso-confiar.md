---
numero: 04
titulo: "Posso confiar? O bug do % de urnas"
hora: "18:45"
tipo: bastidor
manchete: "Meu painel dizia 44% apurado; o certo era 36,6%"
status: fechado
---

## A pergunta
Posso confiar nesses números?

## O que os dados mostraram
Comparando com o print do g1 do mesmo momento:
- **Votos:** batiam exatamente (Flávio 21.383.323).
- **% de urnas apuradas:** o meu dizia **44,01%**; o g1, **36,60%**.

A causa: o TSE publica dois arquivos que **não andam juntos**. O `br-e006257-ab.json` (andamento) fica alguns minutos **à frente** do `-u.json` (votos). Eu tirava o % de urnas do primeiro e os votos do segundo.

| Coleta | % no `-u.json` (certo) | % no `-ab.json` (adiantado) |
|---|---|---|
| 18:18 | 19,54% | 21,96% |
| 18:35 | 31,90% | 36,60% |
| 18:41 | 36,60% | 44,01% |

## Como calculei
Script comparando os dois campos em cada pasta de `dados/brutos/`. Depois, reprocessamento de `snapshots.csv` e `estados.csv` a partir dos brutos.

## Conclusão
Erro corrigido em minutos e **sem perder nenhum dado**, porque os JSON originais estavam guardados. Lição: ler número e denominador **do mesmo arquivo** e guardar sempre o bruto.

## Desfecho
Corrigido às 18:46. Os CSV antigos ficaram em `*.bak` (fora do git).
