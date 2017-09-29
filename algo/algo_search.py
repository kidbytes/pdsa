'''
Created on Jan 22, 2016

@author: surya
'''

# 1 2 3
# l=0 r=2 m=1
# l=0 r=1 m=0 OR l=2 r=2 m=2
# l=1 r=1 m=1
# The loop breaks when all of them are equal. In the next iteration the
# inequality doesn't hold
def find_k(items, k, l=None, r=None):
    
    if (len(items) == 0):
        return None
    
    if (l < 0 or r < 0 or (l > r)):
        return None
    
    if (l is None):
        l = 0
        
    if (r is None):
        r = len(items) - 1
        
    while (l <= r):
        m = l + (r - l >> 1)
        if (k == items[m]):
            return m
        
        if (k < items[m]):
            r = m - 1
        else:
            l = m + 1
    
# Finds the left most occurence of k  
def first_occurence_of_k(items, k):
    r = len(items) - 1;
    if (r == 0):
        return None
    
    first = None
    l = 0
    while (l <= r):
        m = l + (r - l >> 1)
        if (k == items[m]):
            first = m
            r = m - 1  # Keep searching left for better index
        if (k < items[m]):
            r = m - 1
        else:
            l = m + 1    
            
    return first

# When k is not found, binary_search for k either ends at the
# first element greater than k or last element less than k
def first_larger_than_k(items, k):
    r = len(items) - 1;
    if (r == 0):
        return None
    
    first = None
    l = 0
    while (l <= r):
        m = l + (r - l >> 1)
        if (k < items[m]):
            first = m
            r = m - 1  # Keep searching left for better index
        else:
            l = m + 1    
            
    return first    

# Finds index of smallest element in a circular sorted list
def find_pivot_in_circular(items):
    r = len(items) - 1;
    if (r == 0):
        return None
    
    l = 0
    while (l < r):  # different
        m = l + (r - l >> 1)
        if (items[m] > items[r]):
            l = m + 1
        else:
            r = m   # different
            
    return l      

# Finds the smallest element in a circular sorted list    		
def find_min_in_circular(items):  
    p = find_pivot_in_circular(items)
    if p is not None:
        return items[p]
    
# Finds k in a circular sorted list   
def find_k_in_circular(items, k):            
    p = find_pivot_in_circular(items)
    if p is None:
        return None
    
    r = len(items) - 1;
    if (k <= items[r]):
        return find_k(items, k, p, r)
    else:
        return find_k(items, k, 0, p-1)
        
    
# We need to generate 1,2,4,8,.. (powers of 2)
# Indexing starts at 0. So we are looking for 2^p - 1
def find_k_unknown_length(items, k):
    p = 0
    
    while (True):
        try:
            i = ( 1 << p ) - 1
            
            if (k == items[i]):
                return i
            
            if (k < items[i]):
                break
        except:
            p = p + p/2
            
        p = 2 * p
        
# Find kth largest in array A[n] in O(n) time
# Pick a random element and partition around it. If p == (k-1) we are done.
# Otherwise, find kth largest in A[0:p-1] or find (k - (p + 1)) in A[p+1:n-1]


# Find kth largest in array A[n] in O(n) time when n is not known.
# 1. Use min heap to store k largest elements. When a new element e comes in
#    if (e > top)
#       pop the top and insert e

# 2. Take an array of size 2k-1. When the array becomes full, find kth largest
#    using partition and discard the smallest k elements. You can use an array
#    of size 4k and discard 3k smaller elements when it becomes full. Benefits
#    of partiton is higher with larger N. More storage gives better performance 
#    but there is a space trade off.



# 1 Billion IP addresses. Each is 32 bit unsigned integer. 32 bits give you 1 Billion.
# Find missing IP address. 
# If you split the IP into two 16 bits, then there will be 2^16 most significant bits.
# And for each, there will be 2^16 least signficant bits for a total of 2^32 entries.
# So, you need an array of 2^16 32-bit unsiged ints. You can probably use shorts.
# For each of the 2^16 indexes, we increment the count. There will be one entry whose
# total is less than 2^16.

#index by most significant 16bits
for (i=0; i < allIps; i++)
	A[i >> 16] += 1

# each index should have a count of 2^16
for (i=0; i < 2^16; i++)
	if (A[i] < 2^16)
		savedIndex = i
		break
	
# index by least 16 significant bits
for (i=0; i < allIps; i++)
	if (A[i >> 16] == savedIndex)
		B[i && x00001111] += 1  --> Use least significant bits here
		
# each index should have a count of 1
for (i=0; i < 2^16; i++)
	if (B[i] == 0)
		savedIP = (savedIndex << 16) | i
		break		
		
return savedIP

# A and B are 2 arrays with same numbers except for one which is a repeat in A.
# Find A XOR B. There should be only one entry which is 1. For this entry, do
# XOR again to get back the original values. Find if this value is a repeat or
# missing in A


# Find majority element from a sequence of unknow length.
# If you discard 2 distinct elements, the majority element still remains majority
# in the remaining stream.
def find_majority(items):
    majority = items[0]
    count = 1
    i = 1
    while(True):
        if (count == 0):
            majority = items[i]
            count = 1
        elif (items[i] == majority):
            count += 1
        else:
            count -= 1
            
        i += 1
        


# Hash function for words in a dictionary
def my_hash(inStr, modulus):
    val = 0
    prime = 997
    
    for c in inStr:
        val = (val * prime + ord(c)) % modulus
        
    return val
        