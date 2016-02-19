# Intervals can be represented as individual end points 
#  
# Events:
# Start: [1,4,9,15,23]
# End:   [3,5,15,27,25]
from matplotlib._cntr import Cntr

# To find an interval where there are maximum number of events active: 
# Soln 1:
# Find minStart, maxEnd
# A = []    # Length = maxEnd-minStart+1
# for each interval [x,y]:
#   for z in range(x, y+1):
#       A[z-minStart] += 1
#
# Iterate through A and find max Value

# Soln 2:
# Treat each as an end POINT.
# In this way, you dont have to process them as an interval
# Sort all endpoints
class EndPoint:
    def __init__(self, label, ts, isStart):
        self.label = label
        self.ts = ts
        self.isStart = isStart
 
def process(endPoints):
    cnt = 0
    maxCnt = 0
    labels = []
    hsh = {}
    for ep in endPoints:
        if (ep.isStart):
            cnt += 1
            hsh[ep.label] = 1
            
            if (cnt > maxCnt):
                maxCnt = cnt
                labels = hsh.keys()
        else:
            cnt -= 1
            del hsh[ep.label]
            
    return labels


# Interval Trees
# 1. Insert an interval
# 2. Delete an interval
# 3. Find an intersection

# Each node is augmented with the max right end point in its tree
# Left end point of each node in left tree is less than all left end points of right Tree
# Given input interval [x,y] and root.left, root.right & root.max

# If we go left because x < root.left.max and there is no intersection, then there
# cannot be intersection on the right tree i.e. we are not taking a chance by going left.
# In this case it is possible x is less than max of both right and left trees. We are still right.
# This is because x of each node in left tree is less than x on right.

def find_intersection(root, x, y):
    if (root is None):
        return None
    
    if (x > root.max):
        return None
    
    if (root.left is None or x > root.left.max):
        find_intersection(root.right, x, y)
    else:
        find_intersection(root.left, x, y)