from turtle import *

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(90)


penup()
goto(-200,0)
pendown()
color("purple")

left(120)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
color("purple")
left(90)
forward(70)
right(90)

penup()
goto(-200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



speed(2)
penup()
goto(300,300)
pendown()
color("yellow")
begin_fill()
circle(30)
end_fill()
exitonclick()