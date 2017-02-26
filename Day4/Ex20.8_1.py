find_list = ["a","b","c","d","e","f","g","h","i","j"
           ,"k","l","m","n","o","p","q","r","s","t"
           ,"u","v","w","x","y","z"]
def count(string,find_letter):
    count = 0
    for letter in string:
        if (letter.lower() == find_letter):
            count += 1
    return count
def find(find_here):
    for i in find_here:
        n = count(strg,i)
        if n > 0:
            print("{0}\t{1}".format(i,n))
strg = input("What is your string?\n")
find(find_list)
input()
