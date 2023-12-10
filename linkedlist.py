class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.value)
            else:
                print(temp.value,end='->')
            temp = temp.next

first_linked_list = LinkedList(4)
print("head = ",first_linked_list.head.value)
print("tail = ",first_linked_list.tail.value)
print("length = ",first_linked_list.length)
first_linked_list.print_list()