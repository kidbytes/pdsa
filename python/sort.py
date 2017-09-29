import util
Hi Ram,
How is every one? Couldn't catch up with you last year. This time I will make sure we will come to Bangalore.

I have a question for you. I'm exploring the option of finding a good residential school in Bangalore for Arnav. Currently he is in 7th grade.

Just a thought at the moment but I'm interested in finding out more. One of my friends pointed us to 'Canadian International School' and 
'Stonehill International School'.  Are you familiar with them? What is  your opinion in general about these international schools.
I'm debating between the schools here and international schools back in India.


#-------------------------
# SELECTION SORT
#-------------------------
# In each iteration find the smallest element
# Invariant: All elements to the left of i are sorted.  
# N, N-1, N-2...1 comparisons i.e. N^2/2 complexity
def selection_sort(inOutList):
    numSwaps = 0
    for i in range(len(inOutList)):
        minIdx = i
        for j in range(i+1, len(inOutList)):
            if (inOutList[j] < inOutList[minIdx]):
                minIdx = j

        inOutList[i], inOutList[minIdx] = inOutList[minIdx], inOutList[i] 
        numSwaps += 1
        
    return numSwaps
           
           
#-------------------------
# INSERTION SORT
#-------------------------             
# Invariant: Everything to the left of i is sorted.
# When i gets incremented, we bubble down element at i to its correct position
# When bubbling stops for the first time we immediately exit the inner loop. 
# This is efficient because we dont bubble down the entire list if not required
# Complexity: N^2/4 - twice as fast as selection_sort
def insertion_sort(inOutList):
    numSwaps = 0
    for i in range(0, len(inOutList)):
        j = i
        while (j > 0):
            if (inOutList[j] < inOutList[j-1]):
                inOutList[j], inOutList[j-1] = inOutList[j-1], inOutList[j]
                numSwaps += 1
                j -= 1
            else:
                break
        
    return numSwaps
 
 
#-------------------------
# SHELL SORT
#------------------------- 
# h-sort: Insertion sort with stride length h i.e. we compare elements at 1 and 1+h
#         for bubbling down
# We keep decreasing the stride length. Since list is partially sorted now, the bubbling
# should stop soon with each decrease in stride length
# a b c d e f   -> length=6, startIdx = last - (length-1), lastIdx = 0 + (length-1)
# 0 1 2 3 4 5   -> 3chars starting at 2 => (2 + (3-1)) = 4 is the last index.
#               -> For half open intervals, you just use 2 + 3 = 5
# -1 converts length to index. Then you can just work using indexes.
# When working with indexes, ix+0 is the first element, ix+1 is the second and so on.s
# You use it to compute the last inclusive index
# for processing. However, for half open intervals, you can directly use length
# Delete 3 chars starting at e => 4 -(3-1) = 2 is the start index
def shell_sort(inOutList):
    numSwaps = 0
    strideLen = len(inOutList)
    while (strideLen >= 1):
        for i in range(2*strideLen-1, len(inOutList), strideLen):
            j = i
            while (j > strideLen-1):
                j2 = j - strideLen
                if (inOutList[j] < inOutList[j2]):
                    inOutList[j], inOutList[j2] = inOutList[j2], inOutList[j]
                    numSwaps += 1
                    j -= strideLen
                else:
                    break
        strideLen /= 2
        
    return numSwaps                
            
            
    
#-------------------------
# MERGE SORT
#-------------------------
def merge(inList, start, mid, end):
    if not (start <= mid and mid <= end):
        raise Exception ("Invalid Range")
#     print "Processing (%d,%d,%d)" % (start, mid, end) 
    
    aux = []
        
    i = start
    j = mid
    for _ in range(start, end):
        if (i == mid):
            aux.append(inList[j])
            j += 1
        elif (j == end):
            aux.append(inList[i])
            i += 1
        elif (inList[i] < inList[j]):
            aux.append(inList[i])
            i += 1   
        else:
            aux.append(inList[j])
            j += 1
    
    inList[start:end] = aux[:]

            
def merge_sort(inOutList, start, end):
    if (end < start):
        raise Exception ("Invalid Range")
    
    if (end - start <= 1):
        return
    
    mid = start + (end - start)/2
    merge_sort(inOutList, start, mid)
    merge_sort(inOutList, mid, end)
    merge(inOutList, start, mid, end)                          
        
        
def bottomup_merge_sort(inOutList):      
    l = len(inOutList)
    stride = 2
    while (stride/2 <= l):
        for x in range(0, l, stride):
            start = x
            mid = min(start + stride/2, l)
            end = min(mid + stride/2, l)
#             print "Calling with (%d,%d,%d)" % (start, mid, end),
            merge(inOutList, start, mid, end)
#             print "\t\t%s" % str(inOutList)
        stride *= 2
    
        
#-------------------------
# QUICK SORT
#-------------------------
def partition(inOutList, start, end):
    
    if (end - start == 1):
        return start
    
    r = util.get_random_number(start, end)
    inOutList[start], inOutList[r] = inOutList[r], inOutList[start]
#     print inOutList[start:end]
    
    pivot = inOutList[start]
    i = start + 1
    j = end - 1
    
    while (True):
        # Stop at first item > pivot
        while(i < end and inOutList[i] < pivot):
            i += 1
    
        # Stop at first item < pivot
        while( j > start and inOutList[j] > pivot):
            j -= 1
                    
        if (i < j):
            inOutList[i], inOutList[j] = inOutList[j], inOutList[i]
            i += 1
            j -= 1
        else:
            break
        
    inOutList[start], inOutList[j] = inOutList[j], inOutList[start]
#     print "Pivot=%d, %s" % (r, str(inOutList[start:end]))
    return j
        
def quick_sort(inOutList, start, end):
    if (end - start <= 1):
        return
    p = partition(inOutList, start, end)
    quick_sort(inOutList, start, p)
    quick_sort(inOutList, p+1, end)    
    
# Uses partition instead of sorting    
def nth_largest(inOutList, n):   
    if (n > len(inOutList)):
        raise Exception("n larger than size of list")     
    
    if (n < 0):
        raise Exception("n cannot be smaller than 0")
    
    start = 0
    end = len(inOutList)
    while (end > start):
        p = partition(inOutList, start, end)
        if (p == n):
            return inOutList[p]
        elif (p < n):
            start = p + 1
        else:
            end = p
            
    return inOutList[n]


def test_nth_largest(inOutList):
    for x in range(0, len(inOutList)):
        print "%d Largest:\t%d" % (x, nth_largest(inOutList, x)) 

#
# Everything from and to the left of lt is less than pivot. 
# Everything to the right of gt is greater than pivot
# Everything from [lt, i) is equal to pivot
# [start,lt) has items < pivot
# [lt,i) has pivots
# (gt,end] has items > pivot
#  -----------------------------
#  < V  |  =V   |        | >V   |
#  -----------------------------
#       ^       ^        ^
#      lt       i        gt
#
def dutch_quick_sort(inOutList, start, end):
    if (end - start <= 1):
        return
    
    r = util.get_random_number(start, end)
    inOutList[start], inOutList[r] = inOutList[r], inOutList[start]
    
    lt = start
    i = start + 1
    gt = end - 1    
    pivot = inOutList[lt]
    while (i <= gt):
        if (inOutList[i] > pivot):
            inOutList[i], inOutList[gt] = inOutList[gt], inOutList[i]
            gt -= 1
        elif (inOutList[i] == pivot):
            i += 1
        else:
            inOutList[i], inOutList[lt] = inOutList[lt], inOutList[i]
            lt += 1
            i += 1
            
    dutch_quick_sort(inOutList, start, lt)
    dutch_quick_sort(inOutList, gt+1, end)
    
def main():
    ONE_TEST = 1
    if (ONE_TEST):
        print "DUTCH QUICK SORT:"
        inOutList = [11, 5, 4, 8, 2, 10, 3, 13, 14, 12, 1, 6, 15, 9, 7] 
        iol2 = list(inOutList)
        
        print "Input : " + str(inOutList)
        dutch_quick_sort(inOutList, 0, len(inOutList))
        print "Output: " + str(inOutList)
        print "IS_SORTED: %r" % util.is_sorted(inOutList)
        
        test_nth_largest(iol2)
        return
        
    #----------------------
    # Nth Largest
    #----------------------
    print "Nth Largest:"
    inOutList = [1,2,3,4,5,6,7,8]
    print inOutList
    for x in range(0, len(inOutList)):
        print "%d Largest:\t%d" % (x, nth_largest(inOutList, x))        
       
    inOutList = [8,7,6,5,4,3,2,1]
    print inOutList
    for x in range(0, len(inOutList)):
        print "%d Largest:\t%d" % (x, nth_largest(inOutList, x))    
          
    inOutList = util.generate_rand_list(15, allowDuplicates=False)
    print inOutList
    for x in range(0, len(inOutList)):
        print "%d Largest:\t%d" % (x, nth_largest(inOutList, x))
      
    inOutList = util.generate_rand_list(15, allowDuplicates=True)
    print inOutList
    for x in range(0, len(inOutList)):
        print "%d Largest:\t%d" % (x, nth_largest(inOutList, x))  
         
    return
                      
    #----------------------
    # Quick Sort
    #----------------------
    print "QUICK SORT:"
    inOutList = [11, 5, 4, 8, 2, 10, 3, 13, 14, 12, 1, 6, 15, 9, 7] #[1,3,5,7,2,4,6,8]
    print "Input : " + str(inOutList)
    quick_sort(inOutList, 0, len(inOutList))
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
     
    inOutList = util.generate_rand_list(15, allowDuplicates=False)
    print "Input : " + str(inOutList)
    quick_sort(inOutList, 0, len(inOutList))
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
          
    inOutList = util.generate_rand_list(15, allowDuplicates=True)
    print "Input : " + str(inOutList)
    quick_sort(inOutList, 0, len(inOutList))
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
    return

    #----------------------
    # Merge Sort
    #----------------------
    print "MERGE SORT:"
    inOutList = [1,3,5,7,2,4,6,8]
    print "Input : " + str(inOutList)
    merge_sort(inOutList, 0, len(inOutList))
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
     
    inOutList = util.generate_rand_list(15, allowDuplicates=True)
    print "Input : " + str(inOutList)
    merge_sort(inOutList, 0, len(inOutList))
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
    
    print "\nBOTTOMUP MERGE SORT:"
    inOutList = [1,3,5,7,2,4,6,8]
    print "Input : " + str(inOutList)
    bottomup_merge_sort(inOutList)
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
     
    inOutList = util.generate_rand_list(15, allowDuplicates=True)
    print "Input : " + str(inOutList)
    bottomup_merge_sort(inOutList)
    print "Output: " + str(inOutList)
    print "IS_SORTED: %r" % util.is_sorted(inOutList)
            
    inOutList = util.generate_rand_list(16, allowDuplicates=False)
    print "Input : " + str(inOutList)
    bottomup_merge_sort(inOutList)
    print "Output: " + str(inOutList)   
    print "IS_SORTED: %r" % util.is_sorted(inOutList)         
    return
        
    #----------------------
    # Selection Sort
    #----------------------
    print "\nSELECTION-SORT:"
    inOutList = [1,3,5,7,2,4,6]
    print "Input : " + str(inOutList)
    ns = selection_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
    print "IS_SORTED: " % util.is_sorted(inOutList)
    
    inOutList = util.generate_rand_list(10)
    print "Input : " + str(inOutList)
    ns = selection_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
        
    inOutList = util.generate_rand_list(10, 0, False)
    print "Input : " + str(inOutList)
    ns =selection_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
            
    #----------------------
    # Insertion Sort
    #----------------------
    print "\nINSERTION-SORT:"
    inOutList = [1,3,5,7,2,4,6]
    print "Input : " + str(inOutList)
    ns = insertion_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
    
    inOutList = util.generate_rand_list(10)
    print "Input : " + str(inOutList)
    ns = insertion_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
        
    inOutList = util.generate_rand_list(10, 0, False)
    print "Input : " + str(inOutList)
    ns = insertion_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
        
    #----------------------
    # Shell Sort
    #----------------------
    print "\nSHELL-SORT:"
    inOutList = [1,3,5,7,2,4,6]
    print "Input : " + str(inOutList)
    ns = shell_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns)       
    
    inOutList = util.generate_rand_list(10)
    print "Input : " + str(inOutList)
    ns = shell_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
        
    inOutList = util.generate_rand_list(10, 0, False)
    print "Input : " + str(inOutList)
    ns = shell_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns)   
                

    
        
if __name__ == '__main__':
    main()
        