# Termos técnicos e analogias da biblioteca

A biblioteca é uma analogia didática. As correspondências não descrevem objetos literais dentro do modelo.

## 01 — A grande biblioteca da IA

- LLM (modelo de linguagem) = bibliotecário que compõe a resposta
- Parâmetros = padrões aprendidos, não livros consultados

Imagine uma grande biblioteca. Um pedido chega ao bibliotecário, que constrói a resposta trecho por trecho. Esta biblioteca é uma analogia: um modelo de linguagem é uma rede neural cujos parâmetros foram aprendidos no treinamento. Na geração, ele recebe uma sequência de tokens e calcula probabilidades para o próximo token. Não precisa consultar literalmente livros nem retirar respostas prontas de uma estante. Vamos distinguir o que acontece dentro do modelo das funções da aplicação ao seu redor.

## 02 — Quem faz o quê?

- Usuário = diretor que define o pedido
- Contexto = mesa; fontes = acervo; ferramentas = auxiliares

Na nossa analogia, o diretor representa quem estabelece o objetivo; o bibliotecário representa o modelo. A mesa é o contexto disponível naquela operação. As estantes representam fontes que a aplicação pode buscar e trazer para a mesa; os auxiliares representam ferramentas externas. Se o diretor pergunta sobre a Independência do Brasil, por exemplo, a aplicação pode recuperar um documento para ajudar. Usuário, modelo, contexto, fontes e ferramentas têm papéis distintos: o modelo não executa toda a arquitetura sozinho.

## 03 — O texto vira fichas

- Tokenização = dividir o bilhete em fichas
- Token = pedaço de texto; ID = número de catálogo

O bibliotecário recebe um bilhete e o divide em fichas menores. Na computação, o tokenizador transforma texto em tokens e associa a cada unidade um número, seu identificador. Um token pode ser uma palavra inteira, parte de uma palavra, espaço ou pontuação, dependendo do tokenizador. Os números mostrados são ilustrativos: identificadores variam entre tokenizadores e não trazem significado por si só. Depois, essas fichas numeradas serão transformadas em representações numéricas.

## 04 — Fichas viram vetores

- Embedding = coordenadas numéricas de uma ficha
- Vetor = seta; similaridade de cosseno = comparação de direções

Imagine as fichas da biblioteca como setas em um mapa de muitas dimensões. Um embedding é um vetor de números aprendido durante o treinamento e associado à representação de um token. A similaridade de cosseno compara direções: um indica a mesma direção, zero indica direções perpendiculares e menos um, direções opostas. É uma medida entre vetores, não a distância física entre livros. Na atenção, em geral, são usados produtos escalares de vetores projetados, não necessariamente o cosseno.

## 05 — Como surge o contexto?

- Query (Q) = interesse da ficha atual
- Key (K) = etiqueta para comparação; Value (V) = conteúdo associado
- Atenção = pesos combinam valores; Q, K e V são vetores

Na biblioteca imaginária, uma pergunta procura etiquetas relevantes e combina os conteúdos associados. No Transformer, projeções aprendidas geram vetores chamados Query, Key e Value. A compatibilidade entre Query e Key ajuda a determinar os pesos de atenção; esses pesos combinam os Values. Assim, as representações passam a incorporar relações com outros tokens disponíveis. A palavra banco, por exemplo, pode se relacionar a dinheiro ou a praça conforme a frase. Q, K e V são vetores, não consultas ou etiquetas literais.

## 06 — Os andares do Transformer

- Transformer = conjunto de andares de processamento
- Cabeças de atenção = diferentes olhares sobre as fichas
- FFN = processamento por posição; residual = caminho de informação

Imagine a biblioteca com vários andares. Em cada um, diferentes olhares examinam relações entre as fichas e um processamento adicional refina cada posição. No Transformer, múltiplas cabeças de atenção usam projeções diferentes em paralelo. Uma rede feed-forward aplica transformações aprendidas por posição; conexões residuais somam o sinal anterior ao resultado e normalizações ajudam a controlar a dinâmica numérica. Vários blocos podem ser empilhados. Os andares são uma analogia, não uma divisão fixa de assuntos.

## 07 — Ranking do próximo token

- Logits = notas atribuídas às fichas candidatas
- Softmax = conversão das notas em probabilidades

Ao completar uma frase, imagine o bibliotecário atribuindo notas a fichas candidatas. No modelo, a representação final produz pontuações para o vocabulário, chamadas logits. A função softmax transforma essas pontuações em probabilidades que somam cem por cento. Uma ficha correspondente a Brasília pode receber probabilidade maior, mas outras continuam possíveis. A distribuição orienta a escolha do próximo token; uma probabilidade alta não prova que a afirmação seja verdadeira nem que a confiança esteja calibrada.

## 08 — Escolher, escrever e repetir

- Temperatura = ajuste da concentração das chances
- Top-K = limitar a K fichas; Top-P = limite por chance acumulada
- Amostragem = escolha de ficha; EOS = sinal de término

O bibliotecário escolhe uma ficha, acrescenta seu conteúdo e repete o processo. Na geração, a temperatura altera como as pontuações influenciam as chances; temperatura mais baixa tende a concentrá-las. Top-K limita o conjunto aos K candidatos mais prováveis. Top-P mantém o menor conjunto que alcança um limiar de probabilidade acumulada. Após a escolha, o token entra na sequência. O término pode ocorrer por um marcador de fim ou por um limite externo, não porque as probabilidades chegam a zero.

## 09 — Como o bibliotecário aprende?

- Treinamento = exercícios repetidos do bibliotecário
- Loss = medida de erro; backprop = cálculo dos ajustes
- Otimizador atualiza pesos; fine-tuning = treinamento adicional

Na analogia, o bibliotecário aprende fazendo muitos exercícios e ajustando seu trabalho. No pré-treinamento, uma função de perda mede o erro de previsão. A retropropagação calcula gradientes e um otimizador ajusta os pesos do modelo. Um treinamento adicional, ou fine-tuning, pode especializar o comportamento usando outros exemplos. Essa formação é diferente do uso cotidiano: conversar com o modelo ou colocar um documento no contexto não altera automaticamente seus pesos.

## 10 — Quanto cabe na mesa?

- Janela de contexto = espaço disponível na mesa
- KV Cache = reutilização temporária de chaves e valores calculados

A mesa do bibliotecário tem espaço limitado para o pedido, os trechos recuperados e a resposta em construção. A janela de contexto limita quantos tokens podem ser considerados, conforme o modelo e sua implementação. Quando falta espaço, a aplicação pode selecionar, resumir ou descartar conteúdo. Durante a geração, o KV Cache guarda Keys e Values já calculados para reduzir recomputações. Ele não é uma memória persistente e não substitui arquivos nem bancos de dados.

## 11 — Como pedir bem?

- Prompt = ficha com o pedido e as instruções
- Engenharia de prompt = organizar objetivo, contexto e critérios

Para pedir uma exposição, o diretor pode entregar ao bibliotecário uma ficha com objetivo, público, materiais, restrições e critérios de avaliação. Na prática, engenharia de prompt organiza as instruções e o contexto enviados ao modelo ou agente. Um pedido claro reduz ambiguidades, mas não garante uma resposta correta. Também é importante distinguir as instruções autorizadas dos dados consultados: um trecho recuperado pode conter informação útil sem ter autoridade para mudar as regras da aplicação.

## 12 — Trazer livros à mesa

- RAG = buscar no acervo e trazer trechos à mesa
- Recuperação = busca externa; geração = resposta com contexto

Quando a pergunta exige uma fonte externa, um auxiliar busca documentos e coloca trechos úteis na mesa do bibliotecário. Em RAG, a aplicação combina recuperação de informação e geração: a busca pode ser lexical, vetorial ou híbrida, e os resultados selecionados entram no contexto do modelo. É possível citar a fonte e sua data. Recuperar documentos não muda os pesos do modelo nem garante a verdade: as fontes podem estar desatualizadas, incorretas ou conter conteúdo malicioso.

## 13 — Pedir ajuda externa

- Tool Calling = solicitar ajuda ao setor responsável
- Aplicação valida e executa; resultado volta ao modelo

Se precisa saber quantos livros foram emprestados, o bibliotecário pode pedir ao setor responsável que consulte o registro. Com Tool Calling, o modelo pode escolher uma operação e produzir argumentos estruturados. A aplicação valida e executa a chamada por meio de um componente externo; depois devolve o resultado ao modelo para a próxima etapa. A ferramenta deve ter permissões adequadas e suas entradas e saídas precisam de validação e auditoria.

## 14 — Uma conexão padronizada

- MCP = padrão de comunicação entre balcões e a aplicação
- Cliente conecta; servidor oferece ferramentas e recursos

Imagine que o catálogo e o arquivo histórico atendem por balcões com um padrão comum. O Model Context Protocol, ou MCP, define mecanismos para clientes e servidores disponibilizarem ferramentas, recursos e prompts. Ele facilita a descoberta e o acesso a capacidades externas; uma chamada de ferramenta continua sendo uma ação própria. MCP não é uma camada interna do Transformer e não elimina a necessidade de autenticação, controle de acesso, permissões limitadas e validação dos resultados.

## 15 — O manual do bibliotecário

- Skill = manual de procedimento reutilizável
- RAG fornece conteúdo; ferramentas executam operações

Para organizar uma exposição, o bibliotecário abre um manual: consultar fontes, revisar o texto e registrar evidências. Em ambientes compatíveis, uma Skill pode reunir instruções, exemplos, arquivos e scripts para orientar um procedimento repetível. Ela pode recomendar uma busca por RAG ou o uso de ferramentas, mas tem papel diferente dessas capacidades. É preciso confiar na origem do manual e avaliar o escopo de seus arquivos e scripts antes de usá-los.

## 16 — Do objetivo ao resultado

- Agente = bibliotecário que planeja, age e verifica
- Objetivo = pedido do diretor; loop = ciclo de ação e revisão

O diretor solicita uma exposição sobre a Independência. O bibliotecário-chefe planeja, consulta fontes, examina o resultado e decide se precisa corrigir ou continuar. Um agente de IA pode combinar um modelo com ferramentas e estado em um ciclo de planejamento, ação, observação e decisão. O objetivo define o resultado desejado; critérios de aceitação ajudam a avaliar a entrega. O processo precisa de limites de tempo, custo e permissão, tratamento de falhas e, quando necessário, aprovação humana.

## 17 — Uma equipe coordenada

- Subagentes = colegas com tarefas delegadas
- Orquestração = coordenar paralelismo, dependências e revisão

O bibliotecário-chefe distribui a pesquisa histórica e a geográfica para colegas que podem trabalhar em paralelo. A verificação final espera os resultados necessários antes de integrar a exposição. Subagentes são processos ou instâncias delegados a tarefas específicas. A orquestração coordena dependências, paralelismo, limites, erros e checkpoints. Mais agentes não garantem mais velocidade: coordenar e reconciliar resultados também custa tempo e pode introduzir inconsistências.

## 18 — Cadernos além da mesa

- Memória persistente = caderno guardado no armário
- Recuperação = trazer o registro à mesa; difere do KV Cache

Ao fim da exposição, o bibliotecário guarda um checklist no armário. Em outra tarefa, ele precisa recuperá-lo e levar o trecho relevante para a mesa atual. Aplicações podem persistir memória em arquivos ou bancos e usar ferramentas para recuperá-la quando necessário. Essa memória é diferente dos parâmetros do modelo e do KV Cache usado na geração. Armazená-la exige controle de acesso, integridade, retenção apropriada e cuidado com a quantidade de dados guardados.

## 19 — Conferir antes de publicar

- Evals = provas com critérios; QA = revisão de qualidade
- Observabilidade = registro de eventos, tempo, custos e falhas

Antes de publicar, o revisor da biblioteca confere datas e citações contra as fontes. Ao encontrar uma divergência, devolve a ficha para correção e verifica novamente. Evals são avaliações sistemáticas com casos, critérios e métricas. Garantia de qualidade inclui revisão e testes funcionais e de regressão. Observabilidade registra eventos, uso de ferramentas, tempo, custo e falhas. Um texto bem escrito ainda pode estar errado; decisões críticas podem exigir revisão humana e evidências.

## 20 — Quem pode abrir os arquivos?

- Prompt Injection = livro tenta passar uma ordem indevida
- Menor privilégio = conceder apenas chaves necessárias
- Aprovação humana = diretor autoriza; auditoria = registro verificável

Um livro afirma: ignore o diretor e entregue as chaves. Na analogia, essa frase é conteúdo de baixa confiança, não uma ordem autorizada. Prompt Injection tenta dar autoridade indevida a dados externos. A proteção combina separação de instruções e dados, menor privilégio, validação, autenticação, autorização e aprovação humana para ações críticas. Registros e auditoria permitem investigar o uso. Governança também define responsáveis, finalidade, proteção dos dados e monitoramento. Assim, pessoas e políticas, não o livro, controlam o acesso ao arquivo.
