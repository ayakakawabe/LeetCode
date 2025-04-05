#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.stack=[]
        self.length=0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length=self.length+1

    def pop(self) -> int:
        if self.length!=0:
            self.length=self.length-1
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if self.length!=0:
            return self.stack[self.length-1]
        else:
            return None

    def empty(self) -> bool:
        if self.length==0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

