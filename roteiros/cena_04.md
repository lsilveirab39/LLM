# Cena 04: Fichas viram vetores

## Objetivo visual
Uma ficha ID vira vetor de três valores ilustrativos. Dois vetores apontam para direções semelhantes e outro diferente. Exibir ângulos simples: direção similar, ortogonal, oposta. Evitar tratar distância física como cosseno.

## Conteúdo do slide original
- 04/20
- FASE 1 — REPRESENTAÇÃO
- Fichas viram vetores
- (Embeddings e similaridade de cosseno)
- Cada token ganha uma representação numérica.
- O ângulo entre vetores pode indicar semelhança.
- ID
- VETOR
- COSSENO
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — Imagine cada ficha colocada num mapa com muitas dimensões. Fichas de temas relacionados podem apontar para direções parecidas.
TÉCNICA — O embedding é um vetor de números, aprendido no treinamento, recuperado a partir do ID. Na similaridade de cosseno comparamos a direção entre dois vetores: 1 é mesma direção, 0 é ortogonal e −1 é direção oposta. Não é a mesma coisa que distância física entre livros.
EXEMPLO — Brasil e Argentina podem ter representações com maior semelhança em uma aplicação de embeddings semânticos do que Brasil e liquidificador. Cada componente do vetor isoladamente não costuma ter interpretação humana simples.
CUIDADO — Na atenção do Transformer normalmente se usam produtos escalares de vetores projetados, não um cálculo explícito de similaridade de cosseno em toda camada.
TRANSIÇÃO — O Transformer combina os vetores considerando a frase toda.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
