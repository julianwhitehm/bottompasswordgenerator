import random
import string

number = random.randint(8,32)
random_string = "".join(random.choice(string.ascii_lowercase) for i in range(number))

print("🥺")
print("👉👈 ")
print(random_string)
