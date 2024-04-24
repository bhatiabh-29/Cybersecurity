#!/usr/bin/env python
# coding: utf-8

# In[1]:


l1 = [1,2,3]
print(l1)


# In[2]:


letters = ["a", "b", "c"]
print(letters)



# In[4]:


matrix = [["a", "b"], ["c", "d"]]
print(matrix[1])


# In[6]:


#list function

chars = list("Hello World")
print(chars[0])


# In[8]:


#range function
numbers = list(range(1, 30))
print(numbers)


# In[9]:


#len function defines the number of items in the list 

print(len(numbers))


# In[12]:


#accessing elemenst from the list 

A_lits = list("Hello Wor")

print(A_lits[::2])


# In[13]:


#print the list in reverse order 
print(A_lits[::-1])


# In[14]:


#unpacking lists

numners = [1, 2, 3, 4, 5, 6, 7 ,8]
#assigning first 2 of them to different variables and keeping others in the list

first, second, *others = numners
print(first)
print(second)
print(others)


# In[15]:


#looging over the list 

new_list = list(range(20))

def loopinglist():
    for letters in new_list:
        print(letters)
        

loopinglist()


# In[19]:


#using enumerate 

def looping():
    new_list[0] = 100
    new_list[19] = 999
    for letter in enumerate(new_list):
        print(letter[0], letter[1])
        
looping()


# In[20]:


def looping():
    for index, item in enumerate(new_list):
        print(index, item)
        
looping()


# In[24]:


#Adding objects in the list 

add_remove_items = ["a", "b", "c"]

#add items to the end of the list 
add_remove_items.append("d")
print(add_remove_items)

#add items in between the list using the insert function, mention indes and the item
add_remove_items.insert(1, "@")
print(add_remove_items)


# In[26]:


#removing items from the list 

#using the pop function we can remove the item from the list 
#just using pop will delete the last item from the list
add_remove_items.pop()
print(add_remove_items)

#using index with the pop function can delete the item in between
add_remove_items.pop(1)
print(add_remove_items)


# In[27]:


#remove function can derectly remove the item in the list

new_list.remove(999)
print(new_list)


# In[28]:


#del can remove a range of object from the list 

del new_list[9:14]
print(new_list)


# In[29]:


#clear all the contents from the list

new_list.clear()
print(new_list)


# In[30]:


new_list.append(100)
print(new_list)


# In[32]:


new_list.append(100)


# In[ ]:


#count the number of occurances of 100 in the the list

new_list.count(100)

