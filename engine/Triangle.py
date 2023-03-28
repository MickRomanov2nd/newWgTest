from engine.Shape import Shape


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self):
        print(f"Drawing Triangle: ({self.x}, {self.y}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}) in {self.color} color")
