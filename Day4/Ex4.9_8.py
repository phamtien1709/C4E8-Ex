def area_of_circle(r):
    from math import pi
    a = round((pi* r**2),2)
    return a
while True:
    radius = float(input("Radius?\t"))
    print(area_of_circle(radius))  
