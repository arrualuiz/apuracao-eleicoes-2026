---
numero: 10
titulo: Os estados andam na frente do nacional
hora: "19:28"
tipo: bastidor
manchete: "A soma dos estados ficou sempre ~5 p.p. de seções à frente do arquivo nacional do TSE"
status: fechado
---

## A pergunta
Parece que atualizou duas vezes nos sites, mas o coletor não gravou nada novo. O que houve?

## O que os dados mostraram
Às 19:27, o arquivo nacional do TSE estava parado em 19:14:08 (64,81%). Os estados, porém, já tinham versões novas: BA 19:17:16 (54%), MG 19:16:52 (68%), RJ 19:16:40 (57%), CE 19:17:07 (53%), PE 19:16:39 (60%).

Somando as 27 UFs e o exterior em cada coleta guardada:

| Coleta | Soma das UFs | Arquivo nacional |
|---|---|---|
| 18:18 | 20,80% | 19,54% |
| 18:41 | 43,18% | 36,60% |
| 19:14 | 69,84% | 64,81% |
| 19:28 | 73,58% | 64,81% (parado) |

## Como calculei
O coletor só gravava quando o arquivo **nacional** mudava, e por isso perdia as atualizações dos estados. Mudei para gravar quando **qualquer** arquivo muda, e o nacional passou a ser a soma das UFs. O histórico foi recalculado a partir dos brutos.

## Conclusão
O TSE publica cada estado primeiro e consolida o nacional depois. Somar os estados dá um placar **mais atual que o dos sites** (g1 e UOL mostram o nacional). Depois da correção, entre 19:30 e 19:41 entraram 4 coletas novas com o nacional ainda parado.

## Desfecho
**Confirmado às 20:04.** O arquivo nacional ficou parado em 19:14:08 (64,81%) por 50 minutos. Quando voltou, às 20:04:39, marcou **84,96%**, praticamente o que a soma dos estados já mostrava desde 19:41 (84,93%). Ou seja, durante 50 minutos quem olhava só o nacional (g1, UOL) via um placar ~20 pontos de apuração atrasado.

| Hora | Soma das UFs (nosso) | Nacional do TSE (sites) |
|---|---|---|
| 19:41 | 84,93% | 64,81% (parado desde 19:14) |
| 20:06 | 85,40% | 84,96% (publicado às 20:04:39) |
