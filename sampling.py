print("Akshat Verma")
n = 10.89
print(n)
print(int(n))
print(type(n))

e = (2,3,4)
print(e)
print(type(e))
set1 = {"a", "b", "c"}   
print(type(set1))
s ="'chai'"
print(repr(s))

import random

print(random.randint(1, 10))
l1 = ['a', 'b', 'c', 'd']
print(random.choice(l1))
print(random.sample(l1, 3))
random.shuffle(l1)
l1
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

from fractions import Fraction
MYFRA = Fraction(1, 3)
print(MYFRA)
