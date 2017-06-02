class  stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class TestStack(object):

    def TestClient(self):
        s = stack()
        assert(s.isEmpty()==True)
        s.push(1)
        assert(s.isEmpty()==False)
        s.pop()
        assert(s.isEmpty()==True)
        s.push(2)
        assert(s.peek()==2)
        s.push(1)
        assert(s.size()==2)
        print("Implementation is sorrect")

stackObject = TestStack()
stackObject.TestClient()
