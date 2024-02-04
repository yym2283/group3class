from turtle import Screen,Turtle
hexa_color = input("Enter the color of hexagon:hexa_color=")
circle_color = input("Enter the color of circle:cir_color=")
square_color = input("Enter the color of square:square_color=")
border_color = input("Enter the color of border:border_color=")
sc= Screen()
turta= Turtle()
sc.title("Group 3: Acitivity 1")
sc.bgcolor("purple")
turta.speed(10)

def hexagon(hexa_color, border_color):
    turta.pencolor(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()

   
def square(square_color, border_color):
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()
    
   
def circle(circle_color, border_color):
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()
def setPos(x, y):
    turta.penup()
    turta.setheading(0)
    turta.goto(x, y)
    turta.pendown()

 
def pattern(hexa_color, square_color,circle_color, border_color):
    
    setPos( x= -200, y = 100)
    hexagon( hexa_color, border_color)
    setPos( x= -85, y = -30)
    hexagon( hexa_color, border_color)
    setPos( x= 15, y = -160)
    hexagon( hexa_color, border_color)

    
    setPos( x= -50, y = 100)
    circle(circle_color, border_color)
    setPos(x= 65, y = -30)
    circle( circle_color, border_color)
    setPos( x= 165, y = -160)
    circle( circle_color, border_color)

    setPos( x=25 , y = 100)
    square( square_color, border_color)
    setPos(x= 140, y = -30)
    square( square_color, border_color)
    setPos( x= 240, y = -160)
    square( square_color, border_color)


def main():
    pattern( hexa_color, square_color, circle_color, border_color)
    turta.hideturtle()
main()
sc.exitonclick()


