#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Write a Python program to solve (x + y) * (x + y)
#Test Data : x = 4, y = 3

x=4; y=3
print((x + y) * (x + y))


# In[44]:


#Write a Python program to parse a string to Float or Integer.
x=input('Enter a number:')

while True:
    try:
        print(float(x))
        print(int(x))
        break
    except ValueError:
        print('please enter a number istead of a string')
        break


# In[72]:


#Write a python program to find the sum of the first n positive integers.

n=int(input('Enter a number: '))
sum=0

for i in range(0,n+1):
    sum=i+sum
    print(sum)
print(sum)


# In[98]:


#Write a Python program to convert the distance (in feet) to inches, yards, and miles

d_infeet=input('Please enter the distance (in feet): ')

x=float(d_infeet)
print(x,'in feet equal to ',x*12,' inches')
print(x,'in feet equal to ',x/3,' yaards')
print(x,'in feet equal to ',x/5280,' miles')


# In[99]:


#Write a Python program to convert all units of time into seconds
t_hour=float(input('Please enter the hours: '))
t_minutes=float(input('Please enter the minutes: '))
t_second=float(input('Please enter the second: '))

print('The total time in seconds: ',t_hour*60*60+t_minutes*60+t_second)


# In[117]:


#Write a Python program to convert seconds to day, hour, minutes and seconds.
t_second=input('Please enter the total seconds: ')

x=float(t_second)

m_day=60*60*24
m_hour=60*60
m_minute=60

t_day=x//m_day
t_hour=(x-t_day*m_day)//m_hour
t_minute=(x-t_day*m_day-t_hour*m_hour)//m_minute
t_second=x-t_day*m_day-t_hour*m_hour-t_minute*m_minute

print(t_day,'day ',t_hour,'hour ',t_minute,'minute ',t_second,'second')


# In[120]:


#Given variables x=30 and y=20, write a Python program to print "30+20=50"
x=30; y=20

print(f"{x}+{y}={x+y}")


# In[149]:


#Write a Python program to perform an action if a condition is true. Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
variable=1

if variable==True:
    print("First day of a Month!")


# In[139]:


#Write a Python program to check whether variable is of integer or string
v_testing=input('please input a variable: ')

while True:
    try:
        int(v_testing)
        print("It's a integer!")
        break
    except ValueError:
        print("It's a string!")
        break


# In[148]:


#Write a Python function to find the maximum and minimum numbers from a sequence of numbers

sequence_number=input('Enter elements of a list separated by space: ')
number_list=sequence_number.split()
print(number_list)

m_max=int(number_list[0])
m_min=int(number_list[0])

for i in range(len(number_list)):
    if m_max<int(number_list[i]):
        m_max=int(number_list[i])
        
    if m_min>int(number_list[i]):
        m_min=int(number_list[i])

print('The maximum numbers from a sequence of numbers: ',m_max)
print('The minimum numbers from a sequence of numbers: ',m_min)


# In[ ]:




