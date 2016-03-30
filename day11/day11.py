#
#  Advent of Code Day 11
#
import re
from string import ascii_lowercase

currentpswd = 'cqjxjnds'
bad = 'iol'
cons = [ascii_lowercase[i:i+3] for i in range(len(ascii_lowercase)-2)]

def next_pass(newpswd):
    newpswd = list(newpswd[::-1])
    length = xrange(len(newpswd))
    
    for i in length:
        if ord(newpswd[i])!=122:  
            newpswd[i] = chr(ord(newpswd[i])+1)
            break
        if ord(newpswd[i])== 122:
                newpswd[i] = chr(97)
        else:
            break
     
    newpswd = ''.join(newpswd[::-1])
    return newpswd

def fits_new_crit(newpswd):
    cons_letters = [c for c in cons if c in newpswd]
    bad_letters = [b for b in bad if b in newpswd]
    repeat_letters = re.findall(r'(\w)\1', newpswd)
    if len(bad_letters) == 0 and len(cons_letters) > 0 and len(repeat_letters) > 1:
        return True
    else:
        return False

def get_new_pass(pswd):
    pswd = next_pass(pswd)
    while fits_new_crit(pswd) == False:
        pswd = next_pass(pswd)
    else:
        return pswd


firstpswd = get_new_pass(currentpswd)
print "The new password is: ",firstpswd
print "The next password is: ", get_new_pass(firstpswd) 
