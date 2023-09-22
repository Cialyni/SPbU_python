import random

def desclaimer():
    print('Hi! In this game I will guess a four-digit number from non-repeating digits, you will try to guess it.\nEach attempt is one four-digit number, to which I will answer you how many cows you guessed (the numbers are not in their positions) and bulls (the numbers are in their positions.\nI give you exactly 5 attempts, otherwise you lose')

def input_digit(attemp):
    print('This is your attemp №:', attemp)
    print('Input your four-digit number:')
    digit = input()
    return digit

def check(my_digit, digit):
    cows = bulls = 0
    for i, elem in enumerate(digit):
        if int(elem) in my_digit:
            cows += 1
        if int(digit[i]) == my_digit[i]:
            bulls += 1
    return cows - bulls, bulls
def game():
    my_digit = random.sample(range(10), 4)
    print(my_digit)
    attemp = 1
    while attemp <= 5:
        digit = input_digit(attemp)
        cows, bulls = check(my_digit, digit)
        if bulls != 4:
            print('Cows count: {}\nBulls count: {}'.format(cows, bulls))
        else:
            print('Congratulation!!!!\nYou WIN')
            return
        attemp += 1
    print('You lose, try better next time')


if __name__ == '__main__':
    desclaimer()
    game()
