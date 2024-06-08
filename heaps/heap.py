class MaxHeap: # withouth 0 index left empty
    def __init__(self):
        self.heap = []
        
    # helper methods
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]  
    
    def _sink_down(self, index):
        pass
        
    #  - - -
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
    
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:    
            self._swap(current, self._parent(current))
            current = self._parent(current)
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        
        return max_value

my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
print(my_heap.heap)

my_heap.insert(100)
print(my_heap.heap)

my_heap.insert(75)
print(my_heap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""