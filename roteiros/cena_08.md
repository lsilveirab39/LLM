# Cena 08: Escolher, escrever e repetir

## Objetivo visual
Probabilidades em barras mudam de concentração com temperatura; filtros Top-K e Top-P removem candidatos, um token é escolhido e adicionado ao texto. Repetir ciclo e mostrar cartão especial de fim de sequência (EOS).

## Conteúdo do slide original
- 08/20
- FASE 4 — GERAÇÃO
- Escolher, escrever e repetir
- (Temperatura · Top-K · Top-P · EOS)
- A escolha do próximo token pode ser mais ou menos variada.
- Um token especial ou limite pode encerrar a resposta.
- AMOSTRAGEM
- SAÍDA
- PARADA
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário vê várias fichas candidatas. Temperatura baixa tende a favorecer as mais pontuadas; temperatura alta espalha as chances. Top-K mantém somente K candidatos, e Top-P mantém o menor conjunto cuja probabilidade acumulada atinge um limiar.
TÉCNICA — Essas são estratégias de decodificação, posteriores à produção de logits. A cada escolha, o token é adicionado ao contexto e a inferência continua. Um token de fim de sequência, conforme o formato do modelo, pode sinalizar encerramento. O sistema também pode interromper pelo limite de tokens de saída.
EXEMPLO — Se os candidatos têm 60%, 20%, 10%, 6% e 4%, Top-K=2 mantém os dois primeiros e Top-P=0,9 mantém os três primeiros antes da renormalização e escolha.
CUIDADO — O modelo não para por falta de ideias ou porque as probabilidades chegaram a zero. Ele pode selecionar o marcador de término, ou atingir limite externo.
TRANSIÇÃO — Mas como ele aprendeu a calcular tudo isso?

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
