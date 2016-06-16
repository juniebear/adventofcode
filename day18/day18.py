#
# Advent of Code Day 18
#
from itertools import product, starmap

origlights = []

class Lights():
    
    on = "#"
    off = "."
   
    def __init__(self, lights, steps):
        self.lights = lights
        self.steps = steps
        
        self.rows = len(lights)
        self.columns = len(lights[0])
    
    def grid(self, part):
        n = 0
        corners = [(0,0), (0,self.rows-1), (self.columns-1,0), (self.columns-1,self.rows-1)]
        while n < self.steps:
            newlights = [[0 for x in range(self.rows)] for y in range(self.columns)]
            for column in range(self.columns):
                for row in range(self.rows):
                    total = 0
                    neighbors = self.next_to((column, row))
                    for x,y in neighbors:
                        if self.lights[x][y] == self.on:
                            total += 1
                    if self.lights[column][row]== self.on and (total==2 or total==3):
                        newlights[column][row]= self.on
                    elif self.lights[column][row]== self.off and total==3:
                        newlights[column][row] = self.on 
                    elif part == 2 and (column, row) in corners:
                        newlights[column][row]= self.on  
                    else:
                        newlights[column][row]= self.off
                   
            self.lights = newlights         
            n += 1
            
        return sum(l.count('#') for l in self.lights)
                       
    def next_to(self, position):  #return all the neighbors of the current position  
        neighbors = []
        x,y = position
        neighbor = starmap(lambda a,b:(x+a, y+b), product((0,-1,+1), (0,-1,+1)))
        for n in neighbor: # remove all coordinates not within bounds.
            (l,m) = n
            if not l < 0 and not l > self.columns-1 and not m < 0 and not m > self.rows-1:
                neighbors.append(n)   
        return neighbors[1:]

with open('day18.txt') as f:
    for line in f:
        light = list(line.strip())
        origlights.append(light)   
xmaslights1 = Lights(origlights, 100)
print "Part one",xmaslights1.grid(1),"are on."
xmaslights2 = Lights(origlights, 100)
print "Part two",xmaslights2.grid(2),"are on."
