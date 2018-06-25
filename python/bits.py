import math

'''
Thinking about Bits:
* ASCII:  
Dec 0 is NUL
Dec 8 is Backspace
Dec 32 is Space
Dec 127 is DEL  --> Last character

Dec [48-57]  is [0-9]
Dec [65-90]  is [A-Z]
Dec [97-122] is [a-z]

Dec 48 is Hex 30

* Byte is the lowest level at which you can access data; there's no "bit" type and
we can't ask for an individual bit or perform operations on it. Every bit wise operator
will be applied to an entire byte.

* Left and right shift operators are not implementation dependent for unsigned numbers.
For signed numbers, the right shift operator is implementation defined.

* On left shift, zero's are used for padding on the right end. Left shift is equivalent
to multiplying by power of 2. When you shift more than that can fit, you get all 0's.

* Right shift is equivalent to intger division by 2. Right shift 5 by 1 bit gives 2.
Whether the padding to left is 0 or 1 is implementation defined.

* Shifting by 0 bits will give the same number.

* val = val | 1 << n
Sets the nth bit to 1 in val

* Largest possible value for an unsigned integer:
unsigned int max = ~0

* A XOR 0 --> you will always get A back
  A XOR 1 --> you will always get ~A back
  
  If you XOR with 1 twice, you will the original back

* 
x & (1 << n)  --> Test nth bit
x | (1 << n)  --> Set nth bit
x & ~(1 << n) --> Unset nth bit
x ^ (1 << n)  --> Toggle nth bit
x & (x - 1)   --> Turn off right most 1 bit
x & (x + 1)   --> Turn on right most 0 bit 
~x & (x+1)    --> Isolate the right most 0 bit
x & (-x)      --> Isolate the right most 1 bit
x & ~(x-1)    --> Same or x & (~x+1)

Actually -x is the same as ~x+1 in 2s complement
-x is also equal to (numSymbols - x). If you have 4 digits, then numSymbols = 16.
The symbols are from 0 - 15.
-3 = (16-3) = 13 = 1101    
-3 = ~(3-1) = ~2 = 1101

0000  0     9 1001
0001  1    10 1010 
0010  2    11 1011
0011  3    12 1100
0100  4    13 1101
0101  5    14 1110
0110  6    15 1111
0111  7     
1000  8

8421
0110 -> 6   --- x
0101 -> 5   --- x-1

0100 -> 6 & 5  (x & x-1)

largest power of 2 less than the or equal to number
1010 - 1000


'''

# Returns the number of bits set for a given number
def num_bits_set(x):
    cnt = 0
    while(x):
        cnt+=1
        x = x & (x-1)  # Unset the rightmost 1
        
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

# xsaZXsazss the power set for a given set
# Exmple:
#   for 3 elems, iterate from 1 to 7
#   treat each number as a bit array
#   for each number
#      extract each bit that is set to 1 from right
#      for each bit set to 1, get the bit index by getting log
#      The log value can be used as index into input array
# 001, 010, 011, 100, 101, 110, 111
# (Gives, possible ways in which 1|2|3 bits can be turned on)
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
    