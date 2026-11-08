# Renderização das animações

O código em `prototipos.py` contém vinte cenas Manim Community e usa um personagem vetorial original compartilhado. São estudos de produção: a maioria apresenta fluxos simplificados de cartões; ainda requer revisão visual e didática individual e aprimoramento conforme os briefs antes de ser considerada versão final. As cenas são mudas: roteiros e legendas são produzidos separadamente.

Requisitos: Python 3.10 ou mais recente, Manim Community, FFmpeg e ffprobe. Instale Manim conforme a documentação oficial para seu sistema, incluindo as bibliotecas de desenvolvimento Cairo e Pango. No ambiente de desenvolvimento, testou-se Manim Community 0.22.1. Para um ambiente virtual existente:

```bash
python -m pip install 'manim==0.22.1'
python scripts/validar_fontes.py
python scripts/renderizar_manim.py 3 17
python scripts/renderizar_manim.py
python scripts/renderizar_manim.py --concatenar
python scripts/qa_videos.py
```

O renderizador usa 1920×1080, 30 fps e gera H.264 no diretório `output/scenes/`. `--concatenar` renderiza as cenas solicitadas (ou todas, se não especificadas) e somente monta o filme se todos os 20 arquivos existirem. Um arquivo gerado não comprova qualidade didática nem sincronia da narração. Revise cada cena, adicione áudio autorizado e sincronize legendas antes da entrega. Uma instalação pode exigir `--manim /caminho/para/manim`; a concatenação usa `ffmpeg` no PATH. O código não requer serviços pagos ou Manim MCP.

## Narração local e montagem com áudio

Após renderizar as 20 cenas, instale `espeak-ng` e execute `python scripts/gerar_narracao.py`. O script verifica as durações via ffprobe e produz WAVs e `output/legendas/pt-BR-alinhado.srt` com marcações dos trechos efetivamente sintetizados. Ouça e revise a voz e o sincronismo com a animação. Depois, `python scripts/inserir_narracao.py` gera cópias em `output/scenes_narradas/` e concatena essas cópias em `output/IA_Biblioteca_Filme_Completo.mp4`. Para um executável fora do PATH, informe `--espeak /caminho/para/espeak-ng`. O script de narração usa 50 s para cenas ausentes por padrão; não considere o resultado final até todas existirem e a narração ser gerada novamente.
