sheep_szs=[5,7,300,90,24,50,75]
biggest = 0
n = 0
total = 0
more_biggest = 0
print("Hello, my name is Hiep and these are my sheep sizes\n",sheep_szs)
for i in sheep_szs:
    if biggest < i:
        biggest = i
sheep_szs[sheep_szs.index(biggest)] = 8
print("Now my biggest sheep has size ",biggest," lest's shear it")
print("After shearing, here is my flock\n",sheep_szs)
while n<2:
    print("MONTH ",n+1,":")
    n+=1
    for up_size in sheep_szs:
        sheep_szs[sheep_szs.index(up_size)] = (sheep_szs[sheep_szs.index(up_size)] + 50)
    print("One month has passes, now here is my flock\n",sheep_szs)
    for j in sheep_szs:
        if more_biggest < j:
            more_biggest = j
    sheep_szs[sheep_szs.index(more_biggest)] = 8
    print("Now my biggest sheep has size ",more_biggest," lest's shear it")
    print("After shearing, here is my flock\n",sheep_szs)
print("MONTH ",n+1,":")
for up_size in sheep_szs:
    sheep_szs[sheep_szs.index(up_size)] = (sheep_szs[sheep_szs.index(up_size)] + 50)
print("One month has passes, now here is my flock\n",sheep_szs)
for i in sheep_szs:
    total = (total + i)
print("My flock has size in total: ",total,"\nI would get ",total," * 2$ = ",(total*2),"$")
