#!/usr/bin/env python3
"""Narra por frases usando Piper local e gera SRT com temporização aproximada.

pip install piper-tts; baixe o modelo pt_BR-faber-medium e seu JSON adjacente.
python scripts/gerar_piper_pronuncia.py --modelo work/vozes/pt_BR-faber-medium.onnx
"""
import argparse, json, re, subprocess, wave
from pathlib import Path
from piper import PiperVoice
from piper.config import SynthesisConfig
from gerar_legendas import ROOT, chunks, timestamp

# IPA em inglês americano inserido apenas na síntese; as legendas mantêm o texto original.
PRONUNCIA = {
 "model context protocol": "mˈɑːdəl kˈɑːntɛkst pɹˈoʊɾəkˌɑːl",
 "prompt injection": "pɹˈɑːmpt ɪndʒˈɛkʃən", "tool calling": "tˈuːl kˈɔːlɪŋ",
 "feed-forward": "fˈiːd fˈɔːɹwɚd", "fine-tuning": "fˈaɪn tˈuːnɪŋ",
 "kv cache": "kˈeɪ vˈiː kˈæʃ", "top-k": "tˈɑːp kˈeɪ", "top-p": "tˈɑːp pˈiː",
 "embeddings": "ɪmbˈɛdɪŋz", "embedding": "ɪmbˈɛdɪŋ", "query": "kwˈiəɹi",
 "keys": "kˈiːz", "key": "kˈiː", "values": "vˈæljuːz", "value": "vˈæljuː",
 "transformer": "tɹænsfˈɔːɹmɚ", "softmax": "sˈɔftmæks", "logits": "lˈɑːdʒɪts",
 "tokens": "tˈoʊkənz", "token": "tˈoʊkən", "prompts": "pɹˈɑːmpts", "prompt": "pɹˈɑːmpt",
 "skills": "skˈɪlz", "skill": "skˈɪl", "scripts": "skɹˈɪpts", "checklist": "tʃˈɛklɪst",
 "q": "kjˈuː", "k": "kˈeɪ", "v": "vˈiː", "evals": "ɪvˈælz", "checkpoints": "tʃˈɛkpɔɪnts", "rag": "ɹˈæɡ", "mcp": "ˈɛm sˈiː pˈiː"
}
PATTERN = re.compile(r"(?<![\w])(?:" + "|".join(re.escape(k) for k in sorted(PRONUNCIA,key=len,reverse=True)) + r")(?![\w])", re.IGNORECASE)
def fala_inglesa(text):
 return PATTERN.sub(lambda m: "[[" + PRONUNCIA[m.group().lower()] + "]]", text)

p=argparse.ArgumentParser(); p.add_argument('--modelo',required=True); args=p.parse_args()
voice=PiperVoice.load(args.modelo)
config=SynthesisConfig(length_scale=1.12)
out=ROOT/'output/narracao_piper_pronuncia'; out.mkdir(parents=True,exist_ok=True)
items=json.loads((ROOT/'output/narracao/roteiros_google.json').read_text(encoding='utf-8'))
subs=[]; offset=0; index=1; report=[]
for item in items:
 n=item['slide']; video=ROOT/f'output/scenes/scene_{n:02}.mp4'
 dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(video)],text=True))
 sentences=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])',item['texto'].strip())
 samples=[]; marks=[]; position=0; sample_rate=None; sample_width=2
 for sentence in sentences:
  segments=list(voice.synthesize(fala_inglesa(sentence), syn_config=config))
  if not segments: raise RuntimeError(f'Falha na cena {n}')
  for segment in segments:
   if segment.sample_channels != 1 or segment.sample_width != 2: raise RuntimeError('Formato de áudio inesperado')
   if sample_rate is None: sample_rate=segment.sample_rate
   if segment.sample_rate != sample_rate: raise RuntimeError('Frequência inconsistente')
  audio=b''.join(s.audio_int16_bytes for s in segments); count=len(audio)//2
  marks.append((position,position+count,sentence)); samples.append(audio); position+=count
  silence=round(sample_rate*.55); samples.append(bytes(silence*2)); position+=silence
 # A duração acompanha a fala e acrescenta uma curta pausa de transição.
 target=position/sample_rate+.55; target_frames=round(target*sample_rate)
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
 report.append({'cena':n,'fala_s':round(position/sample_rate-.55,3),'duracao_s':round(target_frames/sample_rate,3)})
 print(f'{n:02}: fala {position/sample_rate-.55:.1f}s, cena {target:.1f}s',flush=True)
(out/'duracoes.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(ROOT/'output/legendas/pt-BR-piper-pronuncia.srt').write_text('\n'.join(subs),encoding='utf8')
