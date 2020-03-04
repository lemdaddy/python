def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return(number)
    elif number % 2 == 1:
        number = number * 3 + 1
        print(number)
        return(number)

number = input('enter a number')
number = int(number)
collatz(number)
if number == 1:
    print('finished!')






