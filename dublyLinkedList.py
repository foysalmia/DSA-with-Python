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

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            if tmp.value == self.tail.value:
                print(tmp.value)
            else:
                print(tmp.value,"<=> ",end="")
            tmp = tmp.next


dubly_linked_list = DublyLinkedList(1)
dubly_linked_list.append(2)
dubly_linked_list.print_list()