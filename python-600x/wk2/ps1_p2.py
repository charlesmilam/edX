s = 'azcbobobegghakl'

num_bobs = 0

for idx, char in enumerate(s):
    bob_check = s[idx:idx + 3]
    if bob_check == 'bob':
        num_bobs += 1

print 'Number of times bob occurs is: ' + str(num_bobs)
