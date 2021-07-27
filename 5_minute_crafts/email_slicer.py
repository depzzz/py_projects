while True:
    email = input("Wass ur email address bish? ").strip()
    if '@' not in email:
        print("Invalid Email Address")
        continue
    break

# Extract Username and Host using @ as Seperator
mylist = email.split("@")
username = mylist[0]
host = mylist[1]

# Print Username and Host
print(f"Username = {username}")
print(f"Host: {host}")