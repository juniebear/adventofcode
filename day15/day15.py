#
# Advent of Code - Day 15
#

import re
properties = []
total = []
parttwo = []
with open("day15.txt") as f:
    for i in f:
        data = re.findall(r'(-?\w+)',i)
        ingredient = [int(data[2]), int(data[4]), int(data[6]), int(data[8]), int(data[10])]
        properties.append(ingredient)
           
#create combination of all numbers that add up to 100
def get_combos(qty):
    amounts = []
    for w in xrange(1,qty-len(properties)+2):
        for x in xrange(1,qty-w):
            for y in xrange(1,qty-w-x): 
                z = qty-(w+x+y)
                a = [w,x,y,z]
                amounts.append(a)
    return amounts

def cook():
    quantities = get_combos(100)
    total = 0
    for q in quantities:
        capacity=durability=flavor=texture=calories=0
        for i in xrange(len(q)):
            capacity += properties[i][0]*q[i]
            durability +=  properties[i][1]*q[i]
            flavor += properties[i][2]*q[i]
            texture += properties[i][3]*q[i]
            calories += properties[i][4]*q[i]
        if calories == 500:
            parttwo.append([capacity, durability, flavor, texture, calories])
        if capacity < 0 or durability < 0 or flavor < 0  or texture < 0:
            newtotal = 0
        else: 
            newtotal = capacity*durability*flavor*texture
        if newtotal > total: 
            total = newtotal
    return total

def bestcalories():
    total = 0
    for p in parttwo:
        if p[0] < 0 or  p[1]< 0 or p[2] < 0 or p[3] < 0:
            newtotal = 0
        else:
            newtotal = p[0]*p[1]*p[2]*p[3]
        if newtotal > total: 
            total = newtotal
    return total
        
print "Part One - Total Score", cook()
print "Part Two - 500 Calories", bestcalories()
        
    
