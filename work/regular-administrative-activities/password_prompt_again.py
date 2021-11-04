import getpass

user_name = getpass.getuser()
print("User Name : %s" % user_name)

while True:
    password = getpass.getpass(prompt='Enter your password: ')

    if password == '#pythonworld':
        print('Welcome!')
        break
    else:
        print('Wrong password!')
