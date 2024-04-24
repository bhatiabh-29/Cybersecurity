#!/usr/bin/env python
# coding: utf-8

# # Activity: Assign Python variables

# ## Introduction
# 
# Variables help security analysts to keep track of a variety of security-related information. For example, analysts may need to create Python variables for the users who are allowed to log in, the number of login attempts that they're permitted, and the current number of attempts that a user has made.
# 
# In this lab, you'll practice assigning values to variables and determining their data types.

# <details><summary><h2>Tips for completing this lab</h2></summary>
# 
# As you navigate this lab, keep the following tips in mind:
# 
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task.
# - To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.
# </details>

# ## Scenario
# You are a security analyst who is responsible for writing code that will automate analysis of login attempts made to a specific device. As the first step, you'll need to create variables to keep track of information relevant to the login process. This information includes the device ID, list of approved usernames, maximum login attempts allowed per user, current login attempts made by a user, and login status.
# 
# Throughout this lab, you'll assign these variables and check the data types of the variables.

# ## Task 1
# In your work as an analyst, imagine there is a device only users specified on an allow list can access, and its device ID is `"72e08x0"`.
# 
# In the following code cell, assign this value to a variable named `device_id`. Then, display the contents of the variable and observe the output.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[1]:


# Assign the `device_id` variable to the device ID that only specified users can access

device_id = "72e08x0"

# Display `device_id`

print(device_idce_id)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Use quotation marks around the value that you assign to the `device_id` variable.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Assign the value `"72e08x0"` to the variable `device_id`. To do this, place the value to right of the `=` operator.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# To display the contents of `device_id`, place the name of this variable inside the `print()` function.
# 
# </details>

# ## Task 2
# Now that the variable `device_id` is defined, you can return its data type.
# 
# In this task, use a Python function to find the data type of the variable `device_id`. Store the data type in another variable called `device_id_type`. Then, display `device_id_type` to examine the output.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.
# 

# In[2]:


# Assign the `device_id` variable to the device ID that only specified users can access

device_id = "72e08x0"

# Assign `device_id_type` to the data type of `device_id`

device_id_type = type(device_id)

# Display `device_id_type`

print(device_id_type)
    


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# The `type()` function allows you to get the data type of a given value.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use `type(device_id)` to get the data type of the `device_id` variable.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# To display `device_id_type`, place the name of this variable inside the `print()` function.
# 
# </details>

# #### **Question 1**
# **Based on the output above, what do you observe about the data type of `device_id`?**

#  The data type of the device_id is of class string

# ## Task 3
# As you continue your work, you're provided a list of usernames of users who are allowed to access the device. The usernames with this access are `"madebowa"`, `"jnguyen"`, `"tbecker"`, `"nhersh"`, and `"redwards"`.
# 
# In this task, create a variable called `username_list`. Assign a list with the approved usernames to this variable. Then, display the value of the `username_list` variable.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[3]:


# Assign `username_list` to the list of usernames who are allowed to access the device

username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`

print(username_list)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# To create a list in Python, use square brackets. Inside the square brackets, write the elements of the list, with a comma between elements.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To assign a value to a variable in Python, place the name of the variable to the left of the `=` operator, and place the value to the right of the `=` operator.
# 
# In this task, make sure to place `["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]` to the right of the `=` operator.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# To display `username_list`, place the name of this variable inside the `print()` function.
# 
# </details>

# ## Task 4
# In this task, find the data type of the `username_list`. Store the type in a variable called `username_list_type`. Then, display `username_list_type` to examine the output.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[4]:


# Assign `username_list` to the list of usernames who are allowed to access the device

username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Assign `username_list_type` to the data type of `username_list`

username_list_type = type(username_list)

# Display `username_list_type`

print(username_list_type)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# The `type()` function allows you to get the data type of a given value.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To get the data type of `username_list`, call the `type()` function and pass in `username_list`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# In Python, you can use the `print()` function to display the value of a variable. To display `username_list_type`, call the `print()` function and pass in `username_list_type`.
# 
# </details>

# #### **Question 2**
# **Based on the output above, what do you observe about the data type of `username_list`?**

# The type of variable username_list is of type list which store multiple values

# ## Task 5
# Now, imagine that you've been informed that the previous list is not up-to-date and that there is another employee that now has access to the device. You're given the updated list of usernames with access, including the new employee, as follows: `"madebowa"`, `"jnguyen"`, `"tbecker"`, `"nhersh"`, `"redwards"`, and `"lpope"`.
# 
# In this task, reassign the variable `username_list` to the new list. Run the code to display the list before and after it's been updated to observe the difference.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[5]:


# Assign `username_list` to the list of usernames who are allowed to access the device

username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`

print(username_list)

# Assign `username_list` to the updated list of usernames who are allowed to access the device

username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]

# Display `username_list`

print(username_list)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# When reassigning a variable to a new value in Python, place the name of the variable to the left of the `=` operator, just as you would when assigning the variable for the first time.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To reassign `username_list` to the updated list, place `username_list` to the left of the `=` operator.
# 
# </details>

# #### **Question 3**
# **Based on the output above, what do you observe about the contents of `username_list`?**

# The username list has been updated and the variable assigned to it has not changed it remains the same.

# ## Task 6
# In this task, define a variable called `max_logins` that represents the maximum number of login attempts allowed per user. Store the value `3` in this variable. Then, store its data type in another variable called `max_logins_type`. Display `max_logins_type` to examine the output.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[6]:


# Assign `max_logins` to the value 3

max_logins = 3

# Assign `max_logins_type` to the data type of `max_logins`

max_logins_type = type(max_logins)

# Display `max_logins_type`

print(max_logins_type)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# When assigning a value to a variable in Python, use the `=` operator. Place the name of the variable to the left of the `=` operator, and place the value to the right of the `=` operator.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To assign `3` to `max_logins`, place `max_logins` to the left of the `=` operator, and place `3` to the right of the `=` operator.
# 
# To assign `max_logins_type`, place `max_logins_type` to the left of the `=` operator before the `type()` function call.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# In Python, you can use the `print()` function to display the value of a variable. To display `max_logins_type`, call `print()` and pass in `max_logins_type`.
# 
# </details>

# #### **Question 4**
# **Based on the output above, what do you observe about the data type of `max_logins`?**

# The type of max_logins is of interger class

# ## Task 7
# In this task, define a variable called `login_attempts` that represents the current number of login attempts made by a user. Store the value `2` in this variable. Then, store its data type in a variable called `login_attempts_type`. Display `login_attempts_type` to observe the output.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[7]:


# Assign `login_attempts` to the value 2

login_attempts = 2
 
# Assign `login_attempts_type` to the data type of `login_attempts`

login_attempts_type = type(login_attempts)

# Display `login_attempts_type`

print(login_attempts_type)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# When assigning a value to a variable in Python, use the `=` operator. Place the name of the variable to the left of the `=` operator, and place the value to the right of the `=` operator.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To assign `2` to `login_attempts`, place `login_attempts` to the left of the `=` operator, and place `2` to the right of the `=` operator.
# 
# To assign `login_attempts_type`, place `login_attempts_type` to the left of the `=` operator, and place a call to the `type()` function to the right of the `=` operator.
# 
# When calling `type()`, make sure to pass in `login_attempts`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# In Python, you can use the `print()` function to display the value of a variable. To display `login_attempts_type`, call `print()` and pass in `login_attempts_type`.
# 
# </details>

# #### **Question 5**
# **Based on the output above, what do you observe about the data type of `login_attempts`?**

# The data type of the login attempts is integer

# ## Task 8
# In this task, you'll determine the Boolean value that represents whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.
# 

# In[8]:


# Assign `max_logins` to the value 3

max_logins = 3

# Assign `login_attempts` to the value 2

login_attempts = 2

# Determine whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed,
# and display the resulting Boolean value

print(login_attempts <= max_logins)
    


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# In Python, you can use the `<=` comparison operator to determine whether one value is less than or equal to another value.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To determine whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed, use the `<=` operator. Place `login_attempts` to the left of the `<=` operator, and place `max_logins` to the right of the `<=` operator.
# 
# To make sure the resulting Boolean value is displayed, write this code inside of the parantheses where `print()` is called.
# 
# </details>

# #### **Question 6**
# **What is the output? What does this mean?**

# The output of the staement is True since the login attempts is 2 which is less than the max logins attempts allowed.

# ## Task 9
# This code continues to check for the Boolean value of whether `max_logins` is less than or equal to `login_attempts`. In this task, reassign other values to `login_attempts`. For example, you might choose a value that is higher than the maximum number of attempts allowed. Observe how the output changes.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[9]:


# Assign `max_logins` to the value 3

max_logins = 3

# Assign `login_attempts` to a specific value

login_attempts = 5

# Determine whether the current number of login attempts a user has made is less than or equal to the maximum number of login attempts allowed,
# and display the resulting Boolean value

print(login_attempts <= max_logins)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# To assign `login_attempts` to a specific value, make sure to write the value to the right of the `=` operator.
# 
# </details>

# #### **Question 9**
# **Based on the different values you assigned to `login_attempts`, what did you observe about the output?**

# Based on the vallue assigned the output is False since the login attempts is greater than the max_logins

# ## Task 10
# Finally, you can also assign a Boolean value of `True` or `False` to a variable.
# 
# In this task, you'll create a variable called `login_status`, which is a Boolean that represents whether a user is logged in. Assign `False` to this variable and store its data type in a variable called `login_status_type` and display it.
# 
# Be sure to replace each `### YOUR CODE HERE ###` with your own code before you run the following cell.

# In[10]:


# Assign `login_status` to the Boolean value False

login_status = False

# Assign `login_status_type` to the data type of `login_status`

login_status_type = type(login_status)

# Display `login_status_type`

print(login_status_type)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# To assign the Boolean value `False` to the `login_status` variable, make sure to write `False` to the right of the `=` operator.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Note that Boolean values should not have quotation marks around them in code.
# 
# </details>

# #### **Question 8**
# **Based on the output above, what do you observe about the data type of `login_status`?**

# The value assigned to it is False which is of boolean data type

# ## Conclusion
# 
# **What are your key takeaways from this lab?**

# Data Types in Python:
# 
# Python is a dynamically typed language, which means that the data type of a variable is determined at runtime.
# Data types are important because they define the kind of data a variable can hold and what operations can be performed on it.
# 
# \String (str):
# 
# Strings are used to represent text in Python.
# They are enclosed in either single (' '), double (" "), or triple (''' ''' or """ """) quotes.
# Strings are immutable, meaning their values cannot be changed after creation.
# 
# Integer (int):
# 
# Integers are used to represent whole numbers in Python.
# They can be positive, negative, or zero.
# Python supports both regular integers and long integers, with automatic conversion as needed.
# 
# Boolean (bool):
# 
# Booleans have only two values: True and False.
# They are often used for logical operations and comparisons.
# Booleans are essential for conditional statements and control flow.
# 
# Type Function:
# 
# The type() function is used to determine the data type of a given object or variable.
# It returns a type object, which can be used to check the type of an object programmatically.

# In[ ]:




