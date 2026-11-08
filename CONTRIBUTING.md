# Como contribuir

Obrigado por ajudar a tornar IA compreensível. Você pode contribuir em português, propondo correções, explicando uma dúvida ou enviando melhorias. Antes de uma mudança grande, abra uma issue para combinar o objetivo e verificar se há trabalho semelhante.

1. Escolha uma etapa em [roteiros/INDICE_20_CENAS.md](roteiros/INDICE_20_CENAS.md), descreva o público e a dificuldade encontrada.
2. Compare slide, notas, roteiro, glossário e vídeo. Preserve os arquivos originais e trabalhe em uma branch própria.
3. Explique o conceito com uma analogia clara e, em seguida, diferencie-a do mecanismo real. Inclua um exemplo curto e evite afirmar que a metáfora é literal.
4. Se alterar uma animação, faça o movimento demonstrar o conceito; mantenha personagem e linguagem visual consistentes. Respeite as 20 etapas e sua ordem, salvo decisão discutida no projeto.
5. Se alterar narração ou legenda, revise pronúncia, tempo de leitura e sincronia. Ao alterar o PowerPoint, preserve as notas e explique como a reprodução foi testada. Não sobrescreva a apresentação original; use outro nome.
6. Execute `python scripts/validar_fontes.py` e os testes relevantes. Para vídeos, use `python scripts/qa_videos.py` e inclua resolução, duração, codec, quadros examinados e limitações. Os caminhos e dependências estão em [animacoes/README.md](animacoes/README.md).
7. Abra um pull request pequeno, descrevendo problema, solução, arquivos afetados e testes; inclua capturas ou amostras quando ajudarem na revisão. Indique claramente o que não foi testado.

A revisão deve considerar precisão, clareza para públicos técnico e não técnico, contraste, legibilidade em celular, legendas e acessibilidade. Recomenda-se que outra pessoa revise a explicação e os resultados visuais.

## Licenças, dados e segurança

Use somente materiais e vozes cuja reutilização seja autorizada para o uso pretendido e registre origem, licença e atribuição. Pergunte antes de introduzir dependência de serviço pago. Não inclua informações pessoais, dados de terceiros ou segredos no repositório, exemplos, capturas, arquivos de apresentação, áudio, vídeo ou histórico Git. Examine os metadados e as notas antes de enviar. Se detectar uma credencial exposta, não a reproduza em uma issue: siga [SECURITY.md](SECURITY.md).

Consulte também [AGENTS.md](AGENTS.md) e [docs/CRITERIOS_ACEITACAO.md](docs/CRITERIOS_ACEITACAO.md). A participação deve seguir o [código de conduta](CODE_OF_CONDUCT.md).
