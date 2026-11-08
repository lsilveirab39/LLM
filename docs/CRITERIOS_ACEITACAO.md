# Critérios de aceitação

## Conteúdo e didática
- [ ] Exatamente 20 cenas, alinhadas aos 20 slides de origem e preservando a ordem.
- [ ] Analogia da biblioteca presente em todas as cenas e coerente com as notas.
- [ ] Termos técnicos corretos e identificados (tokens, IDs, embeddings, cosseno, Q/K/V, FFN, logits, Softmax, temperatura, Top-K, Top-P, EOS, loss, backprop, janela de contexto, KV Cache, RAG, Tool Calling, MCP, Skills, agents, orquestração, memória, evals, governança).
- [ ] Animações demonstram o mecanismo em cada etapa; não apenas movimentos repetitivos do bibliotecário.
- [ ] Distinção clara entre componentes internos do LLM e integração externa ao modelo.
- [ ] Cena final inclui Prompt Injection, fronteiras de confiança, menor privilégio, aprovação humana, logs, auditoria, qualidade e governança.

## Vídeo, apresentação e acessibilidade
- [ ] Uma cena MP4 por slide: `output/scenes/scene_XX.mp4`, MP4 H.264 em 1920×1080, 16:9, sem marca d'água.
- [ ] Filme completo `output/IA_Biblioteca_Filme_Completo.mp4`, ordenado de 01 a 20, com áudio/narração somente se gerado com recurso permitido.
- [ ] Legendas SRT sincronizadas; roteiro de narração pt-BR disponível independentemente de TTS.
- [ ] Títulos e palavras-chave legíveis em tela móvel; contraste apropriado; cuidado com movimento excessivo.
- [ ] Notas do apresentador da apresentação original preservadas integralmente no material de referência.
- [ ] Eventual PowerPoint com vídeos incorporados é testado em PowerPoint desktop (ou sua limitação documentada).

## Engenharia, custo e QA
- [ ] Sem APIs pagas obrigatórias, sem chaves no repositório e sem dependências não justificadas.
- [ ] Código-fonte de geração versionado, instruções reproduzíveis e scripts de renderização.
- [ ] `ffprobe` valida cada MP4; amostras de frames revisadas; relatório QA por cena.
- [ ] Testes automatizados e QA factual documentados.
- [ ] Sem alegar que outputs existem quando não foram renderizados.
