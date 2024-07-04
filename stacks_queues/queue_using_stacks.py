class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        
        if len(self.stack1) == 0:
            self.stack1.append(value)
            return
        # if len(self.stack1) == 1:

        for _ in range(len(self.stack1)):
            n = self.stack1.pop()
            self.stack2.append(n)
        
        self.stack1.append(value)
        for _ in range(len(self.stack2)):
            n = self.stack2.pop()
            self.stack1.append(n)


    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
