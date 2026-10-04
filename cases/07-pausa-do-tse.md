---
numero: 07
titulo: "Ficou sem atualizar: a pausa do TSE"
hora: "19:14"
tipo: bastidor
manchete: "25 minutos parado e depois um lote de 20,6 milhões de votos"
status: fechado
---

## A pergunta
Ficou um tempo sem atualizar e atualizou agora. Foi o coletor que falhou?

## O que os dados mostraram
O log mostrou o coletor consultando a cada 3 min (18:56, 18:59, 19:02, 19:05, 19:08, 19:11), sempre com o arquivo nacional do TSE na versão **18:48:59**. Às **19:14:08** saiu um lote enorme: de 47% para 65% das seções no arquivo nacional, com **20,6 milhões** de válidos novos.

## Como calculei
`status.py` mostra o intervalo entre coletas, se cada pasta está completa (30 JSON) e a versão do TSE de cada coleta.

## Conclusão
A pausa era do arquivo nacional do TSE, não do coletor. A investigação revelou algo mais importante: **os estados continuavam publicando nesse intervalo** (case 10).

## Desfecho
Fechado.
