#!/usr/bin/env python3
"""Confere se as fontes do projeto de vídeo estão completas. Dependências: apenas stdlib."""
from pathlib import Path
from zipfile import ZipFile
import json
root=Path(__file__).resolve().parents[1]
scenes=json.loads((root/'roteiros'/'cenas.json').read_text(encoding='utf-8'))
assert len(scenes)==20, f'Esperadas 20 cenas; vieram {len(scenes)}'
assert [s['slide'] for s in scenes]==list(range(1,21)), 'Ordem de cenas incorreta'
pptx=root/'slides'/'IA_Biblioteca_20_Slides_Animados_Governanca.pptx'
assert pptx.exists(), 'PowerPoint original ausente'
with ZipFile(pptx) as z:
    slide_parts=[n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')]
    notes_parts=[n for n in z.namelist() if n.startswith('ppt/notesSlides/notesSlide') and n.endswith('.xml')]
assert len(slide_parts)==20, f'{len(slide_parts)} slides encontrados'
assert len(notes_parts)==20, f'{len(notes_parts)} notas encontradas'
for i,s in enumerate(scenes,1):
    p=root/'assets'/'gifs_referencia'/f'slide_{i:02d}.gif'
    assert p.exists() and p.stat().st_size>1024, f'GIF faltando: {p}'
    assert (root/'roteiros'/f'cena_{i:02d}.md').exists(), f'Roteiro faltando: {i}'
    assert s['presenter_notes'].strip(), f'Notas em branco: {i}'
    assert s['animation_brief'].strip(), f'Animação não descrita: {i}'
print('OK: 20 slides, 20 notas, 20 GIFs, 20 roteiros, 20 briefs de animação.')
