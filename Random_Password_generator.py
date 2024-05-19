import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="abcdefghijklmnopqrstuvwxyz".upper()
numbers="0123456789"
symbols="!@#$%^&*()"
all_char=lower+upper+symbols+numbers
length=int(input("enter a length: "))
password="".join(random.sample(all_char,length))
print("Generated Password: ",password)
             