import turtle, time

turtle.title('거북아 놀자')

tt = turtle.Turtle()
tt.color('red')
tt.pensize(3)


for i in range(4):
        for j in range(8):
                tt.circle(30)
                tt.penup()
                tt.left(45)
                # tt.goto(60,-60)
                tt.pendown()


        # for j in range(8):
        #         tt.pendown()
        #         tt.forward(30)
        #         # tt.penup()
        #         tt.left(45)
        #         tt.pendown()
        #         tt.circle(30)
        tt.penup()
        tt.goto (60,-60)
        tt.pendown()

    # for i  in range(4):
    #     tt.forward(100)
    #     tt.left(90)

    # tt.penup()
    # tt.goto (50,-50)
    # tt.pendown()
    # tt.penup()
# tt.goto (100,-100)

# tt.circle(50)
time.sleep(2)

