#generating rnadom numbers
import numpy as np
#seed definition
np.random.seed(123)

print(np.random.rand())

#simulating a dice, 7 is not included
print(np.random.randint(1,7))


#Some if stepping
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
    print("Going down")
elif dice <=5 :
    step = step +1
    print("Going up")
else :
    step = step + np.random.randint(1,7)
    print("Going up by far")

# Print out dice and step
print(dice)
print(step)