import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
def solve(meal_cost, tip_percent, tax_percent):
    total = round(meal_cost*(1 + tip_percent/100 +
                                          tax_percent/100))
    return(total)

if __name__ == '__main__':
    meal_cost = float(input('Meal cost : ').strip())

    tip_percent = int(input('Tip percent : ').strip())

    tax_percent = int(input('Tax percent : ').strip())

    total = solve(meal_cost, tip_percent, tax_percent)

    print(total)





