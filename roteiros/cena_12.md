# Cena 12: Trazer livros à mesa

## Objetivo visual
Bibliotecário consulta catálogo externo, seleciona páginas relevantes, traz apenas trechos à mesa, depois redige resposta com indicação de fonte. Diferenciar RAG de alterar pesos do modelo.

## Conteúdo do slide original
- 12/20
- FONTES EXTERNAS
- Trazer livros à mesa
- (RAG (Retrieval-Augmented Generation))
- A aplicação recupera trechos relevantes de fontes.
- Os documentos entram no contexto antes da resposta.
- BUSCA
- FONTES
- CONTEXTO
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — O bibliotecário recebe uma pergunta sobre um evento recente e pede ao auxiliar que procure um livro ou documento atual. Os trechos mais úteis são colocados sobre a mesa.
TÉCNICA — RAG é uma arquitetura que combina recuperação de informação com geração de texto. A busca pode ser vetorial, lexical ou híbrida. Documentos selecionados são adicionados ao contexto do modelo gerador. A recuperação geralmente ocorre antes da inferência final, mas a consulta de busca também pode ser transformada por outros modelos.
EXEMPLO — Buscar o documento oficial sobre o tema e usar os trechos para escrever a resposta, citando fonte e data.
CUIDADO — RAG não altera pesos e não garante verdade; documentos podem ser antigos, incorretos ou maliciosos.
TRANSIÇÃO — Além de buscar informação, o sistema pode precisar executar uma operação.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
