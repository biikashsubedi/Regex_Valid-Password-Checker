import re
pattern = re.compile(r'([a-zA-Z0-9@#%!]{8,100})')
password = input('Choose Password between 8~100: ')
print('Your Password: ' + password)
print('\n')

passw = pattern.fullmatch(password)
print(passw)
