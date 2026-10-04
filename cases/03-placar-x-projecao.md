---
numero: 03
titulo: Placar x projeção por estado
hora: "18:18"
tipo: analise
manchete: "Placar 51,1% para o Flávio, projeção 49,0%: já indicava 2º turno"
status: aberto
---

## A pergunta
Se o placar engana por causa da ordem de apuração (case 01), dá para corrigir esse viés e estimar onde a eleição termina?

## O que os dados mostraram
Projeção por estado, que supõe que cada estado termina votando como já votou:

| Hora | Apurado | Placar Flávio | Projeção Flávio | Projeção Lula |
|---|---|---|---|---|
| 18:18 | 20,8% | 51,11% | **49,01%** | 43,07% |
| 18:35 | 36,9% | 50,53% | 48,44% | 43,60% |
| 18:52 | 52,8% | 50,03% | 48,03% | 44,00% |
| 19:14 | 69,8% | 49,28% | 47,73% | 44,33% |
| 19:41 | 84,9% | 48,47% | 47,46% | 44,65% |

Desde a primeira leitura automática, a projeção já ficava **abaixo de 50%**. Ao longo da noite, o placar foi descendo **em direção à projeção**.

## Como calculei
Para cada UF: votos do candidato ÷ fração do eleitorado já apurado. Somo as UFs e divido pelos válidos projetados do mesmo jeito (`projecao()` em `painel.py`). Valores recalculados com a versão final do método (soma das UFs, case 10).

## Conclusão
Uma correção simples, só por estado, antecipou em mais de uma hora o que o placar mostraria depois. Limitação: diferenças **dentro** do estado (capital x interior) não entram na conta. Em SP, por exemplo, os lotes tardios vieram menos favoráveis ao Flávio (case 08).

## Desfecho
_comparar projeção das 18:18 com o resultado final_
