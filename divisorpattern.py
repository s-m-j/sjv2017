import sys
import stdio

n = int(sys.argv[1])

for i in range(1, n + 1):
    # Вывести i-тую строку
    for j in range(1, n + 1):
        # Вывести j-тый элемент i-той строки
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write('  ')
    stdio.writeln(i)
