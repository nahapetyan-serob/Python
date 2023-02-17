print ("Enter your x and y values")
x = int(input())
y = int(input())
numerator = x - y
if x + y == 0:
    print("You cannot divide to 0")
elif y > x:
    numerator = - numerator
    print (numerator / (x + y))
else: 
    print (numerator / (x + y))
