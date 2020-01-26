# This is my very first Python program

print('Hello World')

year = '2018'
a = 'This is year ' + year

print(a)


def main():
    print(a)
    someNumber = 20
    userGuessedCorrectly = False
    print('Guess a number between 10 and 30..')

    while not userGuessedCorrectly:
        userEnteredNumber = int(input('Your guess: '))

        if userEnteredNumber > someNumber:
            print('Guess Lower!')

        elif userEnteredNumber < someNumber:
            print('Guess Higher!')

        else:
            print('You go it!')
            userGuessedCorrectly = True


if __name__ == '__main__':
    main()
