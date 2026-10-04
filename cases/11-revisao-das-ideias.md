---
numero: 11
titulo: "Revisão às 20h10: o que se confirmou e o que mudou"
hora: "20:10"
tipo: analise
manchete: "A projeção acertou a direção, mas errou para o lado do Flávio: o voto tardio dentro de cada estado veio mais Lula"
status: aberto
---

## A pergunta
Agora que a apuração deu uma travada (~86%), as ideias que tive ao longo da noite se confirmaram ou mudou algo?

## O que os dados mostraram
Placar às 20:10 (soma das UFs, 87,1% das seções): **Flávio 48,31% x Lula 43,66%**. Diferença: Flávio +4,80 milhões de votos.

| Ideia (case) | Na hora | Agora (20:10) | Veredito |
|---|---|---|---|
| 01. O placar parcial engana | Flávio 51,09% com 12% apurado | 48,31% | ✅ confirmou: caiu 2,8 p.p. |
| 03. Projeção por estado | 18:18: projeção 49,0% x placar 51,1% | placar 48,3% | ✅ projeção errou 0,7 p.p.; o placar da hora, 2,8 |
| 03. (continuação) | projeção 49,0% às 18:18 | projeção 47,4% às 20:10 | ⚠️ a projeção também caiu 1,6 p.p. (ver abaixo) |
| 05. Quanto precisa para o 1º turno | precisava de 49,7% do restante | precisa de **60,7%** | ✅ desde 18:46, 10 de 11 lotes abaixo da linha |
| 06. Palpite Flávio 47% | exigia 44,7% do restante | exige 38,7% (lotes recentes: 36–45%) | 🟡 ficou plausível |
| 06. Palpite Lula 42% | exigia 42,4% do restante | já tem 43,66%; exigiria 31,5% | ❌ não deve acontecer |
| 08. SP cada vez menos Flávio | lotes de SP caindo (55 → 51) | margem real +9,8 p.p. x +15,4 previstos | ✅ SP rendeu 548 mil, não 866 mil |
| 09. Lotes com saldo Flávio derrubando o % dele | até 19:14 | desde 19:14, os lotes dão saldo ao **Lula** | 🔄 a fase mudou |
| 10. Estados à frente do nacional | soma das UFs ~20 p.p. à frente | nacional alcançou às 20:04 | ✅ confirmou |

**Por que a projeção também caiu.** Ela supõe que o que falta de cada estado vota igual ao já apurado nele. Nos votos que entraram depois das 19:14, isso não se manteve:

| Estado | Margem F−L prevista | Margem real dos votos novos | Saldo previsto | Saldo real |
|---|---|---|---|---|
| SP | +15,4 | **+9,8** | +866 mil | +548 mil |
| MG | +7,1 | +4,4 | +174 mil | +109 mil |
| RJ | +14,5 | +13,7 | +350 mil | +330 mil |
| BA | −34,8 | −36,2 | −672 mil | −700 mil |
| CE | −28,4 | −31,6 | −364 mil | −405 mil |
| PE | −29,8 | −32,5 | −429 mil | −468 mil |
| **10 maiores** | | | **−144 mil** | **−668 mil** |

Nos estados onde o Flávio lidera, o voto tardio veio **menos** Flávio. Nos estados do Lula, veio **mais** Lula. A projeção errou ~0,5 milhão de votos só nesse trecho, sempre para o lado do Flávio.

## Como calculei
Consultas no banco `dados/apuracao.sqlite`: placar e "quanto precisa" na coleta mais recente; % de cada lote desde 18:46; e, por UF, a margem acumulada às 19:14 (o que a projeção supunha) comparada à margem dos votos que entraram entre 19:14 e 20:10.

## Conclusão
- **Direção:** tudo o que apontava para queda do Flávio e 2º turno se confirmou.
- **Tamanho:** a projeção por estado subestimou o Lula de forma sistemática, porque o voto tardio é diferente do voto inicial **dentro** do mesmo estado (provavelmente capitais e grandes cidades apuradas por último). Uma projeção melhor precisaria olhar município ou zona, não só estado.
- **Palpite:** o 47% do Flávio ficou plausível; o 42% do Lula já ficou para trás.

## Desfecho
**Checagem 20:14 (89,1%, `analise/revisao.py`):** Flávio 48,14% x Lula 43,86%, diferença 4,53 mi. O último lote (2,5 mi de válidos) foi o mais favorável ao Lula da noite: 52,0% x 41,1%. **Em 7 dos 8 maiores estados desse lote, os votos novos vieram mais Lula que o acumulado** (SP −4, RJ −3, MG −3, BA −5, CE −3, PE −6, GO −4 p.p.). O viés da projeção cresceu: nos 8 maiores estados, desde 19:14, previa um saldo de 488 mil para o Lula e o real foi de 1,14 mi (erro de 650 mil a favor do Flávio).

_comparar no fim: placar final x projeção das 18:18, das 19:14 e das 20:10_
