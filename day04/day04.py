import hashlib

key = 'yzbqklnj'

def find_hash(key, start):
    answer = ''
    i = 0
    while not answer.startswith(start):
        i += 1
        a = key + str(i)
        h = hashlib.md5(a)
        answer = h.hexdigest()
    return i


print 'The secret key of MD5 hash that starts with 5 zeroes is ' + str(key) + str(find_hash(key,'0'*5))
print 'The secret key of MD5 hash that starts with 6 zeroes is ' + str(key) + str(find_hash(key,'0'*6))
