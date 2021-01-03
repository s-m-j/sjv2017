import sys
import stdio

year = float(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and ((year % 100 != 0))
isLeapYear = isLeapYear or ((yaear % 400 == 0))
