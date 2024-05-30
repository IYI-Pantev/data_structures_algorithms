class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.top is None:
            return None
        before = self.top
        self.top = self.top.next
        before.next = None
        self.height -= 1
        return before
    
my_stack = Stack(2)
my_stack.push(1)
my_stack.push(3)
my_stack.push(4)
my_stack.print_stack()
print('- - - - - - ')
my_stack.pop()
print('after stack top is popped')
print('stack top is:', my_stack.top.value)