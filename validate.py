import json
from pathlib import Path
items=json.loads((Path(__file__).parent/'questions.json').read_text())['items']
assert len(items)==400
assert len(set(q['uid'] for q in items))==len(items)
assert all(len(q['options'])==4 and len(set(q['options']))==4 and q['options'][q['correct']]==q['answer'] for q in items)
curated=[q for q in items if q.get('quality_review','').startswith('干擾選項已')]
assert len(curated)==400, f'expected 400 curated items, got {len(curated)}'
assert all(q['answer'] in q['options'] for q in curated)
assert len(set(q['question'] for q in items))==len(items)
assert all(q.get('explanation') and q.get('source_status') for q in items)
print('Bitsight: 400 valid questions')
print(f'Curated option sets: {len(curated)}; unreviewed: {len(items)-len(curated)}')
