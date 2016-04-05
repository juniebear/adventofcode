#
# Advent of Code Day 14
#
stats = []
finish = 2503

with open('day14.txt') as f:
    for i in f:
        data = i.strip().split()
        stats.append({'name': data[0], 
                      'kms':int(data[3]), 
                      'sec':int(data[6]), 
                      'rest':int(data[-2]), 
                      'distance':0, 
                      'time':0, 
                      'resting':0, 
                      'is_flying':True,
                      'points':0})
        
def award_points():
    furthest = 0
    for s in range(len(stats)):
        if stats[s]["distance"] > furthest:
            furthest = stats[s]["distance"]
            reindeer = s
    
    stats[reindeer]["points"] += 1

def race():
    for f in range(finish):
        print f
        for s in range(len(stats)):
            if (stats[s]["time"] < stats[s]["sec"]-1) & stats[s]["is_flying"]:
                stats[s]["distance"] += stats[s]["kms"]
                stats[s]["time"] += 1
            elif (stats[s]["time"] == stats[s]["sec"]-1) & stats[s]["is_flying"]:
                stats[s]["distance"]+= stats[s]["kms"]
                stats[s]["is_flying"] = False
                stats[s]["resting"] = 0        
            elif (stats[s]["is_flying"]==False) & (stats[s]["resting"] < stats[s]["rest"]-1):
                stats[s]["resting"] += 1
            elif (stats[s]["is_flying"]==False) & (stats[s]["resting"] == stats[s]["rest"]-1):
                stats[s]["resting"] += 1
                stats[s]["time"] = 0
                stats[s]["is_flying"] = True
        
        award_points()

def winner_part_one():
    furthest = 0
    winner = ''
    race()
    for s in range(len(stats)):
        if stats[s]["distance"] > furthest:
            winner = stats[s]["name"]
            furthest = stats[s]["distance"]
    return winner+' with a distance of '+ str(furthest)+' km.'

def winner_part_two():
    highest = 0
    for s in range(len(stats)):
        if stats[s]["points"] > highest:
            winner = stats[s]["name"]
            highest = stats[s]["points"]
    return winner +' with  '+ str(highest)+' points.'

print "Part One: The winner of the race is", winner_part_one()
print "Part Two: The winner with the highest points is", winner_part_two()
