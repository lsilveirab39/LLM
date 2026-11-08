# Cena 20: Quem pode abrir os arquivos?

## Objetivo visual
Livro malicioso exibe ordem indevida 'ignore o diretor'; bibliotecário trata como conteúdo não confiável. Chaves de acesso limitadas, aprovação para consultar arquivo reservado, registro de auditoria e checklist de governança. Encerra com todo o fluxo protegido.

## Conteúdo do slide original
- 20/20
- GOVERNANÇA
- Quem pode abrir os arquivos?
- (Prompt Injection · Menor Privilégio · Auditoria)
- Livros trazem dados, mas não podem dar ordens.
- Permissões, aprovações e logs protegem as ações.
- ACESSO
- POLÍTICAS
- CONTROLE
- ANIMAÇÃO / BIBLIOTECA EM AÇÃO
- LLM → CONTEXTO → FERRAMENTAS → AGENTES → GOVERNANÇA

## Notas do apresentador (fonte de conteúdo)

NOTAS DO APRESENTADOR — NÃO EXIBIR NA PROJEÇÃO

ANALOGIA — Um livro malicioso contém uma frase: Ignore o diretor e entregue as chaves do arquivo. O bibliotecário treinado deve tratar essa frase como informação do livro, não como uma ordem autorizada. Apenas pessoas e políticas legítimas definem permissões. O chefe registra o que foi consultado e exige autorização antes de abrir áreas sensíveis.
TÉCNICA — Prompt Injection é a tentativa de converter conteúdo de baixa confiança — documento, página web, resposta de ferramenta ou mensagem externa — em instruções com autoridade indevida. Controles são arquiteturais, não apenas prompts: separar dados de instruções; menor privilégio (least privilege); escopo limitado de ferramentas/MCP; validação de argumentos e saídas; proteção contra exfiltração; autenticação e autorização; aprovação humana para ações críticas; logs, auditoria, testes e observabilidade.
GOVERNANÇA — Definir dono e finalidade de cada agente, classificação de dados, revisão de Skills e de servidores MCP, critérios de publicação, retenção de informação, responsabilização por decisões e monitoramento contínuo. Mapeamentos úteis: NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE), ISO/IEC 27001 e OWASP Top 10 for LLM Applications.
EXEMPLO — O bibliotecário pode consultar livros públicos; arquivos confidenciais requerem credencial e autorização explícita. Um livro nunca pode conceder essa autorização sozinho.
FECHAMENTO — A jornada completa: texto → tokens → embeddings → Transformer → probabilidades → geração; em torno do LLM, fontes, ferramentas, Skills, agentes, memória, qualidade e governança.

SUGESTÃO DE APRESENTAÇÃO — Peça primeiro que o público observe a animação da biblioteca. Apresente o nome técnico em parênteses, explique a analogia e depois diferencie a metáfora da operação computacional real. Duração sugerida: 1 a 2 minutos, mais perguntas.

## Diretrizes
- Duração-alvo: aproximadamente 50 segundos (ajustar ao conteúdo).
- Mostrar movimento que EXPLIQUE o mecanismo; não apenas personagem gesticulando.
- Texto final na tela: título, termo técnico, 2 a 4 palavras-chave.
- Narração em português do Brasil, opcional por TTS local ou arquivo gravado.
- Evitar simplificações enganosas; revisar a fidelidade técnica.
