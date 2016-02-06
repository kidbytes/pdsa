'''
Created on Feb 4, 2016

@author: surya
'''

# Nearest Repeatition
# Given a sentence, we need to find the nearest repeating words

def find_nearest_repetition(sentence):
    myMap = {}
    maxDist = 0
    maxEnd = 0
    retWord = None
    for ix, word in enumerate(sentence):
        if myMap.has_key(word):
            dist = ix - myMap[word]
            if (dist < maxDist):
                maxDist = dist
                maxEnd = ix
                retWord = word
                
        myMap[word] = ix
        
    return (retWord, maxDist, maxEnd)
        
        
# At most 1 character need not repeat
def can_a_word_be_permuted_to_form_palindrome(word):
    myMap = {}
    for c in word:
        if myMap.has_key(c):
            myMap[c] += 1
        else:
            myMap[c] = 1
        
    freq1=0    
    for key in myMap:
        if (myMap[key] % 2 == 1):
            freq1 += 1
            if (freq1 > 1):
                return False
            
    return True

# Partition a dictionary into anagrams
# An anagram is a permutation of a word that is valid
def partition_anagrams(dictionary):
    myMap = {}
    
    for word in dictionary:
        x = word.sort()
        if not myMap.has_key(x):
            myMap[x] = []
            
        lst = myMap[x]
        lst.append(word)
            
    for key in myMap:
        lst = myMap[key]
        print lst         
    
  
# Pair users by attributes. Given: UserId -> [attributes]
# Exact Match:
#    If attributes are small, use bit array. Each bit represents an attribute
#    Use hash function for bit array
#    So, given a set of attributes we can quickly look up if a user is present
# Approximate Match:
#    Use minHash
            
            
# K-Suspicious strings
# If two strings have a common substring of length at least K, then
# they are K-Suspicious. Given a list of strings we need to find all
# K-Suspicious strings
def find_k_suspicious_strings(string_list):
    '''
    For each word of length N, we will find N-K+1 substrings of length K
    Store each word in a hash table. All strings that collide are K-Suspicious.
    Pairing strings and processing them is very inefficient.
    '''   
    pass


# Bloom Filters
# We have a universe U of words
# We take a N bit Array
# We use K hash functions
# For each word, we compute K hash values. Each value is modulus N, so that
# it gives a bit location in the bit array. Each word then has k bits.
# When searching, we get K hash values and see if the bit position is 1 for each.
# If the bit is 0 even for a single hash function then the search should
# be flagged failure.