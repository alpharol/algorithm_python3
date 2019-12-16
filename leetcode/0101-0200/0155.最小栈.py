#https://leetcode-cn.com/problems/min-stack/

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.data = []

    def push(self, x: int) -> None:
        stack = self.stack.append(x)
        mindata = self.data
        if len(mindata) == 0:
            mindata.append(x)
        else:
            if mindata[-1] < x:
                pass
            else:
                mindata.append(x)

    def pop(self) -> None:
        stack = self.stack
        mindata = self.data
        tmp = stack[-1]
        stack.pop(-1)
        if mindata[-1] == tmp:
            mindata.pop(-1)


    def top(self) -> int:
        stack = self.stack
        return stack[-1]

    def getMin(self) -> int:
        mindata = self.data
        return mindata[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    #print(minStack.top())
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())



