#
# Advent of Code Day 6
#

import re

columns = 1000
rows = 1000
lights = []

for y in range(rows):
    lights.append([])
    for x in range(columns):
        lights[-1].append(['F',0])

def process(command,start,end):
    for j in xrange(start[0],end[0]+1):
        for l in xrange(start[1],end[1]+1):
            if command[0] == "on":
                lights[j][l][0]='T'
                lights[j][l][1]+=1
            elif command[0] == "off":
                lights[j][l][0]= 'F'
                if lights[j][l][1] == 0:
                    lights[j][l][1]=0
                else: 
                    lights[j][l][1]-=1
            elif command[0] == "toggle":
                if lights[j][l][0] == 'F':
                    lights[j][l][0]='T'
                    lights[j][l][1]+=2
                else:
                    lights[j][l][0]='F'
                    lights[j][l][1]+=2  
                
def count_on():
    j = []
    for light in lights:   
        i = sum(x[0].count('T') for x in light)
        j.append(i)
    total = sum(g for g in j)  
    print total, 'lights are on'
    
def count_brightness():
    j = []
    for light in lights:
        i = sum(x[1] for x in light)
        j.append(i)
    total = sum(g for g in j)
    print 'Brightness is', total 

with open('day06.txt') as f:
    strings = ("on","off","toggle")
    for line in f:
        command = re.findall(r"\bon\b|\boff\b|\btoggle\b", line)
        total = re.findall(r'(\d+),(\d+)', line)
        start = (tuple(int(s) for s in total[0]))
        end = (tuple(int(s) for s in total[1]))
        process(command, start, end)

#Part One 
count_on()
#Part Two
count_brightness()
