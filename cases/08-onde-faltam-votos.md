---
numero: 08
titulo: Onde ainda faltam votos e para quem pesam
hora: "19:14"
tipo: analise
manchete: "A Bahia ainda tinha mais saldo a entregar que São Paulo inteiro"
status: aberto
---

## A pergunta
Dos estados com eleitores em disputa, o que mudou de uma leitura para outra? Onde mais faltam votos e que tendência aparece?

## O que os dados mostraram
Saldo esperado do que faltava (18:52 → 19:14), supondo que cada estado continue votando como está:

| Para o Lula | Saldo | Para o Flávio | Saldo |
|---|---|---|---|
| Bahia (49% apurado) | +1,60 mi | São Paulo (70%) | +1,20 mi |
| Ceará (50%) | +0,83 mi | Rio de Janeiro (53%) | +0,70 mi |
| Pernambuco (55%) | +0,81 mi | Santa Catarina (81%) | +0,36 mi |
| Maranhão (59%) | +0,52 mi | Minas Gerais (62%) | +0,32 mi |
| **Total** | **+4,63 mi** | **Total** | **+3,22 mi** |

Diferença no momento: Flávio +5,56 mi. Projetada para o fim: **Flávio +4,15 mi**.

**Tendência de São Paulo** (cada lote menos favorável ao Flávio):

| Lote | Flávio x Lula |
|---|---|
| 18:22 | 54,9 x 35,5 |
| 18:41 | 52,6 x 37,5 |
| 19:14 | 51,0 x 39,0 |

Na maioria dos estados, os lotes recentes vieram mais favoráveis ao Lula que o acumulado: PI −6 p.p., GO −5, AM −11, MA −4.

## Como calculei
`variacao.py`. Válidos que faltam por UF = válidos ÷ fração apurada − válidos; saldo = válidos que faltam × (% Flávio − % Lula). `variacao.py --todas SP` mostra a série de um estado.

## Conclusão
O "quanto falta" sozinho engana. O que importa é **quanto falta × a margem local**. E a tendência **dentro** do estado (SP cada vez menos Flávio) indica que a projeção por estado ainda era um pouco otimista para ele.

## Desfecho
**Checagem parcial (20:10, 87%):** a tendência de SP se confirmou. Nos votos que entraram depois das 19:14, a margem do Flávio em SP foi +9,8 p.p. (previsto +15,4): 548 mil de saldo em vez de 866 mil. BA, CE e PE deram ainda mais ao Lula que o previsto.

_conferir o saldo real de BA e SP no fim_
