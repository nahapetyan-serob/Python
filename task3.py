print ("Which Fibonacci number you want to know")
n = int (input())
def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonachi(n-2) + fibonachi (n-1)
print (fibonachi(n))
