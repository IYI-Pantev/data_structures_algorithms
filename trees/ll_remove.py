class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return True
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        return True
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def remove(self, kth):
        if kth < 1:
            return None
        temp = self.head
        if kth == 1:
            rm = temp.next
            temp.next = temp.next.next
            rm.next = None
        temp = self.head
        for _ in range(kth - 2):
            temp = temp.next
        rm = temp.next
        temp.next = temp.next.next
        rm.next = None

    def insert(self, value, index):
        node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        return True

    def reverse(self):
        prev = None
        temp = self.head
        after = None
        while temp:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after

        self.head = prev
    

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print_list()
print('--- removing 3rd element ---')
my_list.remove(3)
my_list.print_list()
print('--- inserting at 2nd index ---')
my_list.insert(3, 2)
my_list.print_list()
print('<== reversing linked list')
my_list.reverse()
my_list.print_list()
