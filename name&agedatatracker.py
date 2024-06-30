#Dictionary
print('How many person/people you would like to input?')
num_per = int(input())
people = {}
for i in range(num_per):
    print('What is the name of the person?')
    name = input()
    print("What is the person's age")
    age = int(input())
    people[name] = age
print(people)
