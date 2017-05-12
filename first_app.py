print('How old do you thing Fred the Chicken is?')
number = 17

run = True
while run:

    guess = int(input('Enter What You Think His Age Is....t'))

    if guess == number:
        print('Yes :D That is his age...')
        run = False
    elif guess < number:
        print('No, Guess a little higher...')
    elif guess > number:
        print('No, Guess a little lower....')

    if run == False:
        print('Game Over')
        choice = input('Press Q to Quit')
        if choice == 'q':
            break