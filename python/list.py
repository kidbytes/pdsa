import random

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->3->4->5.

Node* ptr = inputNode;
Node* list1 = NULL;
Node* list2 = NULL;
 
 
while(ptr) {
  if (ptr->data < 3)
      if (list1 == NULL) {
        list1 = list1End = ptr
      } else {
         list1End->next = ptr
         list1End = ptr
      }
  else
      if (list2 == NULL) {
        list2 = list2End = ptr
      } else {
         list2End->next = ptr
         list2End = ptr
      }
      
      list1End->next = list2
      return list1;
}
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return "[%d]" % self.data
    
#Single Linked List
class SList:
    def __init__(self, other=None):
        self.head = None
        self.last = None
        
        if (other is None):
            return
        
        if (not isinstance(other, SList)):
            raise Exception("Invalid other")
                
        curr = other.head
        while (curr):
            self.append(curr.data)
            curr = curr.next
            
    @staticmethod
    def create_list(numRandomItems):    
        lst = SList()
        for i in range(numRandomItems):
            lst.append(random.randrange(1,numRandomItems))    
        return lst
    
    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
            
    def __str__(self):
        x = []
        curr = self.head
        while(curr is not None):
            x.append(curr.data)
            curr = curr.next
            
        return str(x)
      
    def index(self, data, node=None):
        if (node is None):
            curr = self.head
        else:
            curr = node
                
        while (curr):
            if (curr.data == data):
                return curr
            
        return None    
        
    def delete_with_value(self, data):
        dummy = Node(data-1)
        dummy.next = self.head
        
        cnt = 0
        curr = dummy
        while(curr.next):
            if (curr.next.data == data):
                curr.next = curr.next.next
                cnt += 1
            else:
                curr = curr.next
                
        self.head = dummy.next
        return cnt
    
    def rdelete_with_value(self, nd, data):
        if (nd is None):
            return None
        
        if (nd.data != data):
            ret = self.rdelete_with_value(nd.next, data)
            nd.next = ret
            return nd
        else:
            tmp = nd.next
            nd.next = None
            return self.rdelete_with_value(tmp, data)
            
    def reverse(self, nd):
        if (nd is None):
            return None
        
        ret = self.reverse(nd.next)
        if (ret is None):
            self.head = nd
        else:
            ret.next = nd
        
        nd.next = None    
        return nd
            
        

        
                
#Double Linked List        
class DList(SList):
    def __init__(self):
        SList.__init__(self)
    
    @staticmethod
    def create_list(numRandomItems):    
        lst = DList()
        for i in range(numRandomItems):
            lst.append(random.randrange(1,numRandomItems))    
        return lst
        
    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
            self.last = self.head
        else:
            x = Node(data)
            self.last.next = x
            x.prev = self.last
            self.last = x
    
    def reverse(self, nd):
        if (nd is None):
            return None
        
        ret = self.reverse(nd.next)
        if (ret is None):
            self.head = nd
        else:
            ret.next = nd
        
        nd.prev = ret
        nd.next = None    
        self.last = nd
        return nd
        
    def print_reverse(self):
        curr = self.last
        while(curr is not None):
            print curr.data,
            curr = curr.prev
        print "\n"                
            
def main():
#     lst = SList.create_list(10)
#     print lst
# 
#     lst2 = SList(lst)
#     print lst2
#     
#     lst.delete_with_value(5)
#     print lst
#     
#     lst2.rdelete_with_value(lst2.head, 5)
#     print lst2
#     
#     lst2.reverse(lst2.head)
#     print lst2              
    
    dlst = DList.create_list(10)
    print dlst
    dlst.print_reverse()
          
    dlst.reverse(dlst.head)
    print dlst
    dlst.print_reverse()

      
if __name__ == '__main__':
    main()                
                