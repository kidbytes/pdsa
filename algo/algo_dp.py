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
            minEnd = i 
            
    return (maxSum, maxStart, maxEnd)

def max_subarray_2(items):
    sum[0] = items[0]
    maxStart = maxEnd = 0
    maxSum = sum[0]
    
    start=end=0
    isum = sum[0]
    
    for i in range(1, len(items)):
        if (isum + items[i] < isum):
            if (sum > maxSum):
                maxStart = start
                maxEnd = end
                maxSum = isum
                
            start = end = i
            isum = items[i]
        else:
            sum += items[i]
            end = i
            

    return (maxSum, maxStart, maxEnd)