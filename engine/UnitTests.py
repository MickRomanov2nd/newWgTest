from engine import Circle
from engine.Engine2D import Engine2D
from engine import Rectangle
from engine import Triangle


def test_engine2d():
    engine = Engine2D()
    engine.add_shape(Circle(0, 0, 5))
    engine.add_shape(Triangle(0, 0, 2, 0, 1, 1))
    engine.add_shape(Rectangle(0, 0, 3, 4))
    engine.set_color("red")
    engine.add_shape(Circle(1, 1, 2))
    engine.draw()


def test_circle():
    circle = Circle(0, 0, 5)
    circle.set_color("blue")
    circle.draw()


def test_triangle():
    triangle = Triangle(0, 0, 2, 0, 1, 1)
    triangle.set_color("green")
    triangle.draw()


def test_rectangle():
    rectangle = Rectangle(0, 0, 3, 4)
    rectangle.set_color("yellow")
    rectangle.draw()
