# Cena 14: Uma conexão padronizada

## Objetivo visual
A biblioteca se conecta a serviços externos usando tomadas e etiquetas compatíveis. Mostrar MCP como padrão de comunicação/disponibilização de ferramentas e recursos, não substituto do Tool Calling.

## Conteúdo do slide original
- 14/20
- INTEGRAÇÃO
- Uma conexão padronizada
- (MCP (Model Context Protocol))
- O protocolo organiza acesso a recursos e ferramentas.
- Complementa o Tool Calling; não o substitui.
- CLIENTE
- SERVIDOR
- RECURSOS
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — A biblioteca tem várias salas externas: catálogo, arquivo histórico e serviços. Com um padrão de balcão, o bibliotecário sabe como descobrir os serviços e enviar solicitações sem criar um tipo de telefone para cada sala.
TÉCNICA — O Model Context Protocol define mecanismos padronizados entre aplicações clientes e servidores MCP para disponibilizar ferramentas, recursos e prompts. Uma chamada de ferramenta continua sendo uma ação distinta; MCP organiza como capacidades externas são publicadas e acessadas.
EXEMPLO — Um servidor MCP disponibiliza a busca no catálogo e outro oferece acesso a documentos autorizados.
CUIDADO — MCP não é uma fase interna do Transformer. Cada servidor precisa de controle de acesso, autenticação apropriada, validação de resultados e limitação de permissões.
TRANSIÇÃO — Um manual pode orientar quando usar cada serviço.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
