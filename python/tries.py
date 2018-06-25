# Used for symbol table implementation / efficient spell checking
# Existing solutions like Red Black Trees and Hash tables work on the entire length
# of the string and are logN.  Tries work only on logN characters.
from distutils.sysconfig import PREFIX


# Red Black Trees and Hash tables are original work horses. Can we do better?
# Example: Symbtol table for string keys
#     StringST()
#     void put (String key, Value val)
#     Value get(String key)
#     void delete(String key)
#
# Goal: Faster than hashing and more flexible than BSTs
#
# Hashing is at least in the order or L where L is the length of string.
# This is because we compute the hash.


# R-Way Tries
# There are R possible characters/symbols
# Each node has R children (i.e. R links. One for each possible character)
# Every node has a unique path to it.
# Most of the links are null usually.
# Each node has a path to it. The path identifies the preceding character of the node.
# The root node has no path, so the preceding character is ""
# Cumulative path from root to a node gives a prefix where the node is the last character.
# A node can also have a value if the path represents a key. If it is null then it is just
# an incomplete key.

# Does each node know what character it represents?
#   Not really. The index of the link can be used to deduce that
# Does each node know what substring leads to it?
# Is it necessary?

# [key] -> [value]    
# ex. she->0
#     shell->4 
#                         s
#                           h
#                           e (0)
#                           l
#                           l (4)


# class Node:
#    value = None
#    links[R] = [None]
#
#
# In the above case, the top most node has a value of "" and link for s initialized.
# If you follow this link,  you will reach a node that has a value None and link for
# h. The node for e will have a value of 0. You can also augment the node with 
# a field that stores the character it represents in the chain. Or you can keep
# track of it outside while traversing.

# Additional Symbol Table Api
#    def get_keys(nd)   //Return all keys
#    def has_prefix("abcd") //Return all keys that have "abcd" as prefix. Auto-complete
#    def longest_prefix("abcdef") //Find a key that has the longest prefix in "abcdef"
#    def matches("abc.def")   //.  matches any character. Return key that  match this regex

# To find all keys, you can either do a BFS or DFS on the trie.
# With BFS you work in layers and emit any keys you find at that layer.
# With DFS you go deep on each path and emit keys on the way.
# Looks like if you have long keys, DFS may find more keys quickly.
# And if you have short key, BFS may find more quickly.
# But if you want to do auto-complete i.e find lexically next keys then ?
# I think you just emit all non-null links at that node.

'''
def auto_complete(nd, prefix, out):
    foreach idx, link in enumerate(nd.links):
        if (link != None):
             nextChar = char(ord('a') + idx
            if (link.value != None):
                out.append(prefix + nextChar)
            auto_complete(link, prefix + nextChar, out)
        
        
'''
# A not None link represents the character and we need not store the actual  
# Root node has only links and not key or value
#
#  Given 'she' and Node nd
#  for c in input:
#      i = ord(c) - ord('a')
#      next = nd.links[i]
#      if next is None:
#         return None
#    
#  return next.value
    
# This solution is optimal if R is small

# Deleting a node.
# Remove the value first.
# If a node has all null links and no value, delete the node.
# Go up one node and repeat
# We dont need parent pointer. We start from top for the word and store
# pointers as we are descending


# Iterating a R-way Trie i.e. print all keys using DFS
void print_keys(Node* nd, const string& prefix)  //Initial prefix is ""
{
    if (nd->value)
        print prefix
        
    for(int i=0 ; i < nd->links.size(); i++) 
    {
        if (nd->links[i])
            print_keys(nd->links[i], prefix + itoa('a' + i))
    }
}
def print_keys(nd, que):
    
    
    if (que[-1].data is not None):
        print que
    
    for link in nd.links:
        if (link is not None):
            que.append(link.data)
            print_keys(link, que)
        que.pop(-1)
    