#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
lower=int(input('enter lower bound:'))
upper=int(input('enter upper bound:'))
x=random.randint(lower,upper)
totalchances=math.ceil(math.log(upper-lower+1,2))
print('\n\t you have only',totalchances,'chances to guess the number\n')
count=0
flag=False
while count< totalchances:
    count+=1
    guess=int(input('guess a number:'))
    if x==guess:
        print('congratulations you guessed correctly!',count,'try')
        flag=True
        break
    elif x>guess:
        print('you guessed a smaller number!')
    elif x<guess:
        print('you guessed too big number!')
if not flag:
    print('\n the correct number is %d'%x)
    print('\n better luck next time!')


# In[ ]:




