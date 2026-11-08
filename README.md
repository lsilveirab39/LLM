# IA explicada pela biblioteca

Um projeto colaborativo para explicar modelos de linguagem, agentes e governança de IA por meio de uma biblioteca imaginária. A apresentação tem **20 etapas**, na ordem do material original, com narração em português brasileiro, animações e um glossário que aproxima termos técnicos de exemplos do cotidiano.

A biblioteca é uma **analogia**, não a descrição literal do funcionamento de um LLM: o modelo não consulta automaticamente livros nem possui um acervo de respostas prontas. Buscas, ferramentas e memória externa pertencem à aplicação que pode ser construída ao redor dele.

## Comece por aqui

- [Assistir ou baixar o vídeo com voz Piper e pronúncia revisada](output/IA_Biblioteca_Piper_Pronuncia_Ingles.mp4) — versão de trabalho; veja as limitações no [relatório de QA](docs/RELATORIO_QA.md).
- [Baixar o PowerPoint original com notas](slides/IA_Biblioteca_20_Slides_Animados_Governanca.pptx) — os vídeos não estão incorporados ao arquivo.
- [Consultar o glossário: termo técnico × analogia](output/glossario/termos_analogias.md).
- [Ler o roteiro de cada etapa](roteiros/INDICE_20_CENAS.md) e as [legendas da versão Piper](output/legendas/pt-BR-piper-pronuncia.srt).
- [Ver uma amostra da pronúncia de Query, Key e Value](output/Amostra_Pronuncia_Query_Key_Value.mp4).

Arquivos grandes podem ser baixados pela página do GitHub ou após clonar o repositório. O histórico contém várias versões dos vídeos, portanto o clone pode ocupar espaço considerável.

## Como contribuir

Queremos melhorias que ajudem tanto quem está conhecendo IA quanto quem já trabalha na área: textos mais claros, analogias melhores, representações animadas que expliquem mecanismos, revisão de narração e legendas, correções do PowerPoint e verificações técnicas. Comece por [CONTRIBUTING.md](CONTRIBUTING.md) e abra uma issue para propostas ou problemas. Contribuições podem ser pequenas: corrigir uma frase, revisar uma cena ou apontar uma explicação ambígua já ajuda.

Preserve o material original e mantenha a distinção entre metáfora e mecanismo real. As 20 etapas e sua ordem são a referência do projeto; mudanças estruturais precisam ser discutidas antes. Confira os [critérios de aceitação](docs/CRITERIOS_ACEITACAO.md) e as [regras de trabalho](AGENTS.md).

## Reproduzir e validar

O projeto prioriza Python, Manim Community e FFmpeg. O procedimento de instalação, renderização e narração está em [animacoes/README.md](animacoes/README.md). Para uma verificação inicial das fontes, execute na raiz:

```bash
python scripts/validar_fontes.py
```

A qualidade de um vídeo não é comprovada apenas por sua exportação: confira precisão, legibilidade, pronúncia, sincronia e acessibilidade. A [versão atual tem limitações documentadas](docs/RELATORIO_QA.md), inclusive quanto a sincronização e revisão auditiva.

## Licença e segurança

O repositório inclui uma [licença MIT](LICENSE). **Não presuma que ela concede direitos sobre qualquer material ou serviço de terceiros**: confira a origem, as licenças e eventuais atribuições de fontes, imagens, vozes e ferramentas antes de reutilizá-los ou publicá-los. Em particular, há versões alternativas que usam serviços externos e suas condições precisam ser verificadas.

Não envie chaves de API, dados pessoais ou outros segredos em commits, issues, exemplos, arquivos de mídia ou histórico. Para relatar vulnerabilidades ou exposição acidental, siga [SECURITY.md](SECURITY.md); não publique o segredo na issue. Antes da abertura pública, confira o [checklist de publicação](docs/PUBLICACAO.md).
