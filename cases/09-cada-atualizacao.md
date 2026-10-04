---
numero: 09
titulo: Cada atualização favoreceu quem, e por quanto
hora: "19:28"
tipo: analise
manchete: "O maior lote da noite deu +431 mil ao Flávio e mesmo assim derrubou o percentual dele"
status: aberto
---

## A pergunta
Cada vez que entraram dados, quem foi favorecido e por quanto? Quero um gráfico dos crescimentos por candidato e o mesmo por estado.

## O que os dados mostraram
| Atualização | Válidos novos | Saldo do lote |
|---|---|---|
| 18:18 → 18:22 | 4,4 mi | Flávio +318 mil |
| 18:22 → 18:27 | 6,4 mi | Flávio +507 mil |
| 18:27 → 18:28 | 0,6 mi | Lula +41 mil |
| 18:28 → 18:35 | 7,2 mi | Flávio +655 mil |
| 18:35 → 18:41 | 7,4 mi | Flávio +548 mil |
| 18:41 → 18:46 | 4,7 mi | Flávio +198 mil |
| 18:46 → 18:52 | 6,7 mi | Flávio +393 mil |
| 18:52 → 19:14 | **20,6 mi** | Flávio +431 mil (47,1% x 45,0%) |
| 19:14 → 19:28 | 4,6 mi | **Lula +115 mil** (44,8% x 47,4%) |

**O paradoxo:** o lote das 19:14 deu 431 mil votos a mais ao Flávio, mas com margem de só 2 p.p., contra ~8 p.p. no acumulado. Por isso o **percentual** dele caiu, mesmo com saldo positivo.

**No saldo da noite, por estado** (até 19:28):
- **Flávio:** SP +2,32 mi, SC +1,31 mi, PR +797 mil, RJ +681 mil, RS +647 mil, GO +533 mil, MG +436 mil.
- **Lula:** BA +1,35 mi, PE +804 mil, CE +695 mil, MA +588 mil.
- **Pará:** praticamente empatado.

## Como calculei
Diferença de votos entre coletas consecutivas, com o nacional calculado como soma das UFs (case 10). Gráficos no `painel.html`: "Cada atualização: quem ela favoreceu e por quanto" e "O mesmo, por estado" (mesma escala em todos os quadros).

## Conclusão
"Favorecer" tem dois sentidos: **saldo de votos** (quem ganhou mais no lote) e **efeito no percentual** (o lote veio acima ou abaixo da média). Durante quase toda a noite os lotes deram saldo ao Flávio e, ao mesmo tempo, reduziram a vantagem percentual dele.

## Desfecho
**Checagem parcial (20:10, 87%):** desde 19:14 a fase mudou. A maioria dos lotes passou a dar saldo ao **Lula** (o de 19:30, por exemplo, teve 10,8 mi de válidos com 45,3% x 47,0%).

_a preencher_
