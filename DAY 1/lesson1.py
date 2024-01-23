from turtle import *
#we want to paint a house
setup(width = 600,height=600, startx= None, starty= None )
color("pink")
#step 1: draw a square
width(5)
 
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door 
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120) # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()

goto(200, 200)
pendown()




#drawing a window


begin_fill()
color("pink")
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(30)
forward(60)
left(90)
forward(50)
left(90)
forward(35)

left(90)
forward(50)
right(90)
penup()
goto(200,200)
pendown()
color("pink")
forward(5)
left(180)
forward(65)
right(90)
forward(50)

right(90)
forward(35)
right(90)
forward(45)
end_fill()
exitonclick()
 




