import random

print(random.randint(5, 20))  # line 1
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 5, and the largest could have been 20.

print(random.randrange(3, 10, 2))  # line 2
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 3, and the largest could have been 9.
# Could line 2 have produced a 4?
# No, line 2 could not have produced a 4 because the range starts at 3 and steps by 2,
# resulting in possible values of 3, 5, 7, and 9

print(random.uniform(2.5, 5.5))  # line 3
# What was the smallest number you could have seen, what was the largest?
# The smallest number could have been 2.5, and the largest could have been 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
