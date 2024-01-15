class HashTable:
    def __init__(self,size = 7) -> None:
        self.data_map = [None] * size

    def _hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

    def set_item(self,key,value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get(self,key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

my_hash = HashTable(7)
my_hash.set_item('nuts',1400)
my_hash.set_item('pipe',1000)
my_hash.set_item('longs',500)
my_hash.print_table()
print(my_hash.get("mike"))