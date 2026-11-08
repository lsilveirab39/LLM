# Cena 06: Os andares do Transformer

## Objetivo visual
A ficha sobe por três 'andares' da biblioteca, cada um ilustrando atenção em paralelo, análise Feed-Forward e conexão residual como soma com a ficha anterior; legenda de normalização. Andares em sequência, cálculos internos em paralelo.

## Conteúdo do slide original
- 06/20
- FASE 2 — PROCESSAMENTO
- Os andares do Transformer
- (Multi-Head · Feed-Forward · Residual · Norm)
- Várias camadas analisam a mesma sequência.
- Atenção relaciona; Feed-Forward transforma.
- ATENÇÃO
- FFN
- CAMADAS
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — Pense em andares de uma biblioteca. Em cada andar, diferentes bibliotecários observam relações entre fichas e um analista refina cada ficha. A cópia integral da ficha anterior é combinada com o trabalho novo; uma revisão de escala mantém os cálculos estáveis.
TÉCNICA — Multi-Head Attention permite múltiplas projeções em paralelo. Feed-Forward Networks aplicam transformações aprendidas por posição. Conexões residuais somam o sinal anterior ao resultado processado. Normalizações mantêm a dinâmica numérica controlada. Em arquiteturas comuns, muitos blocos são empilhados sequencialmente.
EXEMPLO — Em um andar o modelo pode representar relações próximas, em outro, interações mais abstratas. Essa especialização é uma intuição didática, não uma divisão fixa por temas.
TRANSIÇÃO — Após os andares, o modelo gera pontuações para os possíveis próximos tokens.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
