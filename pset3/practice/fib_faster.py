def fib_efficient(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after


print(fib_efficient(6))
