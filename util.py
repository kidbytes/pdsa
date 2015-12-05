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