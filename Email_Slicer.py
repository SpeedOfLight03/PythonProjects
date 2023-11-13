email = input("Enter Your Email: ").strip()
lst = email.split('@')
user_name = lst[0]
domain_name = lst[1]

print(f"Your Use Name is {user_name} and your Domain Name is {domain_name}")