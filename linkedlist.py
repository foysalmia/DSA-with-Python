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
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node 
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        if self.length == 0:
            self.tail = None

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

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(0,index):
            tmp = tmp.next
        return tmp.value

    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.value)
            else:
                print(temp.value,end='->')
            temp = temp.next


first_linked_list = LinkedList(2)
first_linked_list.append(3)
print("Before Prepend".center(20))
print("Head = ",first_linked_list.head.value)
print("Tail = ",first_linked_list.tail.value)
print("Length = ",first_linked_list.length)
print("Linked List => ", end="")
first_linked_list.print_list()


print("After Prepend".center(20))
first_linked_list.prepend(5)
print("Head = ",first_linked_list.head.value)
print("Tail = ",first_linked_list.tail.value)
print("Length = ",first_linked_list.length)
print("Linked List => ", end="")

first_linked_list.append(10)
first_linked_list.append(19)
first_linked_list.append(12)
first_linked_list.print_list()
print("Index 0 ::>",first_linked_list.get(10))