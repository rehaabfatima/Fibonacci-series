def recur_fibonacci(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n ==2:
        return[0,1]
    else:
        fib_series=recur_fibonacci(n - 1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series


n= int(input("Enter the length of Fibonacci series : "))
if n<=0:
    print("Please enter a positive number")
else:
    print(recur_fibonacci(n))


    