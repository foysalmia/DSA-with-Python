class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DublyLinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            if tmp.value == self.tail.value:
                print(tmp.value)
            else:
                print(tmp.value,"<=>",end="")
            tmp = tmp.next


dubly_linked_list = DublyLinkedList(1)
dubly_linked_list.print_list()