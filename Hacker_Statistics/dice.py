#Random float
#Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. 
#You're going to use randomness to simulate a game.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


#Roll the dice
#In the previous exercise, you used rand(), that generates a random float between 0 and 1.
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))


#Determine your next move
#In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice.
#We can perfectly code this with an if-elif-else construct!
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random. randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)