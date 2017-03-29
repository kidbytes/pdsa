import random

def generate_rand_list(numItems=10, start=0, allowDuplicates=True):
    out = []
    
    if (allowDuplicates):
        for _ in range(numItems):
            x = random.randrange(1,numItems)
            out.append(start + x)
    else:
        uniq = set()
        while (True):
            x = random.randrange(1,numItems+1)
            if x not in uniq:
                uniq.add(x)
                out.append(start + x)
                  
            if (len(uniq) == numItems):
                break        
            
    return out

def get_random_number(start, end):
    if (end < start):
        raise Exception("end=%d < start=%d" % (end, start))
    
    if (end - start == 1):
        return start
    
    return random.randint(start, end-1)
    
def is_sorted(inList):
    if (len(inList) <= 1):
        return True
    
    for x in range(1, len(inList)):
        if (inList[x] < inList[x-1]):
            return False
    
    return True

    
    
    
    