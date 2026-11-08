#!/usr/bin/env python3
"""Narra por frases usando Piper local e gera SRT com temporização aproximada.

pip install piper-tts; baixe o modelo pt_BR-faber-medium e seu JSON adjacente.
python scripts/gerar_narracao_piper.py --modelo work/vozes/pt_BR-faber-medium.onnx
"""
import argparse, json, re, subprocess, wave
from pathlib import Path
from piper import PiperVoice
from piper.config import SynthesisConfig
from gerar_legendas import ROOT, chunks, timestamp

p=argparse.ArgumentParser(); p.add_argument('--modelo',required=True); args=p.parse_args()
voice=PiperVoice.load(args.modelo)
config=SynthesisConfig(length_scale=1.12)
out=ROOT/'output/narracao_neural'; out.mkdir(parents=True,exist_ok=True)
items=json.loads((ROOT/'output/narracao/roteiros.json').read_text(encoding='utf-8'))
subs=[]; offset=0; index=1; report=[]
for item in items:
 n=item['slide']; video=ROOT/f'output/scenes/scene_{n:02}.mp4'
 dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(video)],text=True))
 sentences=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])',item['texto'].strip())
 samples=[]; marks=[]; position=0; sample_rate=None; sample_width=2
 for sentence in sentences:
  segments=list(voice.synthesize(sentence, syn_config=config))
  if not segments: raise RuntimeError(f'Falha na cena {n}')
  for segment in segments:
   if segment.sample_channels != 1 or segment.sample_width != 2: raise RuntimeError('Formato de áudio inesperado')
   if sample_rate is None: sample_rate=segment.sample_rate
   if segment.sample_rate != sample_rate: raise RuntimeError('Frequência inconsistente')
  audio=b''.join(s.audio_int16_bytes for s in segments); count=len(audio)//2
  marks.append((position,position+count,sentence)); samples.append(audio); position+=count
  silence=round(sample_rate*.55); samples.append(bytes(silence*2)); position+=silence
 # Keep visual pacing, extending the final frame only if narration exceeds the video.
 target=max(dur,position/sample_rate+.3); target_frames=round(target*sample_rate)
 with wave.open(str(out/f'cena_{n:02}.wav'),'wb') as f:
  f.setnchannels(1); f.setsampwidth(2); f.setframerate(sample_rate)
  for b in samples: f.writeframes(b)
  f.writeframes(bytes((target_frames-position)*2))
 for start,end,sentence in marks:
  pieces=chunks(sentence); lengths=[len(re.sub(r'\s+','',x)) for x in pieces]; total=sum(lengths); acc=0
  for piece,length in zip(pieces,lengths):
   a=offset+round(1000*(start+(end-start)*acc/total)/sample_rate); acc+=length
   b=offset+round(1000*(start+(end-start)*acc/total)/sample_rate)
   import textwrap
   subs.append(f'{index}\n{timestamp(a)} --> {timestamp(b)}\n{textwrap.fill(piece,38,break_long_words=False,break_on_hyphens=False)}\n'); index+=1
 offset+=round(target_frames*1000/sample_rate)
 report.append({'cena':n,'fala_segundos':round(position/sample_rate,3),'video_original_segundos':dur,'duracao_saida_segundos':round(target_frames/sample_rate,3)})
 print(f'{n:02}: fala {position/sample_rate:.1f}s, cena {dur:.1f}s',flush=True)
(out/'duracoes.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(ROOT/'output/legendas/pt-BR-neural.srt').write_text('\n'.join(subs),encoding='utf8')
