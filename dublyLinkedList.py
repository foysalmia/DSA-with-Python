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

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

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
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = tmp.next
            self.head.prev = None
            tmp.next = None
        self.length -= 1
        return tmp

    def pop(self):
        if self.length == 0:
            return None
        tmp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tmp.prev
            self.tail.next = None
            tmp.prev = None
        self.length -= 1
        return tmp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.length-1,index,-1):
                tmp = tmp.prev
        return tmp

    def set_value(self,index,value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        before.next = new_node
        new_node.next = after
        after.prev = new_node

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
dubly_linked_list.append(3)
dubly_linked_list.prepend(0)
dubly_linked_list.print_list()
dubly_linked_list.insert(4,5)
dubly_linked_list.print_list()