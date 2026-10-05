---
numero: 15
titulo: "Quatro apurações: 2018, 2022 (dois turnos) e 2026"
hora: "20:35"
tipo: analise
manchete: "Em todas as apurações, quem é mais forte no Sul e no Sudeste começa à frente e perde terreno até o fim; aplicando a reta final de cada uma a 2026, Flávio termina entre +1,7 e +3,4 p.p."
status: aberto
---

## A pergunta
Quero lembrar como foram 2018, 2022 e 2026. As curvas parecem bem diferentes, e é nelas que eu quero me basear.

## O que os dados mostraram
Achei a evolução minuto a minuto do **2º turno de 2018** num infográfico do g1 (fonte TSE; prints em `prints/2018-t2-*`). Transcrevi as 320 linhas para `dados/historico/2018-t2-g1-minuto.csv`. O final confere com o oficial: Bolsonaro 57.797.847 votos, 55,13%.

**Diferença direita − PT por % apurado** (entre parênteses, quanto ainda faltava andar até o resultado final):

| % | 2018 2º turno | 2022 1º turno | 2022 2º turno | 2026 1º turno |
|---|---|---|---|---|
| 2% | +24,3 (−14,0) | +7,4 (−12,6) | +12,8 (−14,6) | +7,3 |
| 10% | +22,0 (−11,7) | +5,5 (−10,7) | +4,1 (−5,9) | +10,2 |
| 20% | +18,1 (−7,9) | +4,6 (−9,8) | +3,1 (−4,9) | **+10,5** |
| 50% | +13,9 (−3,7) | +1,5 (−6,7) | +0,6 (−2,4) | +8,6 |
| 70% | +13,0 (−2,7) | −0,2 (−5,0) | −0,1 (−1,7) | +6,7 |
| 90% | +11,8 (−1,5) | −2,8 (−2,4) | −1,1 (−0,7) | +4,1 |
| Final | **+10,3** | **−5,2** | **−1,8** | ? (+3,7 com 92%) |

**O padrão comum:** nas três apurações completas, o candidato da direita começa com vantagem maior que a final e perde terreno até o fim, sempre na mesma direção. É a ordem regional da apuração (Sul e Sudeste primeiro, Nordeste depois).

**As formas diferentes:**
- **2018 e 2022, 2º turno:** a queda é rápida no começo (a maior parte do ajuste acontece até ~20%) e depois a curva fica quase plana.
- **2022, 1º turno:** a queda é espalhada e continua forte até o fim. Ainda faltavam 2,4 p.p. a partir de 90%.
- **2026, 1º turno:** é a única curva em que a direita **sobe** no começo (até 20%). Depois disso, cai no ritmo de 2022 1º turno.

**Aplicando a "reta final" de cada eleição (o que ainda andou a partir de 90%) aos +4,1 de 2026 com 90%:**

| Se 2026 terminar como… | Andou a partir de 90% | Flávio − Lula final |
|---|---|---|
| 2022 1º turno | −2,4 | **+1,7** |
| 2018 2º turno | −1,5 | **+2,6** |
| 2022 2º turno | −0,7 | **+3,4** |

## Como calculei
- **2018 2º turno:** % apurado = válidos acumulados ÷ válidos finais (104.838.753). Diferença = 2 × % Bolsonaro − 100.
- **2022, dois turnos:** séries do UOL (`dados/uol-historico-2022*.json`, locais).
- **2026:** UOL + soma das UFs.
- Para cada %, o ponto mais próximo de cada série (até 3 p.p. de distância).

## Conclusão
As curvas parecem diferentes, mas contam a mesma história: **o começo da apuração favorece quem é forte no Sul e no Sudeste, e a reta final favorece quem é forte no Nordeste** (nessas eleições, a direita e o PT, respectivamente). Variam a intensidade e o momento. A faixa para 2026 (de +1,7 a +3,4, centro em ~+2,5) coincide com as projeções do case 12 (~+2,4). Três métodos independentes apontam para o mesmo lugar.

Para o **2º turno de 2026** (25/10), já temos as duas referências de 2º turno (2018 e 2022), com a forma típica: ajuste rápido até ~20% e depois quase plano.

## Desfecho
_diferença final de 2026: ___. Qual eleição a reta final de 2026 mais imitou?_

**Lacuna:** falta o **1º turno de 2018**, que seria a comparação mais direta com 2026. Ver o case 14 para reconstruí-lo pelos boletins de urna.
