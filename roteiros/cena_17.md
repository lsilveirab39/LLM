# Cena 17: Uma equipe coordenada

## Objetivo visual
Chefe divide trabalho entre três colegas: História, Geografia e Verificação; duas buscas independentes avançam em paralelo, revisão espera as duas, resultado é integrado. Mostrar dependências e orquestração.

## Conteúdo do slide original
- 17/20
- AGENTES
- Uma equipe coordenada
- (Subagentes e Orquestração)
- O coordenador delega tarefas independentes.
- Reúne resultados, resolve dependências e revisa.
- DELEGAR
- PARALELO
- INTEGRAR
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — Um bibliotecário pesquisa a história, outro a geografia, outro verifica as fontes. O chefe coordena e só junta o material quando as partes estão prontas. Se um precisa da resposta de outro, espera a informação necessária.
TÉCNICA — Subagentes são instâncias ou processos delegados para tarefas específicas. Orquestração define dependências, sequenciamento, paralelismo, limites, agregação, tratamento de erros e checkpoints. As tarefas independentes podem ocorrer em paralelo; as dependentes seguem ordem apropriada.
EXEMPLO — Pesquisa histórica e seleção de imagens podem ocorrer simultaneamente; a revisão final depende de ambas concluírem.
CUIDADO — Mais agentes não garantem ganho de velocidade, pois há overhead de coordenação e risco de inconsistência.
TRANSIÇÃO — Como guardar informações úteis entre tarefas?

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
