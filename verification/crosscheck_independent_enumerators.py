#!/usr/bin/env python3
"""Compare all 15,195 class numbers from two independently implemented enumeration orientations."""
from pathlib import Path
from csv import DictReader
import json
root=Path(__file__).parent
with (root/'full_fundamental_discriminant_classnumbers_under_50000.csv').open() as f:
 a={int(x['q']):int(x['h']) for x in DictReader(f)}
with (root/'independent_forms_first_classnumbers.csv').open() as f:
 b={int(x['q']):int(x['h']) for x in DictReader(f)}
assert len(a)==len(b)==15195
assert a==b
res={'status':'PASS INDEPENDENT ENUMERATORS AGREE EXACTLY','discriminants_compared':len(a),'differences':0}
(root/'enum_crosscheck.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2,sort_keys=True))
