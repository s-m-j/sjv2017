import sys
import stdio

n = int(sys.argv[1])

total = 0.0
for i in range(1, n + 1):
    # Добавить i-тое слагаемое
    total += 1.0 / i

stdio.writeln(total)
