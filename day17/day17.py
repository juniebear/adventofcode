#
# Advent of Code Day 17
#
eggnog = 150        
containers = [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
final = []

def sums(container, eggnog, combo=[]):
    total = sum(combo)
    
    if total == eggnog:
        final.append(combo)
    if total > eggnog:
        return
    
    for c in range(len(container)):
        n = container[c]
        leftover = container[c+1:]
        sums(leftover, eggnog, combo+[n])
    
    return len(final)
        
def part_two():
    count = 0
    shortest = min(map(len,final))
    for f in final:
        if len(f)==shortest:
            count += 1
    return count

print "Part One:", sums(containers, eggnog)
print "Part Two:", part_two()
