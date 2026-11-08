# Checklist antes de tornar o repositório público

Esta lista não substitui a revisão dos responsáveis. A mudança de visibilidade publica conteúdo, histórico e metadados, não apenas o último estado dos arquivos. Qualquer pessoa poderá baixar e manter cópias.

- [ ] Revisar histórico Git, nomes e e-mails de autores e responsáveis. Usar endereços GitHub `noreply` quando houver expectativa de privacidade; substituir dados no histórico exige coordenar clones e referências existentes.
- [ ] Rodar um detector de segredos no histórico completo e nos arquivos disponíveis; revisar apresentações, notas, metadados, imagens, áudio, vídeos e outros anexos. Revogar qualquer credencial efetivamente exposta antes de remover referências.
- [ ] Confirmar os direitos de distribuição do PowerPoint, GIFs, fontes, vozes, modelos e quaisquer materiais de terceiros. Em particular, avaliar as condições do serviço Google Translate TTS usado na versão alternativa e a procedência e licença dos materiais originais; a licença MIT do repositório não comprova direitos de terceiros.
- [ ] Configurar um canal privado de segurança e habilitar o reporte privado de vulnerabilidades no GitHub, se disponível.
- [ ] Revisar os resultados de QA, as limitações de narração e acessibilidade e a clareza do material para públicos diversos.
- [ ] Verificar branches, tags, releases, anexos, issues, pull requests, Actions e demais dados existentes no GitHub: o histórico da branch principal não é a única possível fonte de exposição.

## Auditoria inicial desta preparação

A varredura automatizada dos oito commits então presentes com Gitleaks 8.24.3 e do conteúdo textual disponível com detect-secrets não apontou credenciais conhecidas. Os arquivos internos do PowerPoint foram varridos separadamente, sem detecção de segredos, e foi examinada a lista de metadados de arquivos de vídeo locais. Esses testes não garantem ausência de segredos, informação pessoal, imagens sensíveis ou material de terceiros. Foi identificado um endereço pessoal em metadados de commits anteriores; ele deve ser revisto antes da publicação. A auditoria não garante a revisão integral de áudio e vídeo, conteúdo oculto ou todos os dados hospedados no GitHub.
