class deque(object):

    def __init__(self):
        self.items = []

    def addFront(self,k):
        self.items.insert(0,k)

    def addBack(self,k):
        self.items.insert(len(self.items),k)

    def removeFront(self):
        return self.items.pop(0)

    def removeBack(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items==[]

class TestingDeque(object):

    def Client(self):
        s = deque()
        assert(s.isEmpty()==True)
        s.addFront(1)
        assert(s.size()==1)
        s.addBack(2)
        assert(s.size()==2)
        s.addFront(0)
        assert(s.size()==3)
        s.removeFront()
        assert(s.size()==2)
        s.removeBack()
        assert(s.size()==1)
        s.removeFront()
        assert(s.size()==0)
        assert(s.isEmpty()==True)
        print("ALL TEST CASES PASSED")

t = TestingDeque()
t.Client()
