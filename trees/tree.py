class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

my_binary_search_tree = BinarySearchTree()
my_binary_search_tree.insert(10)
my_binary_search_tree.insert(5)
my_binary_search_tree.insert(15)
print(my_binary_search_tree.root.value)
print(my_binary_search_tree.root.left.value)
print(my_binary_search_tree.root.right.value)
print(my_binary_search_tree.contains(5))