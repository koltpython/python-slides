import turtle  
def draw_sqr(t,x,y,length):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    k = 0
    while k<4:
        t.forward(length) 
        t.right(90) 
        k+=1

my_turtle = turtle.Turtle()
i = 0 
x = -200
y = -200
length = 50
while(i<9):
    draw_sqr(my_turtle,x,y,length)
    x+=length
    i+=1
turtle.done() 