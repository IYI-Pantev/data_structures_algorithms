class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]
        return None

    def keys(self):
        keys_list = []
        for item in self.data_map:
            if item is not None:
                for i in item:
                    keys_list.append(i[0])
        if len(keys_list) > 0:
            return keys_list
        return None

my_hashtable = HashTable()
# print(list(enumerate(my_hashtable.data_map)))
# my_hashtable.print_table()
print('- - - - - -')
my_hashtable.set_item('bolts', 1400)
my_hashtable.set_item('washers', 50)
my_hashtable.set_item('lumber', 70)
my_hashtable.print_table()
# print(my_hashtable.get_item('washers'))
# print(my_hashtable.get_item('nuts'))

print(my_hashtable.keys())