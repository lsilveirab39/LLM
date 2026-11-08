# Cena 10: Quanto cabe na mesa?

## Objetivo visual
Uma mesa enche de fichas até o limite da janela de contexto; caderno de cálculos internos (KV Cache) evita refazer operações enquanto o modelo gera, sem implicar memória persistente.

## Conteúdo do slide original
- 10/20
- FASE 5 — CONTEXTO
- Quanto cabe na mesa?
- (Janela de contexto e KV Cache)
- A mesa comporta um número limitado de tokens.
- O KV Cache reaproveita cálculos, não guarda memória permanente.
- CONTEXT WINDOW
- CACHE
- LIMITE
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário tem uma mesa limitada. Sobre ela ficam o pedido, trechos recuperados e a resposta em construção. Se lotar, a aplicação pode reduzir, resumir ou descartar conteúdos antigos. O caderno KV Cache permite reutilizar cálculos sobre fichas já processadas durante a geração.
TÉCNICA — Janela de contexto é o máximo de tokens que o modelo pode considerar em uma operação, sob as restrições concretas da implementação. KV Cache armazena Keys e Values processados para evitar recomputações desnecessárias na geração autoregressiva. Não é memória persistente nem substitui bancos ou arquivos.
EXEMPLO — Um livro enorme pode não caber na mesa; selecionamos apenas os capítulos relevantes.
TRANSIÇÃO — Pedidos claros ajudam a usar melhor o espaço disponível.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
