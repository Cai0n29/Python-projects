import re 

string = 'The bulb is 8.5 watts'

watts = re.search('\d+\.\d+', string)

print(float(watts.group(0)))