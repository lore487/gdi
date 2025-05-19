import turtle

# Imposta lo schermo
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Disegno 'you'")
pen = turtle.Turtle()
pen.speed(1)  # Imposta la velocità di disegno (1 è la più lenta, 6 è normale, 0 è la più veloce)
pen.penup()
pen.goto(-100, 0)
pen.pendown()

# Disegna la 'y'
pen.left(75)
pen.forward(50)
pen.backward(50)
pen.right(150)
pen.forward(50)
pen.penup()
pen.goto(-50, 0)
pen.pendown()

# Disegna la 'o'
pen.circle(25)
pen.penup()
pen.goto(25, 0)
pen.pendown()

# Disegna la 'u'
pen.left(90)
pen.forward(50)
pen.circle(25, 180)
pen.forward(50)

screen.mainloop()