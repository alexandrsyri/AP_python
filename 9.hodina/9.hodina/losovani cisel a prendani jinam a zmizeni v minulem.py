nonshuffled = list(range(1,33))
shuffled = []
print(nonshuffled)
import random

while nonshuffled:
    shuffled.append(nonshuffled.pop(random.randint(0,len(nonshuffled)-1)))

print(nonshuffled)
print(shuffled)
