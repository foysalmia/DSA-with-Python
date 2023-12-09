class Cokie:
    def __init__(self,color) -> None:
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color


cokie1 = Cokie("Green")
print(f"cokie1 color {cokie1.get_color()}")
cokie1.set_color("Yello")
print(f"cokie1 changed color is {cokie1.get_color()}")