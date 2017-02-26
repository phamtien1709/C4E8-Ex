clothes_1 = ["Jeans", "T-Shirt", "Skirt","T-Shirt","Skirt","T-Shirt",]
find_list = ["jeans","hoody","bra"]
#function
def find(find_list):
    for i in find_list:
        n=count_item(clothes_1,i)
        print("Number of {0}:\t {1}".format(i,n), end="")
        if n < 5:
            print("\tBuy more!")
        else:
            print("\tSale off!")
def count_item(clothes_1, item):
    count = 0
    for cloth in clothes_1:
        if cloth.lower() == item.lower():
            count +=1
    return count
find(find_list)


##def print_clothes(clothes):
##    for index in range(len(clothes)):
##        print(clothes[index], end = "")
##        if index != len(clothes) - 1:
##            print(", ", end = "")
##        else:
##            print()   
##def shop(clothe):
##    while True:
##        choice = input("What do you want (CRUD)?")
##        if choice.upper() == "D":
##            position = int(input("Position?")) - 1
##            print(position)
##            del clothe[position]
##            print_clothes(clothe)
##        elif choice.upper() == "C":
##            new_cloth = input("New item?")
##            clothe.append(new_cloth)
##            print_clothes(clothe)
##shop(clothes_1)
