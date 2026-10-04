# Diário da apuração — 04/10/2026

## 18:07
- 12% das urnas apuradas, Flávio Bolsonaro na frente.

## 18:13 — 12,45% apurado (UOL)
- Flávio 51,09% (7.369.884) x Lula 40,71% (5.872.874). Cury 2,98%, Caiado 2,39%.
- Flávio acima de 50% dos válidos: se fosse o resultado final, ganharia no 1º turno.
- Apuração desigual: PR ~39%, RS/PA ~24%, mas SP ~4%, RJ ~3%, BA ~5%, PE/CE ~6%.
- Sul (favorável ao Flávio) está bem mais adiantado que o Nordeste (favorável ao Lula).
- MG (g1, 13%): Flávio 49,1 x Lula 41,5. MG costuma acompanhar o resultado nacional.
- Para fechar acima de 50%, o Flávio precisa de ~49,8% dos válidos restantes: está no limite.

## 18:18 — 21,96% apurado (TSE, coleta automática)
- Fonte oficial: API do TSE, eleição 6257 (Presidente 1º turno). A coleta passou a ser automática a cada 3 min.
- Flávio 51,17% (11.520.790) x Lula 40,72% (9.168.405).
- Projeção por estado (cada UF termina como está, peso = eleitorado): **Flávio 49,1% x Lula 42,9%, indica 2º turno**.
- O que falta apurar: SP 25% (Flávio 58 x 33), MG 11%, RJ 10%, BA 8% (Lula 64 x 30), PE/CE 5% cada.
- SP joga a favor do Flávio; o Nordeste (BA, PE, CE, MA, PI, RN, AL, SE) joga a favor do Lula.
- O print do g1 aparece com alguns minutos de atraso em relação ao TSE (18:11 vs 18:16).

## 18:46 — 41,57% apurado (TSE)
- Flávio 50,41% x Lula 41,44%. Último lote: Flávio 48,8% x Lula 43,0%, o primeiro claramente abaixo dos 49,7% que ele precisa.
- **Correção:** o % de urnas das coletas automáticas estava adiantado (vinha do -ab.json). Recalculado a partir dos brutos.
- **Meu palpite (18:48): Flávio 47% x Lula 42%.**
  - Projeção por estado no mesmo momento: Flávio 48,2% x Lula 43,9%.
  - Para dar 47 x 42, o Flávio precisaria de 44,7% dos válidos restantes (vem fazendo 49–50%) e o Lula de 42,4% (vem fazendo 42–43%).
  - 47 + 42 = 89% deixaria 11% para os outros; hoje eles somam 8,2%.

## 19:14 — 64,81% apurado (TSE) · Flávio cai abaixo de 50%
- O TSE ficou 25 min sem publicar (versão das 18:48:59 até 19:14:08) e depois soltou um lote grande: 47% → 65% das seções.
- Lote: 21 milhões de válidos, Flávio 48,0% x Lula 43,9%.
- Placar: **Flávio 49,58% x Lula 42,25%**. Primeira leitura com o Flávio abaixo de 50%.
- Agora ele precisa de 50,7% dos válidos restantes para voltar a 50%; o último lote deu 48,0%.
- Projeção por estado: Flávio 47,7% x Lula 44,3%.
- O que falta: SP (10,6 mi, Flávio 52,8), RJ (6,5 mi, Flávio 53,5), MG (6,2 mi), BA (6,1 mi, Lula 64,5), CE e PE (~3,5 mi cada, Lula 61–62).

## 19:14 — análise estado a estado (variacao.py, 18:52 → 19:14)
- Saldo esperado do que falta: Lula +4,63 mi (BA +1,60 mi, CE +0,83, PE +0,81, MA +0,52) x Flávio +3,22 mi (SP +1,20 mi, RJ +0,70, SC +0,36, MG +0,32).
- Diferença atual: Flávio +5,56 mi → projetada no fim: Flávio +4,15 mi.
- **SP:** cada lote novo vem menos Flávio que o acumulado (lotes de 55x35 → 51x39). Se continuar, o saldo de SP para o Flávio fica abaixo do 1,2 mi projetado.
- Na maioria dos estados, os lotes recentes vieram mais favoráveis ao Lula que o acumulado (PI −6, GO −5, AM −11, MA −4).

## 20:06 — 85,4% apurado · o nacional do TSE alcança os estados
- O arquivo nacional do TSE ficou parado de 19:14:08 a 20:04:39 (50 min). Os estados publicaram até ~19:32 e depois também pararam.
- Às 20:04 o nacional voltou com 84,96%, igual à nossa soma dos estados das 19:41 (84,93%). Confirma o case 10.
- Placar (soma UFs, 20:06): **Flávio 48,44% x Lula 43,51%**. Projeção por estado: 47,6% x 44,5%.
- variacao.py: diferença atual Flávio +5,0 mi; o que falta soma Lula +2,85 mi x Flávio +1,21 mi; projetado no fim Flávio +3,4 mi.
- Organização: projeto em pastas (coleta/, analise/, painel/, legado/) e repositório renomeado para noite-da-apuracao-2026.
