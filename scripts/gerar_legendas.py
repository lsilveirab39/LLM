#!/usr/bin/env python3
"""Gera legendas temporizadas por proporção de texto; não é alinhamento fonético.

Execute após renderizar as cenas: python scripts/gerar_legendas.py
Use --fallback apenas para planejar cenas ainda não renderizadas.
"""
import argparse
import json
import re
import subprocess
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def timestamp(ms):
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    seconds, ms = divmod(ms, 1_000)
    return f'{hours:02}:{minutes:02}:{seconds:02},{ms:03}'

def duration(path, fallback):
    if not path.exists():
        if fallback is None:
            raise SystemExit(f'Cena ausente: {path}; renderize ou use --fallback SEGUNDOS')
        return fallback
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(path)], check=True, capture_output=True, text=True)
    return float(result.stdout.strip())

def chunks(text):
    # Keep a maximum of two lines of 38 characters at normal word boundaries.
    words = text.split()
    result, current = [], []
    for word in words:
        proposal = ' '.join(current + [word])
        if current and len(textwrap.wrap(proposal, width=38, break_long_words=False, break_on_hyphens=False)) > 2:
            result.append(' '.join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        result.append(' '.join(current))
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fallback', type=float, help='duração estimada para arquivos ausentes, em segundos')
    args = parser.parse_args()
    if args.fallback is not None and args.fallback <= 0:
        parser.error('--fallback deve ser positivo')
    data = json.loads((ROOT / 'output/narracao/roteiros.json').read_text(encoding='utf-8'))
    if [item['slide'] for item in data] != list(range(1, 21)):
        raise SystemExit('Roteiro deve conter exatamente as cenas 1 a 20 em ordem')
    offset, index, output = 0, 1, []
    for item in data:
        scene = ROOT / f"output/scenes/scene_{item['slide']:02}.mp4"
        ms = round(1000 * duration(scene, args.fallback))
        parts = chunks(item['texto'])
        lengths = [len(re.sub(r'\s+', '', part)) for part in parts]
        total = sum(lengths)
        elapsed = 0
        for part, length in zip(parts, lengths):
            start = round(ms * elapsed / total)
            elapsed += length
            end = round(ms * elapsed / total)
            lines = textwrap.fill(part, width=38, break_long_words=False, break_on_hyphens=False)
            output.append(f'{index}\n{timestamp(offset + start)} --> {timestamp(offset + end)}\n{lines}\n')
            index += 1
        offset += ms
    target = ROOT / 'output/legendas/pt-BR.srt'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(output), encoding='utf-8')
    print(f'{target}: {index-1} legendas, duração {timestamp(offset)}; tempos aproximados')

if __name__ == '__main__':
    main()
