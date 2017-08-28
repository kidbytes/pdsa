# String Transformation
# Given a dictionary D, strings s and t, find if s produces t.
# Is there a way to go from s to t using words within the Dictionary?
# We can define an undirected graph with words in dictionary. There is
# a path between u and v if u and v differ by only 1 character.
# The problem can be solved by finding the shortest path between s and t.
# BFS finds the shorted paths.
#
# Here, instead of marking a node visited, we can delete the node from dictionary.
# For this, input dictionary has to be copied. Once deleted it will never be 
# encountered as a neighbor.

# For each word:
#     For each char in word:
#        For each char X in [a..z]
#            Replace char with X
#            if new word found in dictionary:
#                Delete word from dictionary   //So that during BFS we don't hit this again
#                Push word to queue with counter incremented
#        Restore to original word   //We will be replacing next character


# def does_s_produce_t(myDict, s, t):
#     que = []
#     que.append({s:1})
#     
#     while (len(que) > 0):
#         word = que.pop(0).key()
#         for i in range(len(word):
#             for j in range(1,27):
#                 temp = word[0:i] + 'a' + j  + word[i:]
#                 
                
                 
                