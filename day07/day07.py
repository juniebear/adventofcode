#
# Advent of Code Day 07
#
connection = []
wires = {}
value = []

with open('day07.txt') as f:
    for i in f:
        value = i.strip().split(r" -> ")
        connection.append(value)
          
def run_wires(x):  
    
    if x.isdigit():
        return int(x)
    else:
        if x in wires:
            return int(wires[x])
            
    for c in connection:
        if c[1] == x:
            s = c[0].split(r' ')
            if 'AND' in s:
                signal = run_wires(s[0])&run_wires(s[2])
            elif 'OR' in s:
                signal = run_wires(s[0])|run_wires(s[2])
            elif 'NOT' in s:
                signal = ~run_wires(s[1])&0xFFFF
            elif 'LSHIFT' in s:
                signal = run_wires(s[0])<<int(s[2])
            elif 'RSHIFT' in s:
                signal = run_wires(s[0])>>int(s[2])
            elif c[0].isdigit():
                signal = c[0]
            else:
                signal = run_wires(s[0])
            
            wires[c[1]] = signal
            
            return int(signal)

def part_two(x):
    b = run_wires(x)
    newa = b
    wires.clear()
    wires['b'] = newa
    return run_wires('a')   

            
print 'Part 1: Signal', run_wires('a'), 'is provided to wire a.'
print 'Part 2: Signal', part_two('a'), 'is provided to wire a.'
