#-----------------------------------------------------------------------
# factors.py
#-----------------------------------------------------------------------

import stdio
import sys

# Принимает целочисленное n как арзумент командной строки
# и выводит в стандартный вывод разложение n на простые множители.

n = int(sys.argv[1])

factor = 2
while factor*factor <= n:
    while n % factor == 0:
        # Вычислить множитель.
        n //= factor
        stdio.write(str(factor) + ' ')
    factor += 1
    # Любые множители n больше либо равны factor.

if n > 1:
    stdio.write(n)
stdio.writeln()