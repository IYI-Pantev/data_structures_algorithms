class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        before = self.head
        while before is not None:
            print(before.value)
            before = before.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0: # self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        before = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
             self.tail = self.tail.prev
             self.tail.next = None
             before.prev = None
        self.length -= 1
        return before
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        before = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            before.next = None
        self.length -= 1
        return before
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        before = self.head
        if index < self.length / 2:
            for _ in range(index):
                before = before.next
        else:
            before = self.tail
            for _ in range(self.length - 1, index, -1):
                before = before.prev
        return before
    
    def set_value(self, index, value):
        before = self.get(index)
        if before is not None:
            before.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
 
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
 
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        removed = self.get(index)
        before = removed.prev
        after = removed.next
        
        before.next = after
        after.prev = before
        removed.prev = None
        removed.next = None
        
        self.length -= 1
        return removed

my_dll = DoublyLinkedList(7)
my_dll.append(8)
my_dll.append(9)
my_dll.prepend(10)
my_dll.print_list()
print('- - - - - -')
# my_dll.pop()
# my_dll.print_list()
print(my_dll.get(2))



