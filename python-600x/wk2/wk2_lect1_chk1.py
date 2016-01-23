# number guessing game
secret = int(raw_input('Please think of a number between 0 and 100! '))
guess = 50

while guess != secret:
    print 'keep guessing'

print 'Your secret number is ' + str(guess)
