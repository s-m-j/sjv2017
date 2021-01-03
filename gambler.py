#-----------------------------------------------------------------------
# gambler.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# Принимает целочисленные аргументы stake (сумма), goal (цель) 
# и trialCount (число попыток).
# Производится не более trialCount попыток начиная с суммы stake 
# и до достижения 0 (разорение) либо goal (успех). Печатает в стандартный
# вывод процент побед и среднее число "бросков" в эксперименте.

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

# Запуск trialCount раз до достижения 0 либо целевого выигрыша.
bets = 0
wins = 0
for t in range(trials):
    # Запуск одного экспеимента.
    cash = stake
    while cash > 0 and cash < goal:
        # Симуляция броска.
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

stdio.writeln(str(100 * wins//trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets//trials))
