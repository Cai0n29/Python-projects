print('Welcome to Calculator.py!')
print('Kindly input the 1st number')
user = int(input())
print('Kindly input a Math Symbol. Ex. + - x /')
symbol = input()
print('Kindly input the 2nd number')
sec_user = int(input())


if symbol == '+':
    print("sum: " + str(user + sec_user))
elif symbol == '-':
    print("difference: " + str(user - sec_user))
elif symbol == '/':
    print("quotient: " + str(user / sec_user))
elif symbol == 'x':
    print("product: " + str(user * sec_user))
    