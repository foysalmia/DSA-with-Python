class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        tmp = self.root
        while True:
            if tmp.value == new_node.value:
                return False
            if new_node.value < tmp.value:
                if tmp.left == None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right == None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right

    def contains(self,value):
        tmp = self.root
        while tmp is not None:
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            else:
                return True
        return False


my_bst = BinarySearchTree()
my_bst.insert(25)
my_bst.insert(30)
my_bst.insert(28)
my_bst.insert(32)
my_bst.insert(31)
print(my_bst.contains(31))
print(my_bst.contains(25))