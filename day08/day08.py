#
# Advent of Code Day 08
#
import re

strings = []
part_one = []
part_two = []

with open('day08.txt') as f:
    for i in f:
        i = i.rstrip('\n')[1:-1]
        strings.append(i)
       
for s in strings:
    literal = len(s)+2
    memory_part_one = len(s.decode('string_escape'))
    memory_part_two = len(re.escape(s))
    part_one.append(literal-memory_part_one)
    part_two.append((memory_part_two+6)-literal)
   
print "Part One:",sum(part_one)
print "Part Two:",sum(part_two)
