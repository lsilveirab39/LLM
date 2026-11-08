# Cena 03: O texto vira fichas

## Objetivo visual
Bilhete 'Quem é você?' divide-se em pedaços de texto; cada pedaço recebe ID fictício; os IDs seguem juntos para o modelo. Evidenciar que um token não precisa ser uma palavra.

## Conteúdo do slide original
- 03/20
- FASE 0 — ENTRADA
- O texto vira fichas
- (Tokenização (Tokens e IDs))
- A frase é dividida em partes chamadas tokens.
- Cada parte recebe um ID do tokenizador.
- TEXTO
- TOKEN
- ID
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário recebe um bilhete: Em que ano o Brasil se tornou independente? Ele separa o bilhete em fichas menores. Cada ficha é registrada no catálogo com um número.
TÉCNICA — A tokenização pode dividir palavras em uma ou mais unidades, além de tratar espaços e pontuação. Cada unidade do vocabulário tem um token ID. Os IDs são específicos de um tokenizador, e não universais entre todos os modelos.
EXEMPLO — Não existe obrigação de Brasil possuir o mesmo ID em todos os modelos; um tokenizador pode ainda quebrar uma palavra em pedaços. O ID é apenas índice, não carrega sozinho o significado.
TRANSIÇÃO — Depois das fichas numeradas, elas ganham representações vetoriais.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
