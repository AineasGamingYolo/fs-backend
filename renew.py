#TODO Make this work

import random
import string
import os
import sys


for arg in sys.argv:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    command_list = [
        'secret_key',
        'react_secret_key',
        'help'
    ]

    if arg == 'secret_key':

        yes_or_no = input("Warning! This will replace the secret key and it will log all users out! Type yes to continue: ")
        if yes_or_no == "yes":

            # get random string password with letters, digits, and symbols
            def generate_key(length):
                password_characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(password_characters) for i in range(length))
                print("Random string password is:", password)

            new_key = generate_key(64)

            #def replace_key(self):
            replace_me.replace(replace_me, "replaced")

        elif yes_or_no == "no":
            print("Successfully canceled!")

        else:
            print("Invalid answer! Please try again and use yes or no!")

    if arg == 'help':
        help_txt = "py renew.py secret_key changes your secret key automatically to a 64 character one" \
                   "py renew.py react_secret_key changes your react secret key that is used to communicate to the backend-frontend" \
                   "py renew.py help shows this section"
        print(help_txt)

if arg not in command_list:
    renew_command_list = 'secret_key, react_secret_key, help'
    print("Invalid argument! Available are: " + renew_command_list)
