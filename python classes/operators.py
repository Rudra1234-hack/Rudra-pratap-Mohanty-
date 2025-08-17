#  Arithmetic Operators
a= 10
b=3
print(a+b)  # Addition
print(a-b)  # Subtractionprint(a*b)  # Multiplication
print(a/b)  # Division
print(a//b) # Floor Division
print(a%b)  # Modulus
print(a**b) # Exponentiationprint(a*b)
print(a**b) # Exponentiation    

#comparison operators
print(a==b)    # Equal to
print(a!=b)  # Not equal to
print(a>b)  # Greater than
print(a<b)  # Less than
print(a>=b)  # Greater than or equal to
print(a<=b)  # Less than or equal to    

# Assignment Operators
a = 10
b = 5
a += b  # a = a + b
print(a)
# a = 15
a -= b  # a = a - b
print(a)# a = 10
a *= b  # a = a * b         
print(a)  # a = 50
a /= b  # a = a / b
print(a)  # a = 10.0
a //= b
print(a)  # a = 2.0
a %= b  # a = a % b
print(a)  # a = 0.0
a **= b  # a = a ** b
print(a)  # a = 0.0     

#logical operators
a = True
b = False
print(a and b)  # Logical AND
print(a or b)  # Logical OR
print(not a)  # Logical NOT 

#membership operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) # Membership test       
print(6 not in my_list) # Membership test
print(3 not in my_list) # Membership test
print(6 in my_list) # Membership test
# Identity Operators
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # Identity test
print(a is c)  # Identity test
print(a == c)  # Equality test
print(a is not c)   # Identity test     
