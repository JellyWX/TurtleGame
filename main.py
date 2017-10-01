import turtle
from Element import Element

e = Element(scale=100)
e.from_file('obj.tur')

e.draw()

turtle.exitonclick()
