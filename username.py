from string import ascii_lowercase
from random import choice, randint

abc = ascii_lowercase
users = []

def suggest_username(seed, n = 8):
    for i in range(randint(1,n)):
        seed = seed + choice(abc)
    return seed

while True:
    new_user = input("Enter a username: ")
    if new_user == "":
        break
    else:
        if new_user in users:
            suggested_name = suggest_username(new_user, n=8)
            while suggested_name in users:
                suggested_name = suggest_username(new_user, n=8)
            print("Sorry, that user name is taken.  Maybe try %s"%(suggested_name))
        else:
            users.append(new_user)

print(users)




