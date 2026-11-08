#!/usr/bin/env python3
"""Combina vídeos originais mudos com os WAVs Piper e monta o filme completo."""
import json, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
audio=ROOT/'output/narracao_neural'; target=ROOT/'output/scenes_narradas_neural'; target.mkdir(parents=True,exist_ok=True)
info=json.loads((audio/'duracoes.json').read_text(encoding='utf8'))
if [a['cena'] for a in info] != list(range(1,21)): raise SystemExit('São necessárias as 20 cenas em ordem.')
for row in info:
 n=row['cena']; source=ROOT/f'output/scenes/scene_{n:02}.mp4'; wav=audio/f'cena_{n:02}.wav'
 delta=row['duracao_saida_segundos']-row['video_original_segundos']
 command=['ffmpeg','-y','-loglevel','error','-i',str(source),'-i',str(wav),'-map','0:v:0','-map','1:a:0']
 if delta>0.02:
  command+=['-vf',f'tpad=stop_mode=clone:stop_duration={delta:.3f}','-c:v','libx264','-preset','medium','-pix_fmt','yuv420p']
 else: command+=['-c:v','copy']
 command+=['-c:a','aac','-b:a','160k','-shortest',str(target/f'scene_{n:02}.mp4')]
 subprocess.run(command,check=True)
 print(f'{n:02} concluída',flush=True)
with tempfile.TemporaryDirectory(prefix='piper-concat-') as tmp:
 listing=Path(tmp)/'lista.txt'; listing.write_text(''.join("file '"+str(target/f'scene_{n:02}.mp4').replace("'","'\\''")+"'\n" for n in range(1,21)),encoding='utf8')
 subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(ROOT/'output/IA_Biblioteca_Filme_Voz_Natural.mp4')],check=True)
