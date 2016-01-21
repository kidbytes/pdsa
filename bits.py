import math


# Returns the number of bits set for a given number
def num_bits_set(x):
    cnt = 0
    while(x):
        cnt+=1
        x = x & (x-1)
        
    return cnt

# Returns the parity of a number
#   True if num_bits_set odd
#   False otherwise
def parity(x):
    cnt = num_bits_set(x)
    if (cnt % 2 == 0):
        return False
    else:
        return True


##    
def int_to_string(x):
    if (x ==0):
        return '0'
    
    out = []
    isNegative = False
    if (x < 0):
        isNegative = True
        x = -x
    
    while(x):
        c = x % 10 + int('0')
        out.append(c)
        x /= 10; 
        
    if (isNegative):
        out.append('-')
        
    return ''.join(map(str, out[::-1])) # Reverse

##
def string_to_int(x):
    isNegative = 0
    if (x < 0):
        isNegative=1
        
    y = 0
    for c in x[isNegative:]:
        if (ord(c) < ord('0') or ord(c) > ord('9')):
            raise Exception('Invalid character: ' + c)
        
        y = (y*10) + ord(c) - ord('0') # or int(c)
        
    if isNegative:
        return -y
    else:
        return y

# Returns the power set for a given set
# Exmple:
#   for 3 elems, iterate from 1 to 7
#   treat each number as a bit array
#   for each number
#      extract each bit that is set to 1 from right
#      for each bit set to 1, get the bit index by getting log
#      the log value can be used as index into input array
def power_set(elems):
    if len(elems) == 0:
        print "Empty Input"
        return
    
    out = []
    end = int(math.pow(2, len(elems)))
    for i in range(1, end):
        x=i
        s=''
        while(x):
            y = x & ~(x-1)          #extract the right most 1 bit position
            lg = int(math.log(y,2)) #get the bit index in bit array. Should be a power of 2
            s += elems[lg]          #use the bit index to index input array
            x = x & (x-1)           #unset the right most 1 bit. We don't need it any more
        out.append(s)
        
    return out
    
    
def main():
#     TEST: num_bit_set
#     for x in range(17):
#         print "num_bits_set(%d): %d" % (x, num_bits_set(x))

#     TEST: power_set
#     ps = power_set(['a','b', 'c', 'd', 'e'])
#     for i, v in enumerate(ps):
#         print "%02d -> %s" % (i+1,v) 

#     TEST: int_to_string
#     print int_to_string('-2345')
    
#     TEST: string_to_int
    print string_to_int('123b45')
    print ord('a')
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print e
    