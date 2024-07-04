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
    
    def maxDepth(self):
        height = 0
        def traverse(node):        
            if node is None:
                return 0
            else:
                left_depth = traverse(node.left)
                right_depth = traverse(node.right)
                return max(left_depth, right_depth) + 1
        height = traverse(self.root)
        return height

    

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.maxDepth())