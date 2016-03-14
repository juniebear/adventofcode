#
# Advent of Code Day 10
#
import re
value = "1321131112"
i = 0

def looknsay(num):
    newnumber = ''
    numbers = [n.group(0) for n in re.finditer(r'(\d)\1*',num)]
    for n in numbers:
        newnumber += str(len(n)) + str(n[0])
    return newnumber

def answer(value, qty):
    for i in range(qty):
        value = looknsay(value)
        i+=1
    return len(value)
    
print "Part One", answer(value, 40)
print "Part Two", answer(value, 50)
