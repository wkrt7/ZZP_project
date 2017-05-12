

run = True
while run:
    print('Choose an option')
    print('MENU:\nq -quit\na - add\n')
    guess = input('Enter What You Think His Age Is....t')

    if guess == 'q':
        run = False
        print('Good bye!\n')
    elif guess == 'a':
        print('added\n')
    else:
        print('No such option - insert new character')