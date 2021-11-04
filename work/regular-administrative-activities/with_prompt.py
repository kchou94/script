import getpass

try:
    password = getpass.getpass(prompt='Enter your password: ')
except Exception as error:
    print('Error:', error)
else:
    print('Password entered:', password)
