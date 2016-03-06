#
# Advent of Code Day 05
#
import re   

naughty = []
stringlist = []
nice = []
pair = ['ab','cd','pq','xy']
vowels = ['a','e','i','o','u']

with open('day05.txt') as f:
    stringlist = [line.rstrip() for line in f]
    
def part_one():
    for s in stringlist:
        repeating = re.findall(r'((\w)\2{1,})',s)
        totvowels = sum(s.count(x)for x in vowels)
        badlist = any(letters in s for letters in pair)
        if repeating and totvowels > 2 and badlist==False:
            nice.append(s)
    return len(nice)

def part_two():
    nice[:]=[]
    for s in stringlist:
        repeating = re.findall(r'(\w\w).*\1',s)
        repdiv = re.findall(r'(\w).{1}\1',s)
        if repeating and repdiv:
            nice.append(s)
    return len(nice)

print part_one(), 'strings are nice'
print part_two(), 'strings are nice'

