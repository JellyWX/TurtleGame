import turtle
from Element import Element

e = Element(scale=100)
e.from_file('obj.tur')

e.draw()

#e.shift((2,2))

#e.draw()

e.rotate(45)
e.draw()

turtle.exitonclick()
