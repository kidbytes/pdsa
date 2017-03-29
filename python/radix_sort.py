# The lower bound for any comparison based sorting is NLogN. 
# Can we do better?
# Radix sorts give us a performance of WN where W is length of key.

# Key-Indexed Couting
# Keys are between 0 and R-1
# R is usually small but each item is repeated many times
# Can use key as an array index
# Count frequencies of each letter using key as index
# Compute frequency cumulates
# The cumulate give the index of next entry in final array
# Copy back into original array
# a 2   a->0
# b 3   b->2
# c 1   c->5
# d 2   d->6
# e 1   e->8
# f 3   f->9
                           
# Consider a mapping of student name to section number
# Since the section numbers are small and limited, we
# can use section number as an index into an array and
# sort student names using key indexed sort. However,
# the sort will be stable


# Key Indexed sort uses cumulates. In a cumulated array,
# the value at an index tells where the next entry goes
# Example: A['c'] = 3 tells the a key starting with 'c'
# will go at index 3 in the final solution. Once we put a key,
# we increment the index so that the next key with 'c' goes to the 
# incremented index.

def get_cumulates(items):
    cum = []
    cum.append(0)
    for i in range(1, len(items)):
        cum.append(items[i-1] + cum[i-1])
        
    return cum


x = get_cumulates([2,3,1,2,1,3])
print x

# Cumulate at index i gives the first entry for item at i.
# Iterate over the original array, move item to temp, increment cumulate
# Copy back from temp. This kind of sort is stable
    
    
# If you just have a list of strings you can LSD or MSD sorting.    
# LSD Sorting (Go from right i.e least signigicant digit to right)
# Task: Sort on fixed-length key field like SSN, Date, Acct Number, etc
# Sort on each character using key-indexed counting
# Sort must be stable
# By the time you do the most significant character, the strings are
# automatically sorted. For each character you are spending N+N
# This is a linear sort



# MSD Sorting (Go from right to left. Each char processed in a recursive call)
# Works on variable length keys. Have to override charAt() method to return
# null when index exceeds the size of the string.
# Parition input into R buckets according to 1st character. 
# There are R symbols
# Recursively sort each bucket on the next character
# Too many recursive calls
# A seperate count array needed in each call that needs to be initialized
# Length of count array equals number of symbols R


# Longest repeated substring
# Use suffix sort. A string of length N has N suffixes
# atom
# tom
# om
# m
# Now, sort to bring longest repeated substrings together
# Check longest common prefix (LCP) of adjacent substring to find solution
