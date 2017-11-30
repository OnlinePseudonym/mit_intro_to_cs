import math

def genPrimes():
    num = 2
    while True:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1