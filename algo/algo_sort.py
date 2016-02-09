# In a array count of all entries such that i < j but a[i] > a[j]
#
# The number of inversions is 0 only if the array is sorted in asc order.
# In all other cases the count is > 0
# Example: [1,3,5,2,4,6] has inversions [3,2], [5,2] and [5,4]
# Pictorially: If you were to print input list in one row and sorted list in row below
# and connect the same numbers, the number of the crossing endges gives
# the number of inversions.
# If inversions are less that means two lists are more similar and vice-versa.
# Use Case: Identify customers with similar taste and recommed products
# The largest number of inversions possible is nC2. This happens when arrays are sorted
# in reverse oder.
#
# During a merge operation, every time you copy an element Y from the right array,
# the number of elements remaining in the left array represents the number of
# inversions for Y
def merge(inList, start, mid, end, inversions):
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
            for x in range(i, mid):
                inversions.append("(%d,%d)" % (inList[x], inList[j]))
                            
            j += 1

    
    inList[start:end] = aux[:]

            
def merge_sort(inOutList, start, end, inversions):
    if (end < start):
        raise Exception ("Invalid Range")
    
    if (end - start <= 1):
        return
    
    mid = start + (end - start)/2
    merge_sort(inOutList, start, mid, inversions)
    merge_sort(inOutList, mid, end, inversions)
    merge(inOutList, start, mid, end, inversions)        
    
    
    
def count_inversions(inList):    
    if (len(inList) <= 1):
        return 0
    
    inOutList = list(inList)
    inversions = []
    merge_sort(inOutList, 0, len(inOutList), inversions)
    
    return inversions
   
    


def main():
    inList = [1,3,5,7,2,4,6,8]
    print "Input : " + str(inList)
    inversions = count_inversions(inList)
    print "Num Inversions=%d\n%s" % (len(inversions), str(inversions))
     


if __name__ == '__main__':
    main()
