f = open("alice_words.txt","r")
text = f.read().lower().split()
def count(buon_ngu_qua):
    count = 0
    for dem_roi in buon_ngu_qua:
        if dem_roi.lower() == "alice":
            count +=1
    return count
def find_alice():
    print("Word\t\tCount")
    print("==================")
    print("{0}\t\t{1}".format("alice",count(text)))
find_alice()
    
