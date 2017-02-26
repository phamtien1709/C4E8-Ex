from turtle import *
pensize(3)
bgcolor("lightgreen")
color("hotpink")
tess = True
def draw_poly(n,sz):
    for i in range(n):
        fd(sz)
        lt(360/n)
draw_poly(3,50)
input()
