import turtle, random, time

# Note that each "pixel" is 20x20 pixels (MAKE SURE ITS AN INTEGER)
width = 26
height = 20

pixels = []

screen = turtle.Screen()
screen.setup(width * 20, height * 20)
screen.tracer(0)

class Pixel:
    def __init__(self, posx, posy):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.pu()
        self.turtle.shape("square")
        self.turtle.goto(posx, posy)
    
    def color(self, col): self.turtle.color(col)

for i in range(height):
    for o in range(width):
        pixels.append(Pixel((o - (width / 2)) * 20 + 10, (i - (height / 2)) * 20 + 10))

turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"] # Colors for the turtle

h = 0
while True:
    for i in range(len(pixels)): pixels[i].color(turtleColors[(i + h) % 9])
    h += 1
    #time.sleep(0.1)
    screen.update()
