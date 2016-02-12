
directions = []

with open('day03.txt') as inputfile:
    for a in inputfile:
        directions.append(a)

def trip(directions): 
    house = [(0,0)]
    for b in directions:
        for direction in b:
            location = house[len(house)-1]
            if direction == '^':
                new = location[0],location[1]+1
            if direction == 'v':
                new = location[0],location[1]-1
            if direction == '>':
                new = location[0]+1,location[1]
            if direction == '<':
                new = location[0]-1,location[1]
            house.append(new)
    return house

def santa_alone():
    houses = set( trip(directions))#return unique values
    return len(houses)

def santa_and_robosanta(directions):
    for b in directions:
        santa = b[::2]
        robo = b[1::2]    
        a = trip(santa)
        b = trip(robo)
        houses = set(a+b)
    return len(houses)

print 'Santa delivered at least 1 present to', santa_alone(),'houses'
print 'Santa and Robo-Santa delivered at least 1 present to', santa_and_robosanta(directions), 'houses'  
