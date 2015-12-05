import tree

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

def main():
    inList = [1,2,3,4,5,6,7,8,9]
    nd = build_from_sortedlist(inList)
    bst = tree.BST(nd)
    bst.print_bst()
    bst.print_inorder()
    
if (__name__ == "__main__"):
    main()    
    
    