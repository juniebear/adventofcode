#
# Advent of Code Day 16
#
from collections import Counter
samples = dict()
ticker = {'children':'3',
          'cats':'7',
          'samoyeds':'2',
          'pomeranians':'3',
          'akitas':'0',
          'vizslas':'0',
          'goldfish':'5',
          'trees':'3',
          'cars':'2',
          'perfumes':'1'}

with open("day16.txt") as f:
    for i in f:
        data = i.replace(':','').replace(',','').strip().split(' ')
        samples[data[1]] = {data[x]:data[x+1] for x in xrange(2,len(data),2)}
        
def correct_aunt(possible):
    for x,y in Counter(possible).iteritems():
        if y == 3:  # Return the aunt where all given values match
            return x

def part_one():
    possible = []
    for key,value in samples.iteritems():
        for k in value.keys():
            if value[k]==ticker[k]: #Check which aunt values match the ticker tape
                possible.append(key) #Add them to a list
    return correct_aunt(possible)

def part_two():
    possible = []
    for key,value in samples.iteritems():
        for k in value.keys():
            if k == "cats" or k == "trees":
                if value[k] > ticker[k]:
                    possible.append(key)
            elif k =="pomeranians" or k =="goldfish":
                if value[k] < ticker[k]:
                    possible.append(key)
            else:
                if value[k] == ticker[k]:
                    possible.append(key)
    return correct_aunt(possible)
                 
print "Part One: Aunt",part_one()
print "Part Two: Aunt",part_two()  
