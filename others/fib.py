
def fib1(n):# write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(a, end=' ')
        a, b = b,a+b
    print( )
def fib2(n):# return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(a)
        a,b = b, a+b
    return result
s = 133
print(str(s))