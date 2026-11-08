# IA explicada pela biblioteca — produção de vídeo animado com Codex Cloud

## O que contém

- `slides/IA_Biblioteca_20_Slides_Animados_Governanca.pptx`: apresentação original e notas do apresentador.
- `assets/gifs_referencia/slide_01.gif` ... `slide_20.gif`: GIFs originais extraídos do PowerPoint, para identidade visual. Não são o vídeo final.
- `roteiros/cenas.json`: 20 cenas com objetivos visuais, textos e notas.
- `roteiros/cena_XX.md`: storyboard e explicação técnica de cada cena.
- `AGENTS.md`: regras de execução, QA e segurança para agentes do Codex.
- `PROMPT_CODEX_CLOUD.md`: prompt completo para iniciar uma tarefa no Codex Cloud.
- `docs/CRITERIOS_ACEITACAO.md`: critérios mínimos para aprovar a entrega.
- `scripts/validar_fontes.py`: verifica fontes, cenas e GIFs antes do desenvolvimento.

## Fluxo de uso no GitHub + Codex Cloud

1. Crie um repositório privado no GitHub, por exemplo `ia-biblioteca-animada`.
2. Extraia este ZIP e envie **o conteúdo da pasta raiz `IA_Biblioteca_Codex_Cloud`** para a raiz do repositório.
3. Acesse o Codex Cloud no navegador do celular: https://chatgpt.com/codex . Conecte o repositório e selecione o ambiente.
4. Cole o conteúdo de `PROMPT_CODEX_CLOUD.md` como a primeira tarefa.
5. Revise o plano proposto, os primeiros 2 protótipos e os vídeos exportados. Use o fluxo de revisão/PR do GitHub.

## Saídas esperadas do trabalho do Codex

- `output/scenes/scene_01.mp4` ... `scene_20.mp4`: cenas individuais (1920x1080; H.264; sem marca d'água).
- `output/IA_Biblioteca_Filme_Completo.mp4`: filme compilado, com títulos e transições.
- `output/legendas/pt-BR.srt` e roteiros de narração em `output/narracao/`.
- `output/IA_Biblioteca_Video_Slides.pptx`, quando a incorporação de MP4 for viável e puder ser validada.
- `docs/RELATORIO_QA.md`: testes, limitações e evidências de revisão.

## Tecnologias preferenciais e custo

**Prioridade zero custo de licença:** Manim Community (open source), Python, FFmpeg, Pillow e `python-pptx`, conforme licenças e disponibilidade no ambiente. O Manim MCP é opcional e não deve ser necessário para executar a renderização; em ambientes sem suporte a MCP, usar a CLI do Manim diretamente. Remotion só se a licença aplicável permitir e após justificar uso. Evitar serviços pagos de vídeo, voz e geração de imagem sem autorização explícita.

O Codex Cloud pode ter limites de tempo, CPU, memória, armazenamento e instalação. Caso a renderização completa não seja viável no ambiente, gerar código de projeto reproduzível, roteiro e um protótipo local, e documentar o comando exato para renderizar fora dele. Não afirmar que produziu 20 MP4s sem arquivos existentes.

## Princípios didáticos

A biblioteca é a **analogia**. LLM não consulta literalmente livros em cada resposta; Query/Key/Value são vetores, não consultas reais; tokens podem representar partes de palavras; RAG e ferramentas são componentes **externos** ao mecanismo interno do Transformer; o término de uma resposta não ocorre porque a probabilidade chegou a zero.
