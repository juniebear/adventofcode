import csv

dimensions = []

with open('day2.txt','r') as inputfile:
    for row in csv.reader(inputfile):
        for a in row:
            b = [int(n) for n in a.split('x')]
        dimensions.append(b) 
print dimensions

def calc_total_wrapping(dimensions):
    totalpaper = 0 
    for box in dimensions:
        side1 = box[0]*box[1]
        side2 = box[1]*box[2]
        side3 = box[2]*box[0]
        d = min(side1, side2, side3)
        totalpaper = totalpaper + (2*side1) + (2*side2) + (2*side3) + d
    return totalpaper

def calc_total_ribbon(dimensions):
    totalribbon = 0
    for ribbon in dimensions:
        ribbon.sort()
        bow = ribbon[0] * ribbon[1] * ribbon[2]
        totalribbon = totalribbon + 2*ribbon[0] + 2*ribbon[1] + bow
    return totalribbon
    
print 'Total square feet of wrapping paper needed: ', calc_total_wrapping(dimensions)
print 'Total length of ribbon needed: ', calc_total_ribbon(dimensions)
