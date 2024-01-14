class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            if tmp.next == None:
                print(tmp.value)
            else:
                print(tmp.value,"=> ",end="")
            tmp = tmp.next

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp


my_new_stack = Stack(1)
my_new_stack.push(2)
my_new_stack.push(3)
my_new_stack.push(4)
my_new_stack.print_stack()
print("Top::>",my_new_stack.top.value)
my_new_stack.pop()
my_new_stack.print_stack()
print("Top::>",my_new_stack.top.value)


            