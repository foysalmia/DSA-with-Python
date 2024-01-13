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
        return tmp
    
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
        tmp = self.get(index-1)
        new_node.next = tmp.next
        tmp.next = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index - 1)
        tmp = prev.next
        prev.next = tmp.next
        tmp.next = None
        return tmp

    def reverse(self):
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        after = tmp.next
        before = None
        while tmp:
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next == None:
                print(temp.value)
            else:
                print(temp.value,end='->')
            temp = temp.next
