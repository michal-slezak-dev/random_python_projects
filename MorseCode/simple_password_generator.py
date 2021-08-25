import random
import string 

all = list(string.letters + string.digits + string.punctuation)

x = int(input())

for k in range(x + 1):
    password = random.choice(all)
    print(password, end="")
