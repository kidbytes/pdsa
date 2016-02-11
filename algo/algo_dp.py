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

# Find edit distance of x[m] and y[n]
# To identify smaller subproblems:
#    The final solution can be in one of the 3 forms:
#    x[m]    or    _    or   x[m-1]
#      _          y[n]       y[n-1] 
#
# You need to find minimum of  edit(x[m], y[n-1]), edit(x[m-1], y[n]) and 
# diff(i,j) + edit(x[m-1], y[n-1])
# To cache solution e(i,j) for x[i] and  y[j] we need a 2-D array
# e(i-1,j), e(i,j-1) and e(i-1,j-1) should be computed before e(i,j)
# We can go in increasing row order or increasing column order. 
# The first row and column should correspond to empty strings.

# Shortest paths from S to all vertices
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



# Longest increasing subsequences
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
    
 

# Edit Distance
# Think of a DAG
# Think of a smaller problem
# Think of how smaller problems can be combined to solve larger problem
# 
# To think about sub-problems, see how the final solution would look like.
# Strip off the last item from final solution. The new solution should
# correspond to some smaller input and give us an indea of how to compute the
# bigger solution using it.
# If you are working with multiple dimentions, then input can be reduced along
# each dimension

# S _ N O W Y
# S U N N _ Y

# We need to find the minimum edit distance (# of inserts, deletes, substitutions)




# Maximum Subarray
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
def max_subarray_1(items):
    maxStart = maxEnd = minSum = 0
    maxSum = isum = items[0]
    
    for i in range(1, len(items)):
        isum += items[i]
        if (isum - minSum > maxSum):
            maxSum = isum - minSum
            maxEnd = i            
        else:
            maxStart = maxEnd = i
             
        if isum < minSum:
            minSum = isum
            
    return (maxSum, maxStart, maxEnd)

def max_subarray_2(items):
    sum[0] = items[0]
    maxStart = maxEnd = 0
    maxSum = sum[0]
    
    start=end=0
    isum = sum[0]
    
    for i in range(1, len(items)):
        if (isum + items[i] < isum):
            if (isum > maxSum):
                maxStart = start
                maxEnd = end
                maxSum = isum
                
            start = end = i
            isum = items[i]
        else:
            sum += items[i]
            end = i
            

    return (maxSum, maxStart, maxEnd)