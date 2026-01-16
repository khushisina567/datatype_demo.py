int_var = 10                      
float_var = 5.75                  
string_var = "42"                 
bool_var = False                 
print("Type of int_var:", type(int_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of bool_var:", type(bool_var))
print()
print("Arithmetic Operations:")
addition = int_var + float_var
multiplication = int_var * float_var
print("Addition:", addition)
print("Multiplication:", multiplication)
print()

print("Type Casting Operations:")
try:
    to_int = int(string_var)        
    to_float = float(string_var)   
    print("Converted to int:", to_int)
    print("Converted to float:", to_float)
except ValueError:
    print("Error: Cannot convert string to number!")
print()
user_value = input("Enter a number: ")
try:
    number = int(user_value)
    print("You entered integer:", number)
except ValueError:
    print("Invalid input! Could not convert to integer.")
print()
age = 21
print("Proper String + Number Concatenation:")
print("My age is " + str(age))      
print()
print("Dynamic Typing Demonstration:")
x = 100              
print("x =", x, "| type:", type(x))
x = "Python"          
print("x =", x, "| type:", type(x))
