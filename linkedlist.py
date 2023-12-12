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
    
    def pop(self):
        if self.length == 0:
            return None
        tmp = self.head
        pretmp = self.head
        while tmp.next:
            pretmp = tmp
            tmp = tmp.next
        self.tail = pretmp
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.value)
            else:
                print(temp.value,end='->')
            temp = temp.next

first_linked_list = LinkedList(4)


first_linked_list.pop()
first_linked_list.print_list()
print("length = ",first_linked_list.length)

print("head = ",first_linked_list.head)
print("tail = ",first_linked_list.tail)