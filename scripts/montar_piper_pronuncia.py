#!/usr/bin/env python3
"""Ajusta o ritmo visual à narração Piper e sobrepõe glossário por cena."""
import json,subprocess,tempfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
audio=ROOT/'output/narracao_piper_pronuncia';target=ROOT/'output/scenes_piper_pronuncia';target.mkdir(parents=True,exist_ok=True)
rows=json.loads((audio/'duracoes.json').read_text(encoding='utf8'))
terms=json.loads((ROOT/'output/glossario/termos_analogias.json').read_text(encoding='utf8'))
assert [r['cena'] for r in rows]==list(range(1,21)) and len(terms)==20

def stamp(t):
 t=round(t*100);h,t=divmod(t,360000);m,t=divmod(t,6000);s,c=divmod(t,100);return f'{h}:{m:02}:{s:02}.{c:02}'
def render(row):
 n=row['cena'];d=row['duracao_s'];src=ROOT/f'output/scenes/scene_{n:02}.mp4';wav=audio/f'cena_{n:02}.wav'
 original=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(src)],text=True))
 with tempfile.TemporaryDirectory(prefix=f'piper-{n:02}-') as tmp:
  ass=Path(tmp)/'glossario.ass'
  header='''[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\nWrapStyle: 0\nScaledBorderAndShadow: yes\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Glossario,DejaVu Sans,35,&H00FFFFFF,&H00FFFFFF,&H00322219,&H00322219,0,0,0,0,100,100,0,0,3,12,0,2,80,80,38,1\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'''
  lines=[];entries=terms[n-1];span=(d-.6)/len(entries)
  for i,entry in enumerate(entries):
   clean=entry.replace('\\','/').replace('{','(').replace('}',')')
   lines.append(f'Dialogue: 0,{stamp(.2+i*span)},{stamp(.2+(i+1)*span)},Glossario,,0,0,0,,{clean}\n')
  ass.write_text(header+''.join(lines),encoding='utf8')
  filters=f'setpts=PTS*{d/original:.9f},fps=30,subtitles={ass}'
  subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(src),'-i',str(wav),'-vf',filters,'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','veryfast','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest',str(target/f'scene_{n:02}.mp4')],check=True)
 print(f'{n:02}: concluída',flush=True)
with ThreadPoolExecutor(max_workers=2) as pool: list(pool.map(render,rows))
with tempfile.TemporaryDirectory(prefix='piper-concat-') as tmp:
 listing=Path(tmp)/'concat.txt';listing.write_text(''.join("file '"+str(target/f'scene_{n:02}.mp4').replace("'","'\\''")+"'\n" for n in range(1,21)),encoding='utf8')
 subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(ROOT/'output/IA_Biblioteca_Piper_Pronuncia_Ingles.mp4')],check=True)
# Ajusta inícios globais à duração real quantizada dos MP4s concatenados.
import bisect,re
srt=ROOT/'output/legendas/pt-BR-piper-pronuncia.srt'; content=srt.read_text(encoding='utf8')
nominal=[0]; actual=[0]
for row in rows:
 nominal.append(nominal[-1]+round(row['duracao_s']*1000))
 path=target/f"scene_{row['cena']:02}.mp4"
 seconds=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(path)],text=True))
 actual.append(actual[-1]+round(seconds*1000))
pattern=re.compile(r'(\d\d):(\d\d):(\d\d),(\d{3}) --> (\d\d):(\d\d):(\d\d),(\d{3})')
def to_ms(v):return (((int(v[0])*60+int(v[1]))*60+int(v[2]))*1000+int(v[3]))
def format_ms(v):
 h,v=divmod(v,3600000);m,v=divmod(v,60000);s,v=divmod(v,1000);return f'{h:02}:{m:02}:{s:02},{v:03}'
def correct(match):
 values=match.groups();start=to_ms(values[:4]);end=to_ms(values[4:]);index=min(19,bisect.bisect_right(nominal,start)-1)
 shift=actual[index]-nominal[index]
 return f'{format_ms(start+shift)} --> {format_ms(end+shift)}'
srt.write_text(pattern.sub(correct,content),encoding='utf8')
