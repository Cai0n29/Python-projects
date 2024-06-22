from random import *
from getpass import getpass
user_password = getpass('Enter Your Password: ')
password = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
final_pass = ""
while(final_pass !=  user_password):
    final_pass = ""
    for letter in range(len(user_password)):
        g = password[randint(0,25)]
        final_pass = str(g) + str(final_pass)
print('Password Cracked: '+ final_pass)