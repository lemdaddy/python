import random
import sys
print('hey wats ur name')
name = input()

print('hey ' + name + ' Im thinking of a number between one and twenty')
secretNumber = random.randint(1,20)
print('DEBUG: Number is ' + str(secretNumber))
try:    
    for guessesTaken in range(1, 7):
        print('take a guess')
        guess = int(input())
        if guess == secretNumber:
            print('You took ' +  str(guessesTaken) + ' attempts to guess it!')
            sys.exit()    
        elif guess > secretNumber:
            print('your guess is too high')
        elif guess < secretNumber:
            print('guess too low')
    print('You took too many tries, the number was ' + str(secretNumber))

except ValueError:
    print('You didnt enter a number')

