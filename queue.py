class queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,k):
        self.items.append(k)

    def serve(self):
        temp=self.items[0]
        self.items.pop(0)
        return temp

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

class TestQueue(object):

    def Client(self):
        s = queue()
        assert(s.isEmpty()==True)
        s.push(1)
        s.push(2)
        assert(s.isEmpty()==False)
        assert(s.size()==2)
        assert(s.peek()==1)
        assert(s.serve()==1)
        assert(s.isEmpty()==False)
        assert(s.peek()==2)
        assert(s.serve()==2)
        assert(s.isEmpty()==True)
        print("ALL TEST CASES PASSED")


#Testing queue
QueueObject = TestQueue()
QueueObject.Client()
