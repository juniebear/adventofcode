#
# Advent of Code Day 13
#
from itertools import permutations

guestlist = {}
guests = []

def happiness(gorl, num):
    if gorl == 'gain':
        return int(num)
    if gorl == 'lose':
        return -int(num)

with open('day13.txt') as f:
    for i in f:
        data = i.strip().replace('.','').split()
        guestlist[data[0], data[-1]] = happiness(data[2], data[3])
        guests.append(data[0])
        
guests = set(g for g in guests) #Guest List

def find_seats(guests, guestlist):
    most_happy = 0
    for g in permutations(guests):
        happiness = 0
        for i in range(len(g)-1):
            c = g[i] # current guest
            n = g[i+1] # next guest
            happiness += (guestlist[c,n] + guestlist[n,c])
        
        happiness += (guestlist[g[0],g[-1]] +guestlist[g[-1], g[0]]) #Add the First and Last Guest too.
        if happiness > most_happy:
            best_seats = g
            most_happy = happiness
    
    return best_seats, most_happy

def add_me():
    for g in guests:
        guestlist['me', g] = 0
        guestlist[g, 'me'] = 0
    guests.add('me')
    return find_seats(guests, guestlist)

print "Best seating chart, part one: ", find_seats(guests, guestlist)
print "Best seating chart, part two: ", add_me()
