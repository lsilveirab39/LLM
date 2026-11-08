#!/usr/bin/env python3
"""Verifica os MP4s presentes e extrai quadros para revisão visual humana.

Exemplo: python scripts/qa_videos.py
O JSON registra ausência e falhas; a existência de quadros não implica aprovação visual.
"""
import json
from fractions import Fraction
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output'
EVIDENCE = OUTPUT / 'qa' / 'quadros'


def examine(path, extract=False):
    if not path.is_file():
        return {'arquivo': str(path.relative_to(ROOT)), 'status': 'ausente'}
    cmd = ['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)]
    try:
        data = json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)
        video = next(s for s in data['streams'] if s['codec_type'] == 'video')
        duration = float(data['format']['duration'])
        result = {'arquivo': str(path.relative_to(ROOT)), 'codec': video.get('codec_name'),
                  'largura': video.get('width'), 'altura': video.get('height'),
                  'fps': video.get('avg_frame_rate'), 'duracao_s': round(duration, 3),
                  'audio': any(s['codec_type'] == 'audio' for s in data['streams'])}
        result['fps_numerico'] = float(Fraction(result['fps']))
        result['status'] = 'ok' if (result['codec'], result['largura'], result['altura']) == ('h264', 1920, 1080) and duration > 0 and result['fps_numerico'] > 0 else 'falha'
        if extract:
            result['duracao_na_faixa_40_60_s'] = 40 <= duration <= 60
        if extract:
            EVIDENCE.mkdir(parents=True, exist_ok=True)
            frame = EVIDENCE / (path.stem + '.png')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(duration / 2), '-i', str(path), '-frames:v', '1', str(frame)], check=True, capture_output=True)
            result['quadro_medio'] = str(frame.relative_to(ROOT))
            result['revisao_visual'] = 'pendente'
        return result
    except (subprocess.CalledProcessError, ValueError, KeyError, StopIteration, ZeroDivisionError, json.JSONDecodeError) as exc:
        return {'arquivo': str(path.relative_to(ROOT)), 'status': 'falha', 'erro': str(exc)}


def main():
    results = [examine(OUTPUT / 'scenes' / f'scene_{i:02}.mp4', True) for i in range(1, 21)]
    results.append(examine(OUTPUT / 'IA_Biblioteca_Filme_Completo.mp4'))
    report = OUTPUT / 'qa' / 'verificacao_tecnica.json'
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{report.relative_to(ROOT)}: {sum(x["status"] == "ok" for x in results)}/{len(results)} arquivos válidos')
    return 0 if all(x['status'] == 'ok' for x in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
