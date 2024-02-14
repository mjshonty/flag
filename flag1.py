from turtle import *

#speed(0)

teleport(-300,175) #set inital position of turtle

#start creation of rectangle for flag

pencolor("blue") #outline color
fillcolor("blue") #fill color

begin_fill()


right(90)
forward(300)
    
left(90)
forward(500)

left(90)
forward(300)
    
left(90)
forward(500)
end_fill()

#draw triangle in upper left corner
teleport(-75, -20)


setheading(300)

pencolor("orange")
fillcolor("orange")


begin_fill()

for i in range(0,6): #loop to draw 6 diamonds in a roundish shape
    right(60)
    forward(30)

    right(60)
    forward(30)

    right(120)
    forward(30)

    right(60)
    forward(30)

    penup()
    forward(50)
    pendown()
    

end_fill()

hideturtle()

done()
