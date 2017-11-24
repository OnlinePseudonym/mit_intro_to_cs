def isIn(char, aStr):
    if len(aStr) <= 1:
        if char == aStr:
            return True
        return False
    else:
        mid = int(len(aStr)/2)
        test = aStr[mid]
        if char == test:
            return True
        elif char > test:
            return isIn(char, aStr[mid:])
        else:
            return isIn(char, aStr[:mid])

strA ='abcdefghijklmnopqrstuvwxyz'
print(isIn('e', strA))
