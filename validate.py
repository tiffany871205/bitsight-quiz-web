import json
from pathlib import Path
items=json.loads((Path(__file__).parent/'questions.json').read_text())['items']
assert len(items)==400
assert len(set(q['uid'] for q in items))==len(items)
assert all(len(q['options'])==4 and len(set(q['options']))==4 and q['options'][q['correct']]==q['answer'] for q in items)
print('Bitsight: 400 valid questions')
