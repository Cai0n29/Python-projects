import numpy as np
import matplotlib as plt

print('Welcome to Coins Game!')
print('Game Criteria')
print('# Maximum of two people to play ')
print('# Maximum of 5 rounds to predict the tossed coin')
print(" # Choose between Heads or Tails ")

print("What's the first person's name?")
first = input()
print("What is the second person's name?")
second = input()
s = []
f = []
for i in range(3):
    np.random.seed(123)
    dice = np.random.randint(0, 2)
    print("What is your " + str(i + 1) + " prediction? " + first +  " Heads or Tails")
    first_pred = input()
    if dice == 0 and first_pred == 'Heads':
        f.append('t')
    elif dice == 1 and first_pred == 'Tails':
        f.append('t')
    else:
        f.append('f')
    np.random.seed(123)
    dice_sec = np.random.randint(0,2)
    print("What is your " + str(i + 1) + " prediction? " + second +  " Heads or Tails")
    sec_pred = input()
    if dice_sec == 0 and sec_pred == 'Heads':
        s.append('t')
    elif dice_sec == 1 and sec_pred == 'Tails':
        s.append('t')
    else:
        s.append('f')

if max(f) == 't':
    print(first + " you won the game!")
elif max(s) == 't':
    print(second + " you won the game!")
elif max(s) == 't' and max(f) == 't':
    print('You guys tied!')

    
    
    
    
