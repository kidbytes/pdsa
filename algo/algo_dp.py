# DP:
# There is an implicit DAG.
# In a DAG, all the nodes can be linearized. They can be arranged in a line
# so that all edges go from left to right.
# Each node represents a sample problem.
# All the edges incident on a node represent the dependent sub-problems
# All the sub-problems have to be processed, like find the max, etc to solve current problem.
# We do this for each node and find the node that has optimum value
# DP is an organization of brute force, where sub-problems are computed only once.

# Memoization is smart recursion, where the smaller solutions are cached.
# In memoization, there is overhead of recursion but we only compute
# sub-problems that are required. In DP, we compute every sub-problem
# from bottom-up.

# * There is an ordering on the subproblems, and a relation that shows how to
# solve a subproblem given the answers to "smaller" subproblems - that appear
# earlier.


#########################################
# EDIT DISTANCE
#########################################
# Find edit distance of x[m] and y[n]
# Think of a DAG
# Think of a smaller problem
# Think of how smaller problems can be combined to solve larger problem
# 
# To think about sub-problems, see how the final solution would look like.
# Strip off the last item from final solution. The new solution should
# correspond to some smaller input and give us an indea of how to compute the
# bigger solution using it.
# If you are working with multiple dimensions, then input can be reduced along
# each dimension

# S _ N O W Y
# S U N N _ Y

# We need to find the minimum edit distance (# of inserts, deletes, substitutions)

# To identify smaller subproblems:
#    The final solution can be in one of the 3 forms:

#      _          y[n]       y[n] 
#
# You need to find minimum of  edit(x[m], y[n-1]), edit(x[m-1], y[n]) and 
# diff(m,n) + edit(x[m-1], y[n-1])
# To cache solution e(i,j) for x[i] and  y[j] we need a 2-D array
# e(i-1,j), e(i,j-1) and e(i-1,j-1) should be computed before e(i,j)
# We can go in increasing row order or increasing column order. 
# The first row and column should correspond to empty strings.


#########################################
# Shortest paths from S to all vertices
#########################################
# The graph can be linearized to a DAG
# If we are finding a shortest path to D, we look at all incident edges to D.
# For each edge we get the shortest path to source edge + current distance from source to D.
# The minimum of this gives the shortest path to D.
# Graph G: 
# Adjacency List
# S -> [A:1, C:2]
# A -> [B:1]
# C -> [A:4, D:3]
# D -> [E:1]
# B -> [D:1, E:2]

# But we need incident edges. Otherwise, If we are computing for A, then we need
# to scan all RHS and find lines where A is present. This is not practical.

# Incident List
# A -> [S:1, C:4]
# C -> [S:2]
# B -> [A:6]

# The problem is which edge do you consider first.

# for node in linearized order:
#    for incidentNode of node:
#        d = S[incidentNode] + dist(incidentNode, node)
#        if (d < minDist):
#            minDist = d
#            parent[node] = incidentNode
#    S[node] = minDist

# Bellman Ford works on directed and undirected graphs - Single source shortest paths
# Supports negative weights but not negative cycles
# For N nodes, we do N iterations. After the Nth iteration there shouldn't be any
# updates to distances. If there is, then there is a cycle. We can say error out with
# this cycle exception

# Iteration 0 means using 0 intermediate nodes. Only node S has 0 distance at this level.
# You can reach S from S using 0 nodes and the distance is 0. All other nodes have inf at this level.
# Iteration 1 means using 1 intermediate node. Only direct edges from S will be updated in this level.
# Iteration 2 means using using S and one other intermediate node. If we are maintaining a 2D array,
# then we look at previous row and get all incident nodes to particular node on current row
# and compute the minimum distance.
# If no updates are made during an interation then we can exit prematurely.

# We don't even need a 2D array. 1D array is sufficient. We loop N times for all edges.
# Each entry gets updated if the new distance is less. Every time a node gets updated, 
# we can update all outgoing edges for efficieny. In this way, the loop can terminate
# prematurely. 
#        https://www.youtube.com/watch?v=vzBtJOdoRy8﻿


#########################################
# Longest increasing subsequences
#########################################
# From the inherent DAG we need to find the longest path.
# At every node, incident edges include all previous nodes that are less than current node.
#
# for i in range(1, len(items)):
#    for j in range (1, i+1):
#        if A[j] < A[i]:
#            if (L[j]+1 > L[i]):
#                L[i] = L[j]+1
#                P[i] = j
#        
    
#########################################
# Knapsack with repetition    
#########################################
# Item  Weight  Value
#  1      6       $30
#  2      3       $14
#  3      4       $16
#  4      2       $9
# Given Capacity aka Weight = 10

# Any item can be the last item
# if item 1, then we are looking at value V[10-6] + $30
# if item 2, then V[10-3] + $14, etc
# We need to find the max of all these combinations
# V[10-6], V[10-3], V[10-4], etc should all be computed
# We can compute V[0..10] from bottom up. Some of these values may not 
# be needed but we do that for convenience. Here, 0..10 are capacities.
# V[0] = 0, i.e. value is 0 for 0 capacity
# for c in range(1,11):
#    V[c] = 0
#    for item in Items:
#      wt = W[item]
#      val = V[item]
#      if ( (c-wt >= 0) and (V[c-wt] + val > V[c]) ):
#        V[c] = V[c-wt] + val

def knapsack_with_repetition(weights, values, capacity):
    if (len(weights) == len(values)):
        pass
    else:
        raise Exception("Unequal lengths")
    
    if (capacity <= 0):
        raise Exception("Capacity must be > 0")
    
    V = [0,0,0,0,0,0,0,0,0,0,0]
    
    for cap in range(1, capacity+1):
        V[cap] = 0
        for iw, wt in enumerate(weights):
            if (cap - wt >= 0 ):
                V[cap] = max(V[cap-wt] + values[iw], V[cap])
    
    print V[capacity]
    
weights = [6,3,4,2]
values = [30,14,16,9]
capacity = 10
knapsack_with_repetition(weights, values, capacity)




#########################################
# Knapsack without repetition    
#########################################
# If an item is included, then you cannot include that item again.
# How do you populate V[cap-wt]. We need to know what items were already included.
# So, we need to keep track of what items were already used.
# Item  Weight  Value
#  1      6       $30
#  2      3       $14
#  3      4       $16
#  4      2       $9
# Given Capacity/Weight = 10
# 
# For a given weight, if the item count is increased, is the last item 
# included or not? 
# V[cap][j] = max { V[cap-wj][j-1] + values[j], V[cap][j-1] }




#########################################
# Shortest Reliable Paths
#########################################
# Find the shortest path from s to t using at most k edges.
# Dijkstra's algorithm focuses only on the shortest path without
# remembering the number of hops in the path.
# Choose subproblems so that all vital information is remembered
# and carried forward.
# Lets dist(v, i) be the length of the shortest path from s to v that
# uses i edges.
# dist(v, 0) are infinity for all vertices except s, for which it is 0.
# dist(v, i) = min (u->v E edges) {dist(u, i-1) + l(u,v)}
#     i.e. for every incident edge on v, find a u-1 path. Then pick
#     the least u-1 path + l(u,v)
# dist(v,1) has a value if there is direct edge from s to v.
# Build a 2D table, with num Edges on Y-axis and nodes a X-axis.
# The row above should give paths from s to all nodes using row-1 hops.
# So, for given (i,j) we find all incident vertices to vertex j in row i-1.
# We pick the vertex k with minimum distance.


#########################################
# All-Pairs Shortest Paths
#########################################


#########################################
# Maximum Subarray
#########################################
# Brute force:
#   n(n-1)/2 ways of picking 2 indices
#   O(n) for each choice
#   O(n^3) overall complexity
#
# Divide & Conquer:
#   Divide into L & R
#   Return max subarray in each
#   Return max subarray ending at the last element of L
#   Return max subarray that starts at the 1st element of R
#   Max subarray is the max of all
#   O(nlogn)
#
# DP:
#    Max subarray can end at any index i
#    For each i, max subarray that ends at i is S[j] - min(S[i], for some i < =j)
#    5 -4 7 1
# def max_subarray_1(items):
#     maxStart = maxEnd = minSum = 0
#     maxSum = isum = items[0]
#     
#     for i in range(1, len(items)):
#         isum += items[i]
#         if (isum - minSum > maxSum):
#             maxSum = isum - minSum
#             maxEnd = i            
#         else:
#             maxStart = maxEnd = i
#              
#         if isum < minSum:
#             minSum = isum
#             
#     return (maxSum, maxStart, maxEnd)
# 
# def max_subarray_2(items):
#     sum[0] = items[0]
#     maxStart = maxEnd = 0
#     maxSum = sum[0]
#     
#     start=end=0
#     isum = sum[0]
#     
#     for i in range(1, len(items)):
#         if (isum + items[i] < isum):
#             if (isum > maxSum):
#                 maxStart = start
#                 maxEnd = end
#                 maxSum = isum
#                 
#             start = end = i
#             isum = items[i]
#         else:
#             sum += items[i]
#             end = i
#             
# 
#     return (maxSum, maxStart, maxEnd)