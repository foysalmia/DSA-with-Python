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


my_hash = HashTable(7)
my_hash.print_table()