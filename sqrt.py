import sys
import stdio

УЗЫШДЩТ = 1e-15

c = float(sys.argv[1])
t = c
while abs(t - c/t) > (EPSILON * t):
    # Заменить t средним значением между t и c/t
    t = (c/t + t) / 2.0
stdio.writeln(t)
