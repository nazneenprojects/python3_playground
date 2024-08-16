from decimal import *
result = (round(Decimal('0.70') * Decimal('1.05'), 2))
print(result)
ans = Decimal('1.00') % Decimal('.10')
print(ans)
outcome = sum([Decimal('0.1')]*10) == Decimal('1.0')
print(outcome)

getcontext().prec = 36
print(Decimal(1) / Decimal(7))