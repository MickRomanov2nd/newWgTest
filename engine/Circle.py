from engine.Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in {self.color} color")
