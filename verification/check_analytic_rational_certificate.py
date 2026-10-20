#!/usr/bin/env python3
"""Exact rational inequalities for the independently derived zero-gap -> class-number bridge.
Uses Fraction only, no floating arithmetic for proof certificates.
This does NOT verify Banks or Lu-Zaman-Zhao analytic theorems.
"""
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path

def partial_exp(x, n):
    return sum((x**k/Q(factorial(k)) for k in range(n+1)), Q(0))

# For x=3/5, e^x <= sum_{k=0}^4 x^k/k! + (x^5/5!)/(1-x/6), since the tail has ratio <= x/6.
x=Q(3,5)
exp_upper = partial_exp(x,4)+(x**5/Q(factorial(5)))/(1-x/6)
assert exp_upper == Q(45553,25000)
assert exp_upper < Q(183,100)
# Consequently e^{-3/5} > 100/183.

# e^10 > 22000 from positive Taylor terms through k=22;
# e^(83/100) > 25/11 from terms through k=4;
# hence e^(1083/100)>50000.
ex10_lower = partial_exp(Q(10),22)
ex083_lower = partial_exp(Q(83,100),4)
assert ex10_lower > 22000
assert ex083_lower > Q(25,11)
assert ex10_lower*ex083_lower>50000
# hence log 50000 < 1083/100

# e^(12/5)>10 from degree-8 partial Taylor sum; hence log(10^10)<24.
assert partial_exp(Q(12,5),8)>10

# 50 squares have more than 13/8 of the weighted mass in sigma <= 1.
squares_mass=sum((Q(1,j*j) for j in range(1,51)), Q(0))
assert squares_mass > Q(13,8)
assert Q(447,2)**2 < 50000

# Small-conductor regime (50000 <= q <= 10^10), gap c=1/5 from LZZ as cited by Banks.
low_small=Q(1,5)*(Q(13,8)*Q(100,183)*Q(447,2)-28)/(Q(22,7)*Q(1083,100))
assert low_small==Q(1455755,1453386)
assert low_small>1

# Large-conductor regime (q >= 10^10), gap c=3/1000 from Banks.
# exp(-9/1000) > 1-9/1000 = 991/1000.
low_large=Q(3,1000)*(Q(13,8)*Q(991,1000)*100000-28)/(Q(22,7)*24)
assert low_large==Q(2254133,352000)
assert low_large>1

out={
 'status':'PASS EXACT RATIONAL CHECKS',
 'dependency':'Banks 2610.15483 explicit gap q>=10^10; Lu-Zaman-Zhao numerical gap q<=10^10 as quoted in Banks; neither reverified here',
 'q_cutoff':50000,
 'class_number_one_excluded_for_q_ge_cutoff':True,
 'square_mass_50_gt_13_over_8':True,
 'exp_three_fifths_upper_fraction':str(exp_upper),
 'taylor_exp10_lower_gt_22000':True,
 'taylor_exp083_lower_gt_25_over_11':True,
 'log_50000_upper':'1083/100',
 'small_regime_h_strict_lower_fraction':str(low_small),
 'large_regime_h_strict_lower_fraction':str(low_large),
 'small_regime_h_strict_lower_decimal':float(low_small),
 'large_regime_h_strict_lower_decimal':float(low_large),
 'no_analytic_lemmas_verified_by_script':True
}
p=Path(__file__).with_name('analytic_rational_certificate.json')
p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
