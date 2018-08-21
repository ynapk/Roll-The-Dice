
# coding: utf-8

# In[302]:


#Import Libs
import random

#Roll Function
def roll_die(sides):
    result = random.randint(1,sides)
    return result

#User Inputs for how many sides on the die
sides = int(input('How many sides on the die?'))
roll = roll_die(sides)

#Print Roll
print(' ')
print('Your die has', sides, 'sides.')
print('You rolled a: ', roll)


# In[ ]:




