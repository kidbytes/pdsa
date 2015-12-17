class Heap:
    def __init__(self, initial_list=None):
        self.data = ['dummy']
        self.last = 0

        if (initial_list is not None):
            print "INPUT:",
            print initial_list
            for x in initial_list:
                self.insert(x)
            print "OP1  :",
            print self.data
            
            self.data = ['dummy']
            self.data.extend(initial_list)
            self._heapify()
            print "OP2  :", 
            print self.data
        

    def _print(self):
        for i, d in enumerate(self.data):
            if (i > 0):
                print "%s " % d

        print "\n"

    def _swap(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp


    def _getSinkIndex(self, k):
        if (2*k > self.last):  # Has no children
            return None

        if (2*k == self.last): # Has only left child
            cmp = 2*k
        else:                  # Has both children
            if (self.data[2*k] > self.data[2*k + 1]):
                cmp = 2*k
            else:
                cmp = 2*k + 1

        if (self.data[cmp] > self.data[k]):
            return cmp
        else:
            return None


    # k is the index of the item that has to swim up
    def _swim(self, k):
        while (k/2 >= 1):
            if (self.data[k] > self.data[k/2]):
                self._swap(k, k/2)
                k = k/2
            else:
                return

    # k is the index of the item that has to swim down
    def _sink(self, k):
        si = self._getSinkIndex(k)
        while (si is not None):
            self._swap(k, si)
            k = si
            si = self._getSinkIndex(k)

    def _heapify(self):
        k = self.last/2
        while (k >=1):
            self._sink(k)
            k -=1

    def insert(self, item):
        self.data.append(item)
        self.last += 1
        self._swim(self.last)

    def insert2(self, item):
        self.data.insert(1, item)
        self.last += 1
        self._sink(1)

if (len(sys.argv) > 1):
    bh = BH(sys.argv[1:])
else:
    inList = []
    for i in xrange(12):
        x = random.randint(10, 100)
        inList.append(x)

    bh = BH(inList)
