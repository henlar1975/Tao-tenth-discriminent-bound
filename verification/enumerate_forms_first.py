#!/usr/bin/env python3
"""Enumerator B: independently generate all primitive reduced forms by (a,b,c), grouping by discriminant.
No reuse of enumeration A's form-generation logic or outputs except final comparison.
"""
from math import gcd, isqrt
from collections import defaultdict
from pathlib import Path
import json,hashlib
L=50000

# Independent squarefreeness classification by trial division of each negative field parameter.
def sqfree(n):
    p=2
    while p*p<=n:
        if n%(p*p)==0:return False
        p+=1
    return True

def fund(q):
    n=-q
    if n%4==1: return sqfree(q)
    return q%4==0 and n//4%4 in (2,3) and sqfree(q//4)

# For each reduced a,b, enumerate compatible c (rather than enumerating q).
counts=defaultdict(int)
for a in range(1,isqrt((L-1)//3)+1):
    for b in range(-a,a+1):
        if b<0 and abs(b)==a:continue
        cmax=((L-1)+b*b)//(4*a)
        for c in range(a,cmax+1):
            if b<0 and a==c:continue
            if gcd(a,gcd(abs(b),c))>1:continue
            q=4*a*c-b*b
            if q<3 or q>=L:continue
            if fund(q):counts[q]+=1

funds={q for q in range(3,L) if fund(q)}
assert set(counts)==funds
assert len(funds)==15195
ones=sorted(k for k,v in counts.items() if v==1)
assert ones == [3,4,7,8,11,19,43,67,163]
root=Path(__file__).parent
lines='h,q\n'+''.join(f'{counts[q]},{q}\n' for q in sorted(counts))
(root/'independent_forms_first_classnumbers.csv').write_text(lines)
res={'method':'forms-first','fundamental_discriminants':len(counts),
'class_number_one_absolute_fundamental_discriminants':ones,
'counts_sha256':hashlib.sha256(lines.encode()).hexdigest(),
'passed':True}
(root/'enum_forms_first.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2,sort_keys=True))
