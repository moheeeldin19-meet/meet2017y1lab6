import turtle
##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('square')
##triangle=square.clone()
##triangle.shape('triangle')
UP_ARROW = "Up"
LEFT_ARROW="Left"
RIGHT_ARROW="Right"
DOWN_ARROW="Down"
SPACEBAR="space"
UP=0
DOWN=1
RIGHT=2
LEFT=3
direction=UP

def up():
    global direction
    direction = Up
    print("you pressed up")
    if direction==Up:
        turtle.goto(x,y+10)
    print(turtle.pos())

def down():
    global direction
    direction=Down
    print("you pressed down")
    x=old_pos[0]
    y=old_pos[1]
    if direction==Down:
        turtle.goto(x,y-10)
        print(turtle.pos())
    
def right():
    global direction
    direction=Right
    print("you pressed right")
    x=old_pos[0]
    y=old_pos[1]
    if direction==Right:
        turtle.goto(x+10,y)
        print(turtle.pos())


def left():
    global direction
    direction=LEFT
    print("you pressed left")
    x=old_pos[0]
    y=old_pos[1]
    if direction==Left:
        turtle.goto(x-10,y)
        print(turtle.pos())


def space():
    global direction
    print("you pressed space")
    x=old_pos[0]
    y=old_pos[1]
    if direction== space:
        turtle.stamp()
    
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(space,SPACEBAR)
old_pos=turtle.pos()

print(turtle.pos())
turtle.listen()    
