class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

class TestingDoubleQueue(object):

    def Client(self):
        q = Queue2Stacks()
        for i in xrange(0,5):
            q.enqueue(i)
        for i in xrange(0,5):
            assert(q.dequeue()==i)
        print("All Test Cases Correct")

q = TestingDoubleQueue()
q.Client()
