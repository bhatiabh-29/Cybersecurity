#!/usr/bin/env python
# coding: utf-8

# # Activity: Practice writing Python code

# ## Introduction
# 
# Python is a programming language that helps in automating instructions to the computer in a variety of contexts, including security contexts. Writing code in Python is a valuable skill that helps security analysts thrive in their technical work.
# 
# In this lab, you'll practice writing your first Python code while learning about a notebook environment. The hands-on practice you engage in throughout the labs will help you apply Python coding skills to your work as a security analyst. You'll benefit the most from the labs if you make sure to not only write in the cells that you're prompted to fill in, but also analyze all the cells thoroughly.

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
# As a security analyst, you'll often use notebook environments and notebooks to write and run code. This lab will help you get familiar with working in a notebook environment, writing code comments in Python, and displaying strings with the `print()` function.
# 
# In this lab, you'll complete a series of tasks that involve observing and running some pre-written cells of text and code, as well as filling in cells with your own text, Python code, and code comments.

# ## Task 1
# 
# The lab environment you're working in is a notebook-based coding environment. Notebooks, such as this one, consist of two types of cells: (1) text cells, also known as markdown cells, and (2) code cells.
# 
# Markdown cells allow you to write plain text and format it in the markdown language. Markdown language is used for formatting plain text in text editors and code editors. For example, you can use markdown to make headers, bold or italicize words, format text as code, add hyperlinks,  and more.
# 
# For this task, write something into the following markdown cell. Be sure to replace the "[Double-click to edit this markdown cell and write something here.]" with your own text. When you have finished editing, press the *Shift* and *Enter* keys (or on some keyboards, the *Shift* and *Return* keys) to display your text.

# [Double-click to edit this markdown cell and write something here.]

# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Double-click the markdown cell and replace the placeholder statement with your own. You can write any statement of your choice.
# 
# </details>

# ## Task 2
# 
# In Python notebooks, code cells allow you to write code comments and code in Python.
# 
# To run a code cell, first place your cursor on the cell. Then, you can either click on the play icon, or press the *Shift* and *Enter* keys (or on some keyboards, the *Shift* and *Return* keys).
# 
# For this task, run the following code cell as is and observe the output.

# In[1]:


# This cell displays "Hello world!"

print("Hello world!")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Once you click on the code cell, you can run the code by either clicking on the triangular play icon, or press the *Shift* and *Enter* keys (or on some keyboards, the *Shift* and *Return* keys).
# 
# </details>

# #### **Question 1**
# **What do you observe about the output after you ran the code cell?**

# The above line executes the print statement and it prints the word "Hello World!"
# 

# ## Task 3
# 
# Writing code comments is a way to document the intention behind code. It's a standard that analysts commonly use in their workflow. Writing comments that accompany code allows you to keep track of the technical decisions you've made in your project. This makes it easier for you and your team to read and revisit your code in order to understand what it does and why you took certain approaches.
# 
# For this task, run the following code cell as is and observe the output.

# In[2]:


# In Python, comments do not get displayed
# This code cell contains only comments


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Once you click on the code cell, you can run the code by either clicking on the triangular play icon, or press the *Shift* and *Enter* keys (or on some keyboards, the *Shift* and *Return* keys).
# 
# </details>

# #### **Question 2**
# **What do you observe about the output after you ran the cell above?**

# Anything mention as comments is not ran and displayed. Commnets are general pratice that every programmer follows to make the code more readable for others and to understand it in a better way. 

# ## Task 4
# 
# To type in a code cell, first click into the cell. Then you can write comments and code inside the cell.
# 
# For this task, add a comment at the beginning of the following code cell, describing what the code is doing. Write the comment to say `# This cell displays "I am using Python."`. Be sure to replace the `# YOUR COMMENT HERE` with your own comment before running the following cell.

# In[3]:


# This cell displays "I am using Python"

print("I am using Python.")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Once you click into the code cell, replace the placeholder comment with your comment. Recall that comments in Python start with the hash symbol (`#`).
# 
# </details>

# #### **Question 3**
# **What do you observe about the output after you ran the cell above?**

# After running the above cell the print statement is executed and "I am using Python is printed below that". Anything mentioned in comments is not printed. It is just for better undertstanding of the code and to make the code more readable.

# ## Task 5
# 
# In Python, `print()` helps you to display information to the screen.
# 
# For this task, use `print()` to display the message `"I am a security analyst."` by placing that message within the parentheses. Be sure to replace the `### YOUR CODE HERE ###` with your own code before running the following code cell.

# In[4]:


# This cell displays "I am a security analyst."

print("I am a security analyst.")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Once you click into the code cell, replace the `### YOUR CODE HERE ###` with `"I am a security analyst."`.
# 
# </details>

# #### **Question 4**
# **What do you observe about the output after you ran the cell above?**

# Print statement is executed and "I am a security analyst is printed"

# ## Task 6
# 
# For this task, write a `print()` statement to display the string `"Python is useful for security!"` Be sure to replace the `### YOUR CODE HERE ###` with your own code before running the following code cell.

# In[5]:


# This cell displays "Python is useful for security!"

print("Python is useful for security!")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Click into the code cell and use `print()` to display the message.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Place the message inside the parentheses of `print()`.
# 
# </details>

# #### **Question 5**
# **What do you observe about the output after you ran the cell above?**

# Print statement is used to display any thing in Python

# ## Task 7
# 
# For your final task, you'll combine all the `print()` statements you've encountered and written in this lab up to this point, into one code cell.
# 
# Complete the following code with the remaining messages. Be sure to replace each `### YOUR CODE HERE ###` with your own code before running the following cell.

# In[ ]:


# This cell displays all the statements written so far

print("Hello world!")
print("I am using Python.")
print("I am a security analyst.")
print("Python is useful for security!")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# First click into the code cell.
# 
# For the third `print()` statement, place the string `"I am a security analyst."` inside the parantheses of `print()`.
# 
# For the fourth `print()` statement, place the string `"Python is useful for security!"` inside the parantheses of `print()`.
# 
# </details>

# #### **Question 6**
# **What do you observe about the output after you ran the cell above?**

# Multiple print statements have been executed

# ## Conclusion
# 
# **What are your key takeaways from this lab?**

# print statement is used for printing the output we want in Python and "#" is used for writing single line comments and """ is used for writing multiple line comments"""

# In[ ]:




