---
numero: 16
titulo: "Abstenção e 2º turno: quem cresce de um turno para o outro"
hora: "20:45"
tipo: analise
manchete: "Quem liderou o 1º turno venceu os seis 2º turnos desde 2002, mas em cinco deles quem ficou em 2º ganhou mais votos entre os turnos. A abstenção de 2026 caminha para o recorde de 1º turno"
status: aberto
---

## A pergunta
A abstenção é muito alta todo ano. Como foi nos anos com 2º turno? Quem ganhou mais votos de um turno para o outro, e quem melhorou ou piorou em cada cenário?

## O que os dados mostraram
Dados oficiais do TSE (dados abertos, 2002–2022), em `dados/historico/presidente_turnos.csv` e `presidente_votos.csv`.

**Abstenção (% do eleitorado):**

| Ano | 1º turno | 2º turno | Variação |
|---|---|---|---|
| 2002 | 17,74% | 20,47% | +2,7 p.p. (+3,1 mi) |
| 2006 | 16,75% | 18,99% | +2,2 p.p. (+2,8 mi) |
| 2010 | 18,12% | 21,50% | +3,4 p.p. (+4,6 mi) |
| 2014 | 19,39% | 21,10% | +1,7 p.p. (+2,4 mi) |
| 2018 | 20,33% | 21,30% | +1,0 p.p. (+1,4 mi) |
| 2022 | 20,95% | **20,58%** | **−0,4 p.p. (−0,6 mi)** |
| 2026 | **21,01%** (parcial, 92% apurado) | | |

- A abstenção sobe no 2º turno em todos os anos, **menos em 2022**: a disputa mais apertada da série mobilizou mais gente.
- A tendência de longo prazo é de alta: de 16,8% (2006) para ~21% hoje. **2026 caminha para a maior abstenção de 1º turno da série.**

**Quem ganhou votos entre os turnos** (1º colocado x 2º colocado do 1º turno):

| Ano | 1º turno | 2º turno | Ganho do 1º colocado | Ganho do 2º colocado |
|---|---|---|---|---|
| 2002 | Lula 46,4 x Serra 23,2 | Lula 61,3 | +13,3 mi | **+13,7 mi** |
| 2006 | Lula 48,6 x Alckmin 41,6 | Lula 60,8 | **+11,6 mi** | **−2,4 mi** (perdeu votos) |
| 2010 | Dilma 46,9 x Serra 32,6 | Dilma 56,1 | +8,1 mi | **+10,6 mi** |
| 2014 | Dilma 41,6 x Aécio 33,6 | Dilma 51,6 | +11,2 mi | **+16,1 mi** |
| 2018 | Bolsonaro 46,0 x Haddad 29,3 | Bolsonaro 55,1 | +8,5 mi | **+15,7 mi** |
| 2022 | Lula 48,4 x Bolsonaro 43,2 | Lula 50,9 | +3,1 mi | **+7,1 mi** |

- **Em 5 de 6 eleições, o 2º colocado ganhou mais votos entre os turnos** (ficou com 51% a 70% dos votos novos). A exceção é 2006, em que o Alckmin teve menos votos no 2º turno que no 1º.
- **Mesmo assim, o 1º colocado venceu todos os seis 2º turnos.** Em 2014 e 2022, a diferença encolheu muito (2022: de 5,2 p.p. para 1,8 p.p.), mas não virou.
- **Brancos e nulos** caem no 2º turno na maioria dos anos (eleitores dos eliminados escolhem um lado), mas subiram em 2018 e 2022.

## Como calculei
`analise/historico_tse.py` baixa o `detalhe_votacao_munzona` (aptos, comparecimento, abstenção, brancos, nulos) e só o `*_BR.csv` do `votacao_partido_munzona` de cada ano, lendo o zip remoto por partes (HTTP Range) em vez dos ~400 MB do arquivo completo. Para presidente, voto no partido = voto no candidato. Abstenção de 2026: abstenções ÷ eleitorado das seções já apuradas (banco SQLite, 20:44).

## Conclusão
Para o 2º turno de 2026, a história dá dois sinais opostos:
- **A favor do Flávio** (líder do 1º turno): o líder venceu as seis disputas. Além disso, os outros candidatos de 2026, que somam ~8% e ~9 milhões de votos (Cury, Caiado, Renan Santos, Zema), vêm majoritariamente do campo da direita e do centro-direita.
- **A favor do Lula** (2º colocado): o 2º colocado costuma ganhar mais votos entre os turnos. Com uma diferença de ~2,4 p.p. no 1º turno (case 12), menor que a de 2022 (5,2), basta ele ficar com uns 65–70% dos votos novos, como o Bolsonaro em 2022 e o Haddad em 2018, para a disputa ficar empatada ou virar.

A abstenção é a terceira variável: em 2022 ela caiu no 2º turno, e quem mobilizar quem não votou no 1º pode decidir.

## Desfecho
_2º turno de 25/10: abstenção __%; Flávio ganhou __ mi e Lula __ mi entre os turnos._
