import getpass

password = getpass.getpass(prompt='Enter your password: ')

if password.lower() == '#pythonworld':
    print('Welcome!')
else:
    print('Wrong password!')
