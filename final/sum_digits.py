def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    n = 0
    c = 0
    for e in s:
        try:
            n += int(e)
            c += 1
        except:
            pass
    if c == 0:
        raise ValueError('No digits in input')
    return n

print(sum_digits("a;d"))