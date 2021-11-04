import getpass

try:
    password = getpass.getpass()
except Exception as error:
    print('Error:', error)
else:
    print('Password entered:', password)
