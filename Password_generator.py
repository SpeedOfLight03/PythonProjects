import random
pass_len = int(input("Enter the length of the password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(s, pass_len))
print(password)