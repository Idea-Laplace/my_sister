import postfix_upgrade as pos
import re
from fractions import Fraction as fr

with open('doc2.txt') as file:
    result = 0
    for line in file:
        sum = re.sub(r'[\n\t]', '', line)
        if sum:
            result += fr(sum)
    print(result)