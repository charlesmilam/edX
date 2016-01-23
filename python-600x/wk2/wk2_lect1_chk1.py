# number guessing game
secret = int(raw_input('Please think of a number between 0 and 100! '))
low = 0
high = 100
guess = (low + high) / 2
guess_msg = "Enter 'h' for too high, 'l' for too low, 'c' for correct: "
resp = ""
proper_resps = ['h', 'l', 'c']

while resp != 'c':
    print
    print 'Is your secret number ' + str(guess) + "?"
    print

    resp = raw_input(guess_msg)
    print
    while resp not in proper_resps:
        print "Please respond with only 'h', 'l' or 'c'"
        print 'Try again'
        print
        resp = raw_input(guess_msg)

    if resp == 'h':
        high = guess
        guess = (low + high) / 2
    elif resp == 'l':
        low = guess
        guess = (low + high) / 2


print 'Your secret number is ' + str(guess)
