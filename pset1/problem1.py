vowels=['a','e','i','o','u']
count=0

for e in s:
    if e in vowels:
        count += 1

print('Number of vowels: ' + str(count))
