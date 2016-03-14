#
# Advent of Code Day 09
#
from itertools import permutations

origin = {}
results = []

with open('day09.txt') as f:
    for i in f:
        source, _, dest, _, distance = i.split()
        origin[(source, dest)] = int(distance)
        origin[(dest, source)] = int(distance)
    
location = list(set(key[0] for key in origin))

for p in permutations(location):
    d = sum([origin[pair] for pair in zip(p[:-1], p[1:])])
    results.append(d)

print "Part One: Shortest Route is",min(results)
print "Part Two: Longest Route is",max(results)
