print ("Enter your number")
num = int (input())
sum = 0
modulo = 0
while num > 0:
    modulo = num % 10
    sum += modulo
    num = num // 10
print (sum)
