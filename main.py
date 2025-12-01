import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
password_pieces = int(input('How many passwords would you like?:'))
password_long = int(input('How long password would you like?:'))
password_digits = input('Does digits in password?:')
password_lowercase = input('Does lowercase letters in password?:')
password_uppercase = input('Does uppercase letters in password?:')
password_special = input('Does special characters in password?:')
remove_badsymbols = input('Do you want il1Lo0O in password?:')

if password_digits.lower() == 'yes':
    chars += digits

if password_lowercase.lower() == 'yes':
    chars += lowercase_letters
if password_uppercase.lower() == 'yes':
    chars += uppercase_letters
if password_special.lower() == 'yes':
    chars += punctuation
if remove_badsymbols.lower() == 'yes':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(password_long, chars):
    password = ''
    for i in range(password_pieces):
        password = ''
        for j in range(password_long):
            password += random.choice(chars)
        print(password)
    return password


print(generate_password(password_long, chars))
