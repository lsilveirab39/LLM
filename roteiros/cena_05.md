# Cena 05: Como surge o contexto?

## Objetivo visual
Uma consulta de biblioteca aparece como Query; fichas com etiquetas são Keys; conteúdos são Values. A Query destaca fichas mais compatíveis com pesos graduais e combina seus conteúdos; indicar que é metáfora de operações matemáticas.

## Conteúdo do slide original
- 05/20
- FASE 2 — PROCESSAMENTO
- Como surge o contexto?
- (Transformer e Self-Attention (Q·K·V))
- A atenção avalia quais tokens se relacionam.
- Query procura, Key sinaliza, Value contribui.
- QUERY
- KEY
- VALUE
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário pergunta pelo tema Geografia. A Query é o assunto procurado; as Keys são etiquetas das fichas; os Values são os conteúdos úteis. Ele não lê tudo com o mesmo peso, mas combina o que for mais relevante.
TÉCNICA — A partir dos vetores, projeções aprendidas geram Query, Key e Value. A compatibilidade entre Q e K determina pesos de atenção. Esses pesos combinam os Values para produzir representações contextuais. Isso ajuda uma palavra como banco a se relacionar a dinheiro ou praça dependendo da frase.
EXEMPLO — Em que ano o Brasil se tornou independente? A expressão em que ano faz o modelo considerar relações com tempo, enquanto Brasil e independente especificam o evento.
CUIDADO — Q, K e V são vetores e não textos de pesquisa reais. O bibliotecário é analogia, não um processo de leitura literal.
TRANSIÇÃO — Um bloco de atenção não é o único cálculo do Transformer.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
