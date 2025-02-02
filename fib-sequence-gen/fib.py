def fib_seq(n):
    if (n <=1): 
        return n #stoping cond = if n < 2, returns n
    else:
        return fib_seq(n-2) + fib_seq(n-1) # fib formula = (n-2) + (n-1)

number = fib_seq(0)
print(number)