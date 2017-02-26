from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for col in colors:
    begin_fill()
    color(col)
    for i in range(2):
        fd(50)
        left(90)
        fd(100)
        left(90)
    fd(50)
    end_fill()
