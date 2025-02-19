#1) Create a python single line comment

# Python single line comments still use the pound sign like in PowerShell.

#2) Create a python multiline comment
"""
This is an example of how to do a multiline comment for Python, even though there
is not official support for multiline comments in Python.
"""
# According to some, putting
# multiple pound sings also
# counts as a multi-line comment.

"""
3) Create a variable called name with the value of your name.
Create a print statement to say ‘Hello [Name]’ using the variable for your name. 
How can you get python to pull the variable value inside of the print statement string (don’t break out of the quotes)?
"""
name = "Gage Rotz"
print(f"Hello {name}") #Using an f-string to insert the name, which was added in Python 3.6.
name = 'Gage Rotz'
print(f'Hello {name}')

#4) Compare the results of #3 using single and double quotes around the string. Does it make a difference like it does in PowerShell?

# There is no difference in how the string is called when it comes to single or double quotes.

#5) What is the purpose of an Escape Character in Python? Create a few print statements utilizing different escape characters, can you get the print statement to output on two lines?

# An escape character is used to put character that have special meanings (such as quotes) into a string in Python. 
# Escape characters also give new functions to otherwise ordinary characters, such as using \n to create a new line.
print("People now say \"sus\" instead of suspicious.")
print("I can now easily print \non new lines.")
print("\t1\t2\t3\t4\t5\n1\n2\n3\n4\n5") # Making a small table (Without any values in the cells.).