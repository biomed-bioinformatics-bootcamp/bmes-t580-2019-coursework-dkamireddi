import random

print('-----------------------------------------------------')
print('                GUESS THAT Primer Game')
print('-----------------------------------------------------')
print()

goal = random.choice('ACGT')
for i in range(4):
    goal += random.choice('ACGT')
guess = 'NNNNN'
name = input('Player what is your name?')

while guess != goal:
    guess = input('Guess a 5 bp primer (A, C, T or G):')

    misses = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            misses += 1
    number_correct = len(guess) - misses
    if misses > 0:
        print('Sorry, you only  guessed %i base(s) correctly. Play again?' % number_correct)
    else:
        print('Excellent work %s, you won!' % name)
print("done")
