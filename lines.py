import turtle, random
arr = []
num = 9
for x in range(0,num):
    arr.append(turtle.Turtle())
    arr[x].speed(0)
while True:
    for x in range(0,num):
        arr[x].right({1:0,2:90,3:180,4:270}.get(random.randint(1,4)))
        arr[x].forward(35)
