import tree
import list

def build_from_sortedlist(inList, start=0, end=None):
    if (end == None):
        end = len(inList)
        
    if(end < start):
        raise Exception("Invalid Range %d %d" % (end, start))
    
    if (start == end):
        return None
    
    if (end - start == 1):
        nd = tree.Node(inList[start])
        nd.size = 1
        return nd
    
    mid = start + (end - start) / 2
    print "start=%d, mid=%d, end=%d" % (start, mid, end)
    nd = tree.Node(inList[mid])
    nd.left = build_from_sortedlist(inList, start, mid)
    nd.right = build_from_sortedlist(inList, mid+1, end)
    if (nd.left):
        nd.left.parent = nd
        nd.size += nd.left.size
    if (nd.right):
        nd.right.parent = nd
        nd.size += nd.right.size
                
    return nd                     



# Convert a BST to a doubly linked list
# x = inorder(nd.left, dlist)
# x.next = nd
# nd.prev = x
# y = inorder(nd.right)
# nd.next = y
# y.prev = nd
# return y
def convert_bst_to_doubly_linked_list(nd, lastNd):
    if not nd:
        return
    
    convert_bst_to_doubly_linked_list(nd.left, lastNd)
    lastNd.append(nd.data)
    convert_bst_to_doubly_linked_list(nd.right, lastNd)    
    

    
# Merge 2 BST's
# Convert each to a doubly linked list
# Merge them
# Convert them back to BST


# Build BST from a doubly linked list
# Find mid point and use it as a root

# Find k largest elements in a BST
# Do a reverse inorder traversal
# As soon as we hit k, stop

# From A pre-order traversal output, you can build a unique BST

# Lowest Common Ancestor

# Nearest Restaurant given location (p, q)
# First BST sorted on x coordinates
# Second BST sorted on y coordinates
# Take a delta d
# Find all x coordinates in (p+d, p-d) range
# Find all y coordinates in (q+d, q-d) range
# Find intersection of these points
# Choose d small and keep doubling
# Look Quad Trees / K-D Trees

# Most visited pages. Log file containing billions of entries of form
#      timestamp, page
# Return a list of k most common pages
# Hash Table has (timestamp -> pointer to timestamp record in BST)
# Whenever we need to increment count, find hash entry, reference BST
# and increment the counter there. 
# Find max in BST and call k predecessor calls to find k most hit entries


# Interval Trees
# Intervals are maintained as a BST
# Find all users that intersect a give interval [L,U]



'''
.###..........###
.###..###.......#
.###..#.#.....###
......###.......#
..............###
.................


def class Node:
    self.color = white
    self.visited = False
    self.neighbors = []
    
    
def DFS(nd):
    nd.visited = True
    count = 1
    
    for nei in nd.neighbors:
        if (nei.color == 'white'):
            next
            
        if not nei.visited:
            nei.visited = True
            count += 1
            DFS(nei)
            
    return (nd, count)



def Erase(nd):
    nd.color = white

    for nei in nd.neighbors:
        if nei.color == 'black':
            nei.color = white
            Erase(nei)
        

def foo(listOfLists):
    maxCnt = None
    maxNd = None
    
    for list in listOfLists:
        for entry in list:
            if (entry.color == 'white'):
                next
                
            if entry.visited:
                next
                
            (nd, cnt) = DFS(entry)
            if (maxCnt is None or cnt > maxCnt):
                maxCnt = cnt
                maxNd = nx
                
    Erase(maxNd)
'''
    
def main():
    inList = [1,2,3,4,5,6,7,8,9]
    nd = build_from_sortedlist(inList)
    bst = tree.BST(nd)
    bst.print_bst()
    bst.print_inorder()
    
    dummy = list.DList()
    convert_bst_to_doubly_linked_list(nd, dummy)
    print "\nDList:" + str(dummy)
    
if (__name__ == "__main__"):
    main()    
    
    