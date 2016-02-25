'''
######################
# RECURSIVE          #
######################
def print_preorder(nd):
    print nd   

    if (nd.left is not None):  
        print_preorder(nd.left)
        
    if (nd.right is not None): 
       print_preorder(nd.right)

    return

def print_inorder(nd):
    if (nd.left is not None):  
        print_inorder(nd.left)
        
    print nd   
    
    if (nd.right is not None): 
       print_inorder(nd.right)

    return
    
def print_postorder(nd):
    if (nd.left is not None):  
        print_postorder(nd.left)
        
    if (nd.right is not None): 
       print_postorder(nd.right)

    print nd   

    return
    
def reset_flags(nd):
    nd.lflag = nd.rflag = False   

    if (nd.left is not None):  
        reset_flags(nd.left)
        
    if (nd.right is not None): 
       reset_flags(nd.right)

    return

def depth(nd):
    
    if (nd.left is None and nd.right is None):
        return 0
    
    ldepth = rdepth = 0
    if (nd.left):
        ldepth = 1 + depth(nd.left)
        
    if (nd.right):
        rdepth = 1 + depth(nd.right)
        
    return max(ldepth, rdepth) 
        
    
def lwidth(nd):
    if (nd.left is None and nd.right is None):
        return 0
    
    lw = rw = 0
    if (nd.left):
        lw = lwidth(nd.left) + 1
    if (nd.right):
        rw = lwidth(nd.right) - 1
    
    return max(lw, rw)
    
    
def rwidth(nd):
    if (nd.left is None and nd.right is None):
        return 0
    
    lw = rw = 0
    if (nd.right):
        rw = rwidth(nd.right) + 1
    if (nd.left):
        lw = rwidth(nd.left) - 1    
        
    return max(rw, lw)
        
            
def width(nd):
    
    lw = rw = 0
    if nd.left:
        lw = lwidth(nd.left) + 1
        
    if nd.right:
        rw = rwidth(nd.right) + 1       
        
    print "width: lw=%d, rw=%d"% (lw, rw)
            
    return lw + rw;
                  
    
            
        
######################
# ITERATIVE          #
######################    
def print_preorder_i(nd):
    stk = [nd]
     
    while (len(stk)):
        curr = stk.pop()
        
        while (curr):
            print curr
            if (curr.right):
                stk.append(curr.right)
                
            curr = curr.left
            

        
def print_inorder_i(nd):
    stk = [nd]
    
    while (len(stk)):
        curr = stk.pop()
        
        if (curr.lflag):
            print curr
            if (curr.right):
                stk.append(curr.right)
                
        else:            
            while (curr is not None):
                curr.lflag = True 
                stk.append(curr)
                curr = curr.left
    
    
    
def print_postorder_i(nd):
    stk = [nd]
    
    while (len(stk)):
        curr = stk.pop()
        
        if (curr.lflag and curr.rflag):
            print curr
            
        elif (curr.lflag):
            if(curr.right):
                curr.rflag = True
                stk.appendd(curr)
                stk.append(curr.right)
            else:
                print curr
        
        else:
            while (curr is not None):
                curr.lflag = True 
                if (curr.right is None):
                    curr.rflag = True
                stk.append(curr)
                curr = curr.left
                    
                    
    
def print_bfs(nd):
    stk = [nd]
    
    while (len(stk)):
        curr = stk.pop(0)
        print curr
        if (curr.left):
            stk.append(curr.left)        
        if (curr.right):
            stk.append(curr.right)


'''

import util

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        
    def __str__(self):
        return "%r" % self.data
    
    
def str2(nd):
    if (nd is None):
        return "None"
    else:
        return str(nd)
    
    
# Binary Search Tree
class BST:
    def __init__(self, nd=None):
        if (nd is not None):
            if (not isinstance(nd, Node)):
                raise Exception("Invalid other")
        
        self.head = nd
        self.input = []
        
    @staticmethod
    def create_from_rand(numItems=10, start=0, allowDuplicates=True):
        r = util.generate_rand_list(numItems, start, allowDuplicates)

        tree = BST()
        for i in r:
            tree.insert(i)
                            
        return tree
                
    @staticmethod            
    def create_from_list(lst):
        tree = BST()
        for i in lst:
            tree.insert(int(i))
        return tree
                    
    def insert(self, data):
        self.head = self._insert(self.head, data)
        
    def min(self):
        return self._min(self.head)
    
    def max(self):
        return self._max(self.head)   
    
    # Returns inorder predecessor node
    def pred(self, data):
        curr = self._find(self.head, data)
        if (curr is None):
            return None;
        
        if (curr.left):
            return self._max(curr.left);
        else:
            while(curr.parent):
                if (curr.parent.data <= data):
                    return curr.parent
                else:
                    curr = curr.parent
            return None    
                
    # Returns inorder successor node          
    def succ(self, data):
        curr = self._find(self.head, data)
        if (curr is None):
            return None;
        
        if (curr.right):
            return self._min(curr.right)
        else:
            while(curr.parent):
                if (curr.parent.data >= data):
                    return curr.parent
                else:
                    curr = curr.parent
            return None             
                       
    # Returns first node with node.data <= data                                   
    def floor(self, data):
        return self._floor(self.head, data)    
    
    # Returns first node with node.data >= data
    def ceil(self, data):
        return self._ceil(self.head, data)  
    
    # Returns node that is at 'pos' in inorder traversal                                                                    
    def select(self, pos):
        return self._select(self.head, pos)
    
    # Returns number of nodes < data
    def rank(self, data):
        return self._rank(self.head, data)
            
    # Prints in level order
    def print_bst(self):
        print "\nBST:"
        lst = []
        lst.append(self.head)
        cnt=1
        while(len(lst) > 0):
            nd = lst.pop(0)
            cnt -= 1
            print nd.data,
                
            if (nd.left):
                lst.append(nd.left)
            if (nd.right):
                lst.append(nd.right)
                
            if (cnt == 0):
                print ""
                cnt = len(lst)                    
    
    def get_inorder_list(self):
        out = []
        self._get_inorder_list(self.head, out)
        return out
                                 
    def print_inorder(self):
        out = self.get_inorder_list()
        print "\nINORDER:",
        for e in out:
            print e.data,
    
    #------------------------------------
    # Private
    #------------------------------------    
    def _size(self, nd):
        if (nd is None):
            return 0
        else:
            return nd.size
                   
    def _insert(self, nd, data):
        if (nd is None):
            nd = Node(data)
            nd.size = 1
            self.input.append(nd)
            return nd
        
        if (data <= nd.data):
            nd.left = self._insert(nd.left, data)
            nd.left.parent = nd
        else:
            nd.right = self._insert(nd.right, data)    
            nd.right.parent = nd
            
        nd.size += 1
        return nd  
                    
    def _find(self, nd, data):
        if (nd is None):
            return None
        
        if (data == nd.data):
            return nd
        elif (data < nd.data):
            return self._find(nd.left, data)
        else:
            return self._find(nd.right, data)
                
    def _max(self, nd):
        if (nd is None):
            return None
        
        curr = nd
        while(curr.right):
            curr = curr.right
        return curr   
                 
    def _min(self, nd):
        if (nd == None):
            return None
        
        curr = nd
        while(curr.left):
            curr = curr.left
        return curr  
     
    def _floor(self, nd, data):
        if (nd is None):
            return None
        
        if (data == nd.data):
            return nd
        elif (data < nd.data):
            return self._floor(nd.left, data)
        else:
            t = self._floor(nd.right, data)
            if (t is None):
                return nd
            else:
                return t
        
    def _ceil(self, nd, data):
        if (nd is None):
            return None
        
        if (data == nd.data):
            return nd
        elif (data > nd.data):
            return self._ceil(nd.right, data)
        else:
            t = self._ceil(nd.left, data)
            if (t is None):
                return nd
            else:
                return t
            
    def _select(self, nd, pos):
        if (nd is None or pos < 0):
            return None
        
        lsize = 0
        if (nd.left):
            lsize = nd.left.size
            
        if (pos == lsize + 1):
            return nd
        elif (pos < lsize + 1):
            return self._select(nd.left, pos) 
        else:
            if (nd.right):
                return self._select(nd.right, pos - (lsize + 1))
        
        return None
    
    def _rank(self, nd, data):
        if (nd is None):
            return 0
        
        if (data == nd.data):
            return self._size(nd.left)
        elif (data < nd.data):
            return self._rank(nd.left, data)
        else:
            return 1 + self._size(nd.left) + self._rank(nd.right, data)
                            
    def _get_inorder_list(self, nd, out):
        if (nd is None):
            return
        
        if (nd.left):
            self._get_inorder_list(nd.left, out)
        
        out.append(nd)
             
        if (nd.right):
            self._get_inorder_list(nd.right, out)    
                                     
def main():
    tree = BST.create_from_rand(15, allowDuplicates=False)
#     tree = BST.create_from_list("9 3 2 2 5 6 6 6 6 3".split())
    
    print "INPUT  :",
    for e in tree.input:
        print str2(e),
        
    tree.print_inorder()
    tree.print_bst()
    print "\nMin=%s, Max=%s" % (str2(tree.min()), str2(tree.max()))
    
    print "\nPRED/SUCC:"
    for e in tree.get_inorder_list():
        p = tree.pred(e.data)             
        s = tree.succ(e.data)
             
        print "%s -> %s\t%s" % (str2(e), str2(p), str2(s))    
         
    print "\nFLOOR/CEIL/RANK:"
    for e in tree.get_inorder_list():
        l = tree.floor(e.data + 1)             
        u = tree.ceil(e.data + 1)
        r = tree.rank(e.data)     
        print "%s -> %s\t%s\t%d" % (e.data+1, str2(l), str2(u), r)   
     
    print tree.rank(7)   
#         
#                     
#     print "\nSelect5=%d, Rankd5=%d" % (tree.select(5).data, tree.rank(5)) #1 8 6 9 2 3 5 2 5 5 
    
if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print ex                 