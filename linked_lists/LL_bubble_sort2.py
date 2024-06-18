class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def swap(self, node1, node2):
        if node1 == self.head:
            prev = None
        else:
            prev = self.head
            while prev.next != node1:
                prev = prev.next

        ptr1 = node1
        ptr2 = node2
        if prev != None:
            ptr1.next = ptr2.next
            ptr2.next = ptr1
            prev.next = ptr2
        else:
            ptr1.next = ptr2.next
            ptr2.next = ptr1
            self.head = ptr2

    #changing with swapping the nodes
    def bubble_sort(self):
        current = self.head
        for i in range(self.length - 1, 0, -1):
            current = self.head
            for _ in range(i):
                if current.value > current.next.value:
                    self.swap(current, current.next)
                    continue
                current = current.next

        return

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()
# my_linked_list.swap(my_linked_list.head, my_linked_list.head.next)
my_linked_list.bubble_sort()
print('-------')
print("\nSorted Linked List:")
my_linked_list.print_list()

# print('-------')
# print(my_linked_list.head.value)


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

