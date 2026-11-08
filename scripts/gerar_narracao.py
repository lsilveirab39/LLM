#!/usr/bin/env python3
"""Sintetiza trechos pt-BR com eSpeak NG e gera legendas alinhadas ao áudio.

Instale espeak-ng e ffprobe. Execute: python scripts/gerar_narracao.py
Se necessário, configure --espeak, LD_LIBRARY_PATH e ESPEAK_DATA_PATH.
As cenas ausentes são consideradas de 50 segundos. A saída alinhada é separada
até que o vídeo final esteja pronto e sua duração seja validada.
"""
import argparse
import json
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path
from gerar_legendas import chunks, duration, timestamp, ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--espeak', default='espeak-ng')
    parser.add_argument('--rate', type=int, default=165, help='palavras por minuto do eSpeak')
    parser.add_argument('--fallback', type=float, default=50.0, help='duração para cenas ausentes')
    parser.add_argument('--gap', type=float, default=0.18, help='pausa entre trechos')
    args = parser.parse_args()
    if args.rate <= 0 or args.fallback <= 0 or args.gap < 0:
        parser.error('taxa e duração devem ser positivas e pausa não negativa')
    if not (Path(args.espeak).is_file() or shutil.which(args.espeak)):
        raise SystemExit('eSpeak NG não encontrado; instale-o ou informe --espeak')
    roteiro = json.loads((ROOT / 'output/narracao/roteiros.json').read_text(encoding='utf-8'))
    if [item['slide'] for item in roteiro] != list(range(1, 21)):
        raise SystemExit('Esperadas 20 cenas em ordem')
    outdir = ROOT / 'output/narracao/audio'
    outdir.mkdir(parents=True, exist_ok=True)
    subtitles, offset, idx = [], 0, 1
    scene_info = []
    with tempfile.TemporaryDirectory(prefix='narracao-') as tmp:
        for item in roteiro:
            scene = item['slide']
            target_secs = duration(ROOT / f'output/scenes/scene_{scene:02}.mp4', args.fallback)
            audio_parts, markers = [], []
            params, frames = None, 0
            for n, part in enumerate(chunks(item['texto'])):
                wav = Path(tmp) / f'{scene:02}_{n:02}.wav'
                subprocess.run([args.espeak, '-v', 'pt-br', '-s', str(args.rate), '-w', str(wav), part], check=True, capture_output=True)
                with wave.open(str(wav), 'rb') as source:
                    this = (source.getnchannels(), source.getsampwidth(), source.getframerate(), source.getcomptype())
                    if params is None:
                        params = this
                    if this != params or source.getcomptype() != 'NONE':
                        raise RuntimeError('Formato WAV inconsistente')
                    data = source.readframes(source.getnframes())
                    count = len(data) // (params[0] * params[1])
                start = frames
                frames += count
                markers.append((start, frames, part))
                audio_parts.append(data)
                gap_frames = round(args.gap * params[2])
                audio_parts.append(bytes(gap_frames * params[0] * params[1]))
                frames += gap_frames
            target_frames = round(target_secs * params[2])
            if frames > target_frames:
                raise SystemExit(f'Cena {scene:02}: áudio {frames/params[2]:.2f}s excede {target_secs:.2f}s; aumente duração ou taxa.')
            wav_out = outdir / f'cena_{scene:02}.wav'
            with wave.open(str(wav_out), 'wb') as dest:
                dest.setnchannels(params[0]); dest.setsampwidth(params[1]); dest.setframerate(params[2])
                for data in audio_parts:
                    dest.writeframes(data)
                dest.writeframes(bytes((target_frames - frames) * params[0] * params[1]))
            import textwrap
            for start, end, part in markers:
                start_ms = offset + round(start * 1000 / params[2])
                end_ms = offset + round(end * 1000 / params[2])
                lines = textwrap.fill(part, 38, break_long_words=False, break_on_hyphens=False)
                subtitles.append(f'{idx}\n{timestamp(start_ms)} --> {timestamp(end_ms)}\n{lines}\n')
                idx += 1
            offset += round(target_frames * 1000 / params[2])
            scene_info.append({'slide': scene, 'duracao_audio_falado_com_pausas_s': round(frames/params[2], 3), 'duracao_cena_s': target_secs})
            print(f'{scene:02}: fala {frames/params[2]:.1f}s / cena {target_secs:.1f}s', flush=True)
    (ROOT / 'output/narracao/duracoes.json').write_text(json.dumps(scene_info, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (ROOT / 'output/legendas/pt-BR-alinhado.srt').write_text('\n'.join(subtitles), encoding='utf-8')
    print(f'{idx-1} legendas alinhadas por trecho; total {timestamp(offset)}')

if __name__ == '__main__':
    main()
