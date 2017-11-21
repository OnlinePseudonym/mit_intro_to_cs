prev = ''
string = ''
longest = ''

for e in s:
    if e >= prev:
        string += e
        if len(string) > len(longest):
            longest = string
    else:
        string = e
    prev = e
print(longest)
