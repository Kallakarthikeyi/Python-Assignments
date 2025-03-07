#1. Write a program to print your name. 
print ("Kalla Sree Karthikeyi")
#2. Write a program for a Single line comment and multi-line comments 
# Single line Comment
''' Multi Line Comments are simple and easy 
          to understand the code '''
#3.  Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a = 13
print(a, type(a))
b = True 
print(b, type(b))
#Python does not have an explicit char or double data type like some other languages
'''
char is represented as a single-character string (str).
double is represented as a float since Python’s float is equivalent to a double-precision floating-point number in other languages.
'''
c = 'k '
print(c, type(c))
d = 87.78
print(d, type(d))
e = 56.7895643
print(e, type(e))
#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

# Global variable
x = 10  

def my_function():
    # Local variable with the same name
    x = 20  
    print("Local x:", x)  # This will print the local variable inside the function

# Printing the global variable
print("Global x:", x)  


my_function()

# Printing global variable again to check 
print("Global x after function call:", x)
