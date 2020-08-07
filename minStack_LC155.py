# ///
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# ///
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minEle = float('inf')
        self.stackList = []
        self.stackList2 = []
    def push(self, x: int) -> None:
        self.stackList2.append(x)
        if len(self.stackList)==0:
            self.minEle = x
            self.stackList.append(x)
            return;
        if x<self.minEle:
            self.stackList.append(2*x-self.minEle)
            self.minEle = x
        else:
            self.stackList.append(x)
        

    def pop(self) -> None:
        self.stackList2.pop()
        topEle = self.stackList[-1]
        if(topEle>self.minEle):
            self.stackList.pop()
        else:
            self.minEle = (2*self.minEle)-topEle
            self.stackList.pop()

    def top(self) -> int:
        return self.stackList2[-1]

    def getMin(self) -> int:
        return self.minEle
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()