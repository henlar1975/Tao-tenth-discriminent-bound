#!/usr/bin/env python3
"""Enumerator A: loop over negative fundamental discriminants, count reduced primitive forms.
Does not use Heegner theorem, class number tables or number-theory software.
"""
from math import isqrt,gcd
from pathlib import Path
import json,hashlib
LIMIT=50000
sqf=[True]*LIMIT
sqf[0]=False
for j in range(2,isqrt(LIMIT-1)+1):
    for k in range(j*j,LIMIT,j*j):
        sqf[k]=False

def is_fundamental(q):
    D=-q
    return (D%4==1 and sqf[q]) or (D%4==0 and D//4%4 in (2,3) and sqf[q//4])

def reduced_forms(q):
    for a in range(1,isqrt(q//3)+1):
        for b in range(-a,a+1):
            if (q+b*b)%(4*a):continue
            c=(q+b*b)//(4*a)
            if a>c or (b<0 and (abs(b)==a or a==c)):continue
            if gcd(gcd(a,abs(b)),c)!=1:continue
            yield (a,b,c)

counts={}
for q in range(3,LIMIT):
    if is_fundamental(q):counts[q]=len(list(reduced_forms(q)))
zero=[q for q,c in counts.items() if c==1]
assert zero==[3,4,7,8,11,19,43,67,163], zero
assert all(c>=1 for c in counts.values())
assert len(counts)==15195,len(counts)
sorted_lines=''.join(f'{k},{v}\n' for k,v in sorted(counts.items()))
root=Path(__file__).parent
(root/'full_fundamental_discriminant_classnumbers_under_50000.csv').write_text('q,h\n'+sorted_lines)
res={'method':'fundamental-discriminant-first','fundamental_discriminants':len(counts),'range':'3 <= |D| < 50000',
'class_number_one_absolute_fundamental_discriminants':zero,
'max_class_number':max(counts.values()),
'csv_sha256':hashlib.sha256((root/'full_fundamental_discriminant_classnumbers_under_50000.csv').read_bytes()).hexdigest(),
'passed':True}
(root/'enum_discriminants_first.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2,sort_keys=True))
