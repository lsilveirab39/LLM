#!/usr/bin/env python3
"""Renderiza cenas Manim selecionadas e, opcionalmente, concatena as 20.

As cenas geradas são mudas; narração e legendas são etapas separadas.
"""
import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args):
    print('+', ' '.join(map(str, args)), flush=True)
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('cenas', nargs='*', type=int, help='números de 1 a 20; padrão: todas')
    p.add_argument('--manim', default='manim', help='caminho para executável Manim')
    p.add_argument('--concatenar', action='store_true', help='concatena somente se todas as cenas existirem')
    args = p.parse_args()
    scenes = args.cenas or list(range(1, 21))
    if any(n < 1 or n > 20 for n in scenes): p.error('cenas devem estar entre 1 e 20')
    output = ROOT / 'output' / 'scenes'
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='biblioteca-manim-') as tmp:
        for n in scenes:
            name = f'Cena{n:02}'
            run([args.manim, '-qh', '--fps', '30', '--disable_caching', '--media_dir', tmp,
                 'animacoes/prototipos.py', name])
            result = Path(tmp) / 'videos' / 'prototipos' / '1080p30' / f'{name}.mp4'
            if not result.is_file(): raise FileNotFoundError(result)
            shutil.copyfile(result, output / f'scene_{n:02}.mp4')
    if args.concatenar:
        paths = [output / f'scene_{n:02}.mp4' for n in range(1, 21)]
        missing = [str(x) for x in paths if not x.is_file()]
        if missing: raise FileNotFoundError('Faltam cenas: ' + ', '.join(missing))
        with tempfile.TemporaryDirectory(prefix='biblioteca-concat-') as tmp:
            listing = Path(tmp) / 'concat.txt'
            # Caminhos produzidos pelo projeto; escape de aspas para o demuxer concat.
            listing.write_text(''.join("file '" + str(x).replace("'", "'\\''") + "'\n" for x in paths), encoding='utf-8')
            run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(listing), '-c', 'copy',
                 str(ROOT / 'output' / 'IA_Biblioteca_Filme_Completo.mp4')])

if __name__ == '__main__': main()
