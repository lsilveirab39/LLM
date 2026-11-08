#!/usr/bin/env python3
"""Adiciona os WAVs gerados às cenas e preserva as versões mudas.

Execute depois de renderizar todas as cenas e gerar narração com duração real.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'output/scenes'
target = ROOT / 'output/scenes_narradas'
target.mkdir(parents=True, exist_ok=True)
for n in range(1, 21):
    video = source / f'scene_{n:02}.mp4'
    audio = ROOT / f'output/narracao/audio/cena_{n:02}.wav'
    if not video.exists() or not audio.exists():
        raise SystemExit(f'Faltam vídeo ou áudio para cena {n:02}')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(video), '-i', str(audio),
                    '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy', '-c:a', 'aac',
                    '-b:a', '160k', '-shortest', str(target / video.name)], check=True)

# Concatena apenas depois que todas as cenas narradas estiverem prontas.
import tempfile
with tempfile.TemporaryDirectory(prefix='biblioteca-narrada-') as tmp:
    listing = Path(tmp) / 'concat.txt'
    listing.write_text(''.join("file '" + str(target / f'scene_{n:02}.mp4').replace("'", "'\\''") + "'\n" for n in range(1, 21)), encoding='utf-8')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(listing),
                    '-c', 'copy', str(ROOT / 'output/IA_Biblioteca_Filme_Completo.mp4')], check=True)
