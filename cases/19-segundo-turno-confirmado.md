---
numero: 19
titulo: "20h57: o TSE confirma o 2º turno"
hora: "20:57"
tipo: bastidor
manchete: "Às 20h57, com 97% apurado, o TSE marcou a eleição como matematicamente definida: Flávio x Lula no 2º turno"
status: fechado
---

## A pergunta
O g1 colocou o selo "2º Turno" ao lado do Flávio e do Lula. Quando isso ficou oficial?

## O que os dados mostraram
O arquivo nacional do TSE tem um campo `md` ("matematicamente definido"). Ele ficou em `"n"` a noite toda e virou **`"s"` no arquivo gerado às 20:57:34**, com **97,24%** das seções apuradas no nacional. A coleta das 20:58 registrou o momento.

| Coleta | Arquivo nacional | % seções | `md` |
|---|---|---|---|
| 20:51 | 20:50:25 | 94,51% | n |
| 20:54 | 20:53:34 | 95,78% | n |
| **20:58** | **20:57:34** | **97,24%** | **s** |

Placar às 20:58 (soma das UFs, 96,83%): **Flávio 47,47% x Lula 44,64%**, diferença de 3,26 milhões de votos. O último lote (1,8 milhão de válidos) veio **Lula 53,6% x Flávio 39,9%**.

Em Minas (print do g1, 94%): Flávio 48,63% x Lula 42,83%, também com o selo de 2º turno.

## Como calculei
Leitura dos campos `md`, `st` e `e` de cada candidato nos `br-u.json` guardados em `dados/brutos/`. Os campos de situação dos candidatos (`st`) seguiam vazios às 20:58.

## Conclusão
A noite que começou com "o Flávio está ganhando com 12%" terminou, do ponto de vista da decisão, às 20h57: **haverá 2º turno**. A projeção por estado indicava isso desde 18:18, **2h39 antes**.

## Desfecho
Fechado. 2º turno em 25/10/2026: Flávio Bolsonaro (PL) x Lula (PT).
