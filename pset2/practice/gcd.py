def gcdIter(a, b)
    test = a
        if a > b:
            test = b
        while b % test != 0 or a % test != 0:
            test -= 1
        return test
