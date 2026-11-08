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

## Voz neural brasileira alternativa

A versão `output/IA_Biblioteca_Filme_Voz_Natural.mp4` usa a voz neural local Piper `pt_BR-faber-medium`. Seu conjunto de dados é indicado como CC0 no [model card](https://huggingface.co/rhasspy/piper-voices/blob/main/pt/pt_BR/faber/medium/MODEL_CARD); o programa Piper é GPL-3.0-or-later. Não é necessária API paga. Para reproduzir, instale `piper-tts==1.8.0`, baixe o arquivo [ONNX](https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx) e o [JSON de configuração](https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json) no mesmo diretório. Depois execute:

```bash
python scripts/gerar_narracao_piper.py --modelo work/vozes/pt_BR-faber-medium.onnx
python scripts/montar_video_piper.py
```

O primeiro comando gera WAVs e `output/legendas/pt-BR-neural.srt`; o segundo cria cópias narradas e o filme. A fala é sintetizada por frases, e a distribuição das legendas dentro de cada frase é aproximada. A voz continua sintética e deve ser avaliada por escuta humana; a sincronia com os movimentos também requer revisão. Os modelos e WAVs intermediários não são necessários para reproduzir o MP4 já gerado.

## Voz do Google, ritmo e glossário em tela

A versão `output/IA_Biblioteca_Voz_Google_Glossario.mp4` usa Google Translate TTS via `gTTS==2.5.4` com `lang=pt` e `tld=com.br`. É um serviço externo não oficial: o texto do roteiro é enviado ao Google, sua disponibilidade pode mudar e não há chave de API paga. Verifique os termos aplicáveis antes de redistribuir a voz. As falas são sintetizadas em frases completas; as animações são retimadas e cada cena termina cerca de 1,1 segundo após a fala. O glossário está em `output/glossario/termos_analogias.json` e o roteiro utilizado em `output/narracao/roteiros_google.json`. Para reproduzir, instale gTTS e FFmpeg com filtros libass e libx264 e execute:

```bash
python scripts/gerar_voz_google.py
python scripts/montar_video_google.py
```

`output/legendas/pt-BR-google.srt` é calculado por frase; dentro de cada frase os tempos são proporcionais ao texto e não são alinhamento fonético. O áudio e os vídeos de cenas intermediários são mantidos localmente e ignorados pelo Git. A sincronia fina das legendas e a pronúncia dos termos técnicos exigem revisão por escuta humana.

## Piper com transições sincronizadas

`output/IA_Biblioteca_Piper_Sincronizado.mp4` mantém a voz Piper e o glossário, com animações retimadas à duração de cada fala e cerca de 1,1 s de pausa ao final. Para gerar novamente, prepare o modelo Piper indicado acima e execute:

```bash
python scripts/gerar_piper_sincronizado.py --modelo work/vozes/pt_BR-faber-medium.onnx
python scripts/montar_piper_sincronizado.py
```

O roteiro é `output/narracao/roteiros_google.json` (texto revisado; a síntese desta versão é local, sem Google). A temporização de cada cena é proporcional à fala completa; isso não é sincronização semântica de cada animação com cada frase. As legendas `output/legendas/pt-BR-piper-sinc.srt` têm tempos aproximados dentro de cada frase e podem se sobrepor ao glossário em alguns reprodutores.

## Pronúncia de termos em inglês

A versão `output/IA_Biblioteca_Piper_Pronuncia_Ingles.mp4` usa a mesma voz Piper pt-BR, com sequências fonéticas IPA em inglês americano para termos selecionados no áudio. A grafia original é preservada nas legendas e no glossário. O dicionário e os comandos de síntese estão em `scripts/gerar_piper_pronuncia.py`; execute-o com `--modelo work/vozes/pt_BR-faber-medium.onnx`, seguido de `python scripts/montar_piper_pronuncia.py`. A voz foi treinada para português brasileiro, portanto inserir fonemas não garante sotaque nativo ou pronúncia perfeita; escuta e ajuste por pessoas continuam necessários. As legendas são aproximadas dentro de cada frase.
