#Em ngai Enter lam :3 anh deo kinh lup vao nhe :*

clothes=["T-Shirt","Sweater"]
while True:
    a = input("Welcome to our shop, what do you want?(C,R,U,D,S)\n(Or E to exit...Don't S!)")
    if a=="c" or a=="C":
        new_clothe=input("New item?")
        clothes.append(new_clothe)
        print("Our items:",end="")
        for j in range (len(clothes)):
            print("\t",clothes[j],"\t ",end="")
    elif a=="r" or a=="R":
        print("Our items:",end="")
        for i in range (len(clothes)):
            print("\t",clothes[i],"\t ",end="")
    elif a=="u" or a=="U":
        b=int(input("Update position?"))
        if b in range(len(clothes)):
            new_clothe=input("New item?")
            clothes[b] = new_clothe
            print("Our items:",end="")
            for k in clothes:
                print("\t",k,"\t ",end="")
        else:
            print("Don't have anything in here!")
            continue
    elif a=="D" or a=="d":
        c=int(input("Delete position?"))
        if c in range(len(clothes)):
            clothes.pop(c)
            print("Our items:",end="")
            for m in clothes:
                print("\t",m,"\t ",end="")
        else:
            print("Don't have anything in here!")
            continue        
    elif a=="E" or a=="e":
        print("See you later!!")
        break
    else:
        continue
    print()
