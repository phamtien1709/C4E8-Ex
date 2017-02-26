from turtle import *
n=int(input("n="))
colors=["red","blue","brown","yellow","grey","pink","black"]
a=0
for i in range(3,n+1):
    color(colors[a])
    a+=1
    for j in range (i):
        left(360/i)
        forward(100)
