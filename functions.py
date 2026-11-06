import random
from my_functions import greet
# Open the file in write mode


with open("data.txt", "w") as file:

    file.write("Cila\n")
    file.write("088\n")
    # a append w write r read
    for temp in range(100):
        x = random.randint(-10, 40)
        file.write(str(x) + "\n")

        # file.write(str(temp))

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
greet()


