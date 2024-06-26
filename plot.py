import matplotlib.pyplot as plt
print('Input the months:')
Months = []
for i in range(3):
    a = input()
    Months.append(a)
print(Months)
print('Input the number of students per month:')
student_num = []
for i in range(3):
    stu = input()
    student_num.append(stu)
print(Months)
print(student_num)
plt.scatter(Months, student_num)
plt.show()
plt.plot(Months, student_num)
plt.show()
