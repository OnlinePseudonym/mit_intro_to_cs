target = 'bob'
count = 0

for i in range(len(s)):
    if target in s[i:i+3]:
        count += 1
print('Number of times bob occurs is: ' + str(count))
