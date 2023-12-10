class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node.value
        self.tail = new_node.value
        self.length = 1

first_linked_list = LinkedList(4)
print("head = ",first_linked_list.head)
print("tail = ",first_linked_list.tail)
print("length = ",first_linked_list.length)