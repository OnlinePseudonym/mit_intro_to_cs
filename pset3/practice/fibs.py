def fib_faster(n):
    global numFibCalls
    numFibCalls += 1
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current

def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

d = {0:0, 1:1}

n = 36
numFibCalls = 0
print("fib_faster")
print(fib_faster(n))
print(numFibCalls)
numFibCalls = 0
print("fib_efficient")
print(fib_efficient(n, d))
print(numFibCalls)
numFibCalls = 0
print("fib")
print(fib(n))
print(numFibCalls)
