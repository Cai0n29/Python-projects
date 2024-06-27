import matplotlib.pyplot as plt
print('YEARS:')
years =[]
for i in range(4):
    y = input()
    years.append(y)
print(years)
print('POPULATION:')
pop = []
for i in range(4):
    p = input()
    pop.append(p)
print(years)
print(pop)
plt.plot(years, pop)
plt.xlabel('YEAR')
plt.ylabel('POPULATION')
plt.title('POPULATION OVER THE YEARS')
plt.show()
