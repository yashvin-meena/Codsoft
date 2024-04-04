import random
import string

ch = string.ascii_letters + string.digits +string.punctuation
length = int(input('Enter the length of password to be generated:'))

my_password = ''
i= 1
while length >= i:
    my_password = my_password + random.choice(ch)
    i = i+1

print(my_password)
