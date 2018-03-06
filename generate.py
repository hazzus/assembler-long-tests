import random
import sys

test_number = int(sys.argv[1])

x = random.randint(0, 2**(128*test_number)-1)
y = random.randint(0, 2**(128*test_number)-1)

with open('test.txt', 'w') as file:
    file.write(str(x * y))


print(str(x) + '\n' + str(y))
