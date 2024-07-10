import numpy as np
print("Heads or Tails")
user= input()
np.random.seed(123)
coin =  np.random.randint(0, 2)
if coin == 0 and user == "Heads":
    print("Heads")
    print("Great prediction!")
elif coin == 1 and user == "Tails": 
    print("Tails")
    print("Great prediction!")
elif coin == 1 and user == "Heads": 
    print("Tails")
    print("Wrong guess")
elif coin == 0 and user == "Tails": 
    print("Heads")
    print("Wrong guess")


