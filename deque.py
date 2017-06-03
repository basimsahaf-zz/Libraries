""" A deque or a 'doubly ended queue' is a queue where you can add and remove from both ends."""
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

    def getFront(self):
    	return self.items[0]

    def getBack(self):
    	return self.items[len(self.items)-1]

    def printItems(self):
    	for index, item in enumerate(self.items):
    		if(index==0):
    			print 'Front: ', item
    		elif(index==len(self.items)-1):
    			print 'Back: ' , item
    		else:
    			print(item)
    	if(self.items==[]):
    		print 'Empty'
    	print("--------")

class TestingDeque(object):

    def Client(self):
        s = deque()
        assert(s.isEmpty()==True)
        s.addFront(1)
        s.printItems()
        assert(s.size()==1)
        assert(s.getFront()==1)
        s.addBack(2)
        s.printItems()
        assert(s.size()==2)
        assert(s.getBack()==2)
        s.addFront(0)
        s.printItems()
        assert(s.size()==3)
        assert(s.getFront()==0)
        s.removeFront()
        s.printItems()
        assert(s.size()==2)
        assert(s.getFront()==1)
        s.removeBack()
        s.printItems()
        assert(s.size()==1)
        assert(s.getBack()==1)
        s.removeFront()
        s.printItems()
        assert(s.size()==0)
        assert(s.isEmpty()==True)
        print("ALL TEST CASES PASSED")

t = TestingDeque()
t.Client()
