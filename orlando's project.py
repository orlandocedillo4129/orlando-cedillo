import turtle
turtle.colormode(255)#bringsin the color mode function

bob =turtle.Turtle()
bob.width(3)
bob.speed(30)
turtle.bgcolor(50,50,50) 
for times in range (400):
    bob.color(times,1,100)
    bob.forward(times*2+10)
    bob.right(250000)

