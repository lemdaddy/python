import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
#ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break #this condition means correct guess

if guess == secretNumber:
    print('good job, you guessed the number in ' + str(guessesTaken) + 'guesses!')
else:
        print('Nope. The number i was thinking of was ' + str(secretNumber))
