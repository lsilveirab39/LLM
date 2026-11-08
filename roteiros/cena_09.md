# Cena 09: Como o bibliotecário aprende?

## Objetivo visual
Supervisor propõe exercícios; biblioteca prevê token, compara resultado com referência, vê indicador de erro (loss), ajusta engrenagens e repete. Sinalizar treinamento separado de inferência; Fine-Tuning como curso extra.

## Conteúdo do slide original
- 09/20
- APRENDIZADO
- Como o bibliotecário aprende?
- (Treinamento · Loss · Backprop · Fine-Tuning)
- Ele prevê, mede o erro e ajusta parâmetros.
- Ajuste fino é um treinamento complementar.
- PREVER
- MEDIR ERRO
- AJUSTAR
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — No início, o bibliotecário não sabe bem completar frases. Um supervisor entrega exercícios; ele tenta, é avaliado e ajusta critérios de trabalho milhares ou milhões de vezes. Depois de sua formação geral, pode fazer um curso complementar.
TÉCNICA — Pré-treinamento usa uma função de perda (loss) para medir o erro de previsão. Backpropagation calcula gradientes que um otimizador usa para ajustar os pesos. Fine-tuning é treinamento adicional, muitas vezes supervisionado, em exemplos específicos.
EXEMPLO — Dado A capital do Brasil é..., o sistema aprende a aumentar a probabilidade de Brasília em contextos apropriados.
CUIDADO — Usar o modelo numa conversa, consultar um documento em RAG ou colocar informações no contexto não altera automaticamente os pesos do modelo.
TRANSIÇÃO — Durante o uso, existe um limite de informação disponível a cada vez.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
