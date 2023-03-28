from engine.Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} in {self.color} color")
