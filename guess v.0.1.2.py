import shelve
from random import sample, shuffle

d = shelve.open('high_score')
counter_least = d['score'] 

digits = 3
guesses = 20

print('This Game Has Been Brought To You By Arinjoy Pramanik And Megh Mukherjee')
print('I am thinking of a', digits, 'digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  centi         One digit is correct but in the wrong position.')
print('  deci          One digit is correct and in the right position.')
print('  backit        No digit is correct.')
print('There are no repeated digits in the number.')

# Create a random number.

letters = sample('0123456789', digits)

if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)

print('I have thought up a number.')
print('You have', guesses, 'guesses to get it.')

counter = 1

while True:
    print('Guess #', counter)
    guess = input()

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.

    clues = []

    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('deci')
        elif guess[index] in number:
            clues.append('centi')

    shuffle(clues)

    if len(clues) == 0:
        print('backit')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == number:
        print('You got it right in ' , counter-1 , 'Guesses , CONGRATULATIONS!')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break

if counter < counter_least:

    print("CONGRATULATIONS AGAIN!! You Made A New HighScore")

    d = shelve.open('high_score')   
    d['score'] = counter          
    d.close()


else:
    print('The Least Number Of guesses are' , counter_least , "It's The Highscore, try to Beat IT!")





    

        

        
