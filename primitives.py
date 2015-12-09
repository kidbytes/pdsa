import random
import list

# Maximize x[j]- x[i] subject to i<j
def max_difference_bruteforce(x):
    if (len(x) == 0):
        raise Exception("Zero Input")
        
    maxDiff = None
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if (maxDiff is None or x[j] - x[i] > maxDiff):
                maxDiff = x[j] - x[i]
                iSave = i
                jSave = j
                
    return [maxDiff, iSave, jSave]

def max_difference_better(x):
    if (len(x) == 0):
        raise Exception("Zero Input")
    
    maxDiff = None
    minSofar = x[0]
    for i in range(len(x)):
        if (x[i] > minSofar):
            continue
        
        for j in range(i+1, len(x)):
            if (maxDiff is None or x[j] - x[i] > maxDiff):
                maxDiff = x[j] - x[i]
                minSofar = x[i]
                iSave = i
                jSave = j
                
    return [maxDiff, iSave, jSave]
    
def main():
#     x = []
#     for i in range(6):
#         x.append(random.randrange(1,10))
# 
#     print x        
#     y = max_difference_bruteforce(x)
#     print y 
#     y = max_difference_better(x)
#     print y
    ls = list.DList()
    for _ in range(6):
        ls.append(random.randrange(1,15))
        
    print ls
    ls.print_reverse()
    
if __name__ == '__main__':
    main()    