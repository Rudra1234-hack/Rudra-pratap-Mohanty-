# # string inbuild methods
str1 = "hello world"   

# #length of string
# print(len(str1))  # Output: 11  
# #counting the number of occurence of a character
# print(str1.count('l'))  # Output: 3
# #finding the index of a character
# print(str1.index('o'))  # Output: 4
# #converting string to lower case
# print(str1.lower())  # Output: hello world
# #converting string to upper case
# print(str1.upper())  # Output: HELLO WORLD
# #replacing a character in string
# print(str1.replace('o', 'x'))  # Output: hexxo worxd
# #splitting a string into a list
# print(str1.split(' '))  # Output: ['hello', 'world']
# #joining a list into a string
# str2 = " ".join(['hello', 'world'])
# print(str2)  # Output: hello world

# #checking if a string starts with a specific substring
# print(str1.startswith('he'))  # Output: True   

# #checking if a string ends with a specific substring
# print(str1.endswith('ld'))  # Output: True
# #reversing a string
# print(str1[::-1])  # Output: dlrow olleh  

# #strip
# str3 = "    Hello World!   "
# #removing leading and trailing spaces
# print(str3.strip())  # Output: Hello World!

# #lstrip
# #removing leading spaces
# print(str3.lstrip())  # Output: Hello World!   
# #rstrip
# #removing trailing spaces
# print(str3.rstrip())  # Output:    Hello World
#5. Create a for loop that iterates through a string and prints each character on a new line.
for char in str1:
    print(char)
    
