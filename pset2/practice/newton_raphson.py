## General approximation algorithm to find roots of a polynomial in one
# variable
#      p(x) = a(sub n)x**n + a(sub n-1)x**n-1 + ... a(sub 1)x + a(sub0 0)

## Want to find r such that p(r) = 0

## For examplt, to find the square root of 24, find the root of p(x) = x**2 - 24

## Newton shows that if g is an approximation to the root, then
#                     g -p(g)/p'(g)
# is a better aprroximation; where p' is derivative of p

epsilon = 0.01
y = .50
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print ('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
