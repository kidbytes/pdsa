import random
import list
import sys

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
    myX = '''
    <test name="ATJ-%0d">
    <parameter name="testCaseId" value="ATJ-%0d" />
    <classes>
        <class name="com.verizon.cao.selenium.modules.Apply_To_Jobs" />
    </classes>
    </test>
    '''
    
    for i in range(79, 141):
        y = myX % (i, i)
        print y
        
    sys.exit(0)
    
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