
# Stacks and Queues from heap
# Maintain an integer variable 'order'.
# Store items of type (order, x)
# order is incrememted for each item pushed into heap
# Heap entries are compared on order
# Stack: Max-Heap
#        Last item inserted has maximum order
#        It will be the first item to be popped
# Queue: Min-Heap
#        First item inserted has minimum order
#        It will be the first item to be popped



# Compute K closest stars
# Farthest star should be at the top of heap
# If the next input is closer than top, then pop the top item and insert input
#
# Compute K largest elements
# Min-Heap with the smallest element at top
# If the next element is greater than top, delete top and insert input


# Compute median of a running sequence
# Use a Min-Heap(H) and Max-Heap(L) simultaneously
# Max-Heap stores the smaller half and Min-Heap stores the larger half.
# if L.size() > H.size():
#    x = L.pop()
#    H.insert(x)
# else:
#    x = H.pop()
#    L.insert(x)

