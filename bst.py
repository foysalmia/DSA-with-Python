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




my_bst = BinarySearchTree()
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)