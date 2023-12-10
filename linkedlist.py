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
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node 
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.value)
            else:
                print(temp.value,end='->')
            temp = temp.next

first_linked_list = LinkedList(4)

first_linked_list.append(5)
first_linked_list.append(6)
first_linked_list.append(7)

print("head = ",first_linked_list.head.value)
print("tail = ",first_linked_list.tail.value)


first_linked_list.print_list()
print("length = ",first_linked_list.length)