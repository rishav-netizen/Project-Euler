
from decimal import Decimal, getcontext

getcontext().prec = 50  # 50 digits of precision

for d in range(2, 1000):
    a = Decimal("1") / Decimal(str(d))
    print(a, end=" | Denominator: ")
    print(d)