#!/usr/bin/env python3
"""Sintetiza frases com Google Translate TTS (gTTS) e prepara legendas.

O serviço é externo; o texto é enviado ao Google. A API não oficial pode falhar
ou mudar. Instale gTTS e FFmpeg antes de executar. Nunca exige credenciais pagas.
"""
import io,json,re,subprocess,wave,textwrap,time
from pathlib import Path
from gtts import gTTS
from gerar_legendas import ROOT,chunks,timestamp

items=json.loads((ROOT/'output/narracao/roteiros_google.json').read_text(encoding='utf8'))
terms=json.loads((ROOT/'output/glossario/termos_analogias.json').read_text(encoding='utf8'))
out=ROOT/'output/narracao_google';out.mkdir(parents=True,exist_ok=True)
cache=ROOT/'work/voz_google';cache.mkdir(parents=True,exist_ok=True)
subs=[];offset=0;idx=1;results=[];rate=24000
for item in items:
 n=item['slide']; sentences=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])',item['texto'].strip())
 pcm=[]; markers=[]; pos=0
 for j,sentence in enumerate(sentences):
  mp3=cache/f'{n:02}_{j:02}.mp3'
  if not mp3.exists():
   for attempt in range(3):
    try:
     gTTS(sentence,lang='pt',tld='com.br').save(str(mp3));break
    except Exception:
     mp3.unlink(missing_ok=True)
     if attempt==2: raise
     time.sleep(2*(attempt+1))
  data=subprocess.check_output(['ffmpeg','-v','error','-i',str(mp3),'-f','s16le','-ac','1','-ar',str(rate),'-'])
  num=len(data)//2;markers.append((pos,pos+num,sentence));pcm.append(data);pos+=num
  gap=round(.32*rate);pcm.append(bytes(gap*2));pos+=gap
 # 0.32 s ending pause + 0.80 s tail, rather than a long static wait.
 tail=round(.80*rate);pcm.append(bytes(tail*2));duration=(pos+tail)/rate
 with wave.open(str(out/f'cena_{n:02}.wav'),'wb') as w:
  w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate)
  for data in pcm:w.writeframes(data)
 for start,end,sentence in markers:
  pieces=chunks(sentence); lengths=[len(re.sub(r'\s+','',x)) for x in pieces];total=sum(lengths);acc=0
  for piece,length in zip(pieces,lengths):
   a=offset+round(1000*(start+(end-start)*acc/total)/rate);acc+=length
   b=offset+round(1000*(start+(end-start)*acc/total)/rate)
   subs.append(f'{idx}\n{timestamp(a)} --> {timestamp(b)}\n{textwrap.fill(piece,38,break_long_words=False,break_on_hyphens=False)}\n');idx+=1
 offset+=round(duration*1000)
 results.append({'cena':n,'fala_s':round((pos-gap)/rate,3),'duracao_s':round(duration,3)})
 print(f'{n:02}: fala {(pos-gap)/rate:.1f}s, cena {duration:.1f}s',flush=True)
(out/'duracoes.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(ROOT/'output/legendas/pt-BR-google.srt').write_text('\n'.join(subs),encoding='utf8')
