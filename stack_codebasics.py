from collections import deque
from queue import LifoQueue
# stack using deque and to do this job collections is imported
stack = deque()
stack.append(4)
stack.append(2)
stack.append(5)
stack.append(3)
print('max = ', max(stack))
print(stack)
stack.pop()
print(stack)
stack.pop()
# to check stack is empty or not
print(not stack)
# to check top element of the stack
print('Top element = ', stack[-1])

# stack using list
fruits = ['mango', 'banana', 'orange']
print(fruits.pop())
print(fruits)

# next is creating stack from queue module
# in this case to push we have to use put method and to pop we have to get method
stack2 = LifoQueue()
stack2.put('dhaka')
stack2.put('khulna')
stack2.put('new york')
stack2.put('california')
print(stack2)



