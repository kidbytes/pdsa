import util

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
        
        
        
        
def main():
    
    #----------------------
    # Merge Sort
    #----------------------
    inOutList = [1,3,5,7,2,4,6,8]
    print "Input : " + str(inOutList)
    merge_sort(inOutList,0, len(inOutList))
    print "Output: " + str(inOutList)
    
    inOutList = util.generate_rand_list(15, allowDuplicates=False)
    print "Input : " + str(inOutList)
    merge_sort(inOutList,0, len(inOutList))
    print "Output: " + str(inOutList)
        
    return
        
    #----------------------
    # Selection Sort
    #----------------------
    print "\nSELECTION-SORT:"
    inOutList = [1,3,5,7,2,4,6]
    print "Input : " + str(inOutList)
    ns = selection_sort(inOutList)
    print "Output: %s --> %d" % (str(inOutList), ns) 
    
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
        