#1. Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not possible (division by zero)")

arithmetic_operations(8,2)


#2. Write a method for increment and decrement operators(++, --).
def increment_decrement(n):
    print("Value:", n)
    n += 1  # Increment
    print("After Increment:", n)
    n -= 1  # Decrement
    print("After Decrement:", n)


increment_decrement(10)

#3. Write a program to find the two numbers equal or not.
a = int(input())
b = int(input())
if(a==b):
    print("numbers are equal")
else:
    print("numbers are not equal")
#4. Program for relational operators (<,<==, >, >==)
a = 3
b = 25
print(a<b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)
#5.  Print the smaller and larger number.
a = int(input())
b = int(input())
if a < b:
    print("Smaller Number:", a)
    print("Larger Number:", b)
elif a > b:
    print("Smaller Number:", b)
    print("Larger Number:", a)
else:
    print("Both numbers are equal.")
