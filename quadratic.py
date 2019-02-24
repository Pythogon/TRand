import turtle, random
arr = []
num = 5
for x in range(0,num):
    arr.append(turtle.Turtle())
    arr[x].speed(0)
    arr[x].shape('circle')
    arr[x].penup()
while True:
    for x in range(0,num):
        arr[x].right(random.randint(1,359))
        arr[x].forward(5)
