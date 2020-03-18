def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return(number)
    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)
        return(number)

inputNumber = input('enter a number ')
number = int(inputNumber)
while number != 1:
    collatz(number)

else:
    print(number)
