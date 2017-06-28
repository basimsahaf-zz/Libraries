class SegTree:
    """ A class that implements a segment tree."""
    

    def __init__(self, inputList):

        self.N = len(inputList)
        self.segTree = [0] * ( 4 * len(inputList))
        self._build( inputList, 0, len(inputList)-1, 1)

    def query(self, x, y):

        """ A function that queries the segment tree to check the sum of a range of indices

        input : 2 indices, x and y lying inside the input list
        output : an integer representing the sum"""

        assert x <= y < self.N

        return self._query(0, self.N-1, 1, x, y)

    def update(self, x, y):

        """ A function that updates the index x, increasing it by y

        input : an index x, smaller than the size of the input array and how much to increase it by, y
        output : void"""

        assert x <=y < self.N
        
        return self._update(0, self.N-1, 1, x, y)

    def _build(self, inputList, L, R, v):

        if(L==R):
            self.segTree[v] = inputList[L]
        else:

            mid = (L+R)//2
            self._build(inputList, L, mid, 2*v)
            self._build(inputList, mid+1, R, 2*v+1)

            self.segTree[v] = self.segTree[2*v] + self.segTree[2*v+1]

    def _query(self, L, R, v, x, y):
        
        if R < x or L > y:
            return 0
        
        elif x <= L <= R <= y:
            # import pdb
            # pdb.set_trace()
            return self.segTree[v]
        else:
            mid = (L+R)//2
            return self._query(L, mid, 2*v, x, y) + self._query(mid+1, R, 2*v+1, x, y)

    def _update(self, L, R, v, x, y):

        if L==R:
            self.segTree[v]+=y
        else:
            mid = (L+R)//2
            self._update(L,mid,2*v,x,y)
            self._update(mid+1,R,2*v+1,x,y)
            self.segTree[v] = self.segTree[2*v] + self.segTree[2*v+1]

def main():

    print("\nThis is an interface for testing the Segment Tree class implementation")
    print("Please enter a space separated list of integers to be used as input\n")
    
    inp = list(map(int,input().split()))
    st = SegTree(inp)

    print("\nEnter the number of queries/updates:\n")
    M = int(input())
    print("\nEnter your queries/updates:\n")
    for i in range(M):
        inp = input().split()
        if(inp[0]=="query"):
            print(st.query(*(list(map(int, inp[1:])))))
        else:
            st.update(*(list(map(int, inp[1:]))))

if __name__ == "__main__":
    main()



# CREDITS:

# This code is heavily influenced from this link : http://algosaur.us/segment-tree/
# Note that I have not explored lazy propagation for traversing the segment tree yet.
# TODO: Make update function more explicit such that the user can see the changes
# TODO: Implement Lazy Propagation
# TODO: Get some sleep :p




