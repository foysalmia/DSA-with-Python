class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        tmp = self.first
        while tmp is not None:
            if tmp.next == None:
                print(tmp.value)
            else:
                print(tmp.value,"=> ",end="")
            tmp = tmp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True 

    def dequeue(self):
        if self.length == 0:
            return None
        tmp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        tmp.next = None
        self.length -= 1
        return tmp


