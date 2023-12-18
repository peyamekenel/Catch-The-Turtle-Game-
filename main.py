import turtle
import random
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle Game")
FONT = ('Arial', 30, 'normal')
score_turtle = turtle.Turtle()
countdownTurtle=turtle.Turtle()
turtle_list=[]
score=0
game_over=False
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("purple")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)
grid_size=10
x_cords=[-20,-10,0,10,20]
y_cords=[20,10,0,-10]
def make_turtle(x,y):
    t=turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)
    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

        #print(x,y)
    t.onclick(handle_click)

def setup_turtles():
    for x in x_cords:
        for y in y_cords:
            make_turtle(x,y)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtles_ramdomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_ramdomly,1000)


def countDown(time):
    global game_over
    countdownTurtle.hideturtle()
    countdownTurtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdownTurtle.setpos(0, y-30)
    countdownTurtle.clear()
    if time>0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countDown(time-1),1000)
    else:
        game_over=True
        countdownTurtle.clear()
        hide_turtles()
        countdownTurtle.write(arg="Game Over!!", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_ramdomly()
    countDown(10)
    turtle.tracer(1)
start_game_up()
turtle.mainloop()