class Node:
    """A node in the linked list for chaining."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  # Update the value if key already exists
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        """Search for a value by its key in the hash table."""
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next

        return False

    def __repr__(self):
        """String representation of the hash table."""
        result = []
        for i, node in enumerate(self.table):
            items = []
            current = node
            while current:
                items.append(f"{current.key}: {current.value}")
                current = current.next
            result.append(f"{i}: " + " -> ".join(items))
        return "\n".join(result)

# Example usage
hash_table = HashTable()

# Inserting key-value pairs
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("cherry", 3)
hash_table.insert("banana", 4)  # Updating value for key "banana"

# Searching for keys
print(hash_table.search("banana"))  # Output: 4

# Deleting a key
hash_table.delete("banana")
print(hash_table.search("banana"))  # Output: None

# Printing the hash table
print(hash_table)
