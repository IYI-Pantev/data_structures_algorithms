class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0


    def partition_list(self, x):
        dumy1 = Node(0)
        prev1 = dumy1
        dumy2 = Node(0)
        prev2 = dumy2

        current = self.head
        while current is not None:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        
        prev1.next = dumy2.next
        self.head = dumy1.next

my_ll = LinkedList(3)
my_ll.append(1)
my_ll.append(4)
my_ll.append(2)
my_ll.append(5)

my_ll.print_list()
print('--------')
my_ll.partition_list(3)
my_ll.print_list()