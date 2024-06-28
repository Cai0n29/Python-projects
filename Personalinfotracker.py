import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

cars = {'Country':names, 'Drives_right': dr, 'Speed':cpc}

cars = pd.DataFrame(cars)
print(cars)

print('Number of people')
p = int(input())
countries = []
names = []
ages = []
for i in range(p):
    print("What is the person's nationality")
    count = input()
    countries.append(count)
    print("What is the person's name")
    name = input()
    names.append(name)
    print("What is the person's age")
    age = input()
    ages.append(age)
dic = {'Nationality': countries, 'Name': names, 'Age':ages}
dic = pd.DataFrame(dic)
print(dic)
    
    
    