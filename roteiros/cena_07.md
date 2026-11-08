# Cena 07: Ranking do próximo token

## Objetivo visual
Fichas candidatas para 'A capital do Brasil é...' recebem notas e barras de logits; as barras transformam-se em probabilidades via Softmax; uma ficha continua destacada, ainda sem ser escolhida.

## Conteúdo do slide original
- 07/20
- FASE 3 — PREDIÇÃO
- Ranking do próximo token
- (Logits e Softmax)
- O modelo dá uma pontuação aos candidatos.
- As pontuações são convertidas em probabilidades.
- LOGITS
- SOFTMAX
- CHANCES
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário termina a frase O ano foi... e monta uma lista de fichas candidatas. Cada uma recebe uma nota.
TÉCNICA — A representação final é projetada sobre o vocabulário, gerando logits, pontuações não normalizadas. A função softmax transforma logits em uma distribuição de probabilidades que soma 100%.
EXEMPLO — A resposta pode favorecer uma ficha com 1822, mas o modelo também atribui probabilidades a outros candidatos. Essas probabilidades não são uma medida de verdade factual nem confiança calibrada.
TRANSIÇÃO — A etapa seguinte escolhe um desses tokens e prossegue.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
