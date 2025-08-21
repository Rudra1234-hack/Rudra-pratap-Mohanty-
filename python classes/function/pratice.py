# #1. reverse a string without using slicing
# str1 = "hello world"
# print("Reversed string:", ''.join(reversed(str1)))

# #2. count values in a string
# print("count value of a str:",str1.count('l'))

# #3.check if a string is a palindrome
# str2="madam"
# print("Is the string a palindrome?", str2 == str2[::-1])


# # what is a palindrome
# '''
#     A palindrome is a word, phrase, number, or other sequence of characters that reads the same
#     forward and backward (ignoring spaces, punctuation, and capitalization).
#     Examples of palindromes include "madam", "racecar",
# '''
# #4. write a function to calculate the factorial of a number
# # factorial of a numer means
# '''    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
#     It is denoted by n! and is defined as:
#     n! = n * (n-1) * (n-2) * ... * 1
#     For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
# '''
# def factorial(n):
#     """This function calculates the factorial of a number."""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# # calling the function
# num = 3
# print(f"The factorial of {num} is: {factorial(num)}")

# #5. write a function to check if a number is prime
# # A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
# # A prime number has exactly two distinct positive divisors: 1 and itself.
# # examples of prime numbers include 2, 3, 5, 7, 11, and 13.
# # how to calculate prime number in mathematics give me an example
# def is_prime(n):
#     """This function checks if a number is prime."""    
#     if n <= 1:
#         return False    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# # calling the function
# num = 9
# print(f"Is {num} a prime number? {is_prime(num)}")
# # for i in range(2, int(n**0.5) + 1) whatb does it mean
# # The expression `int(n**0.5) + 1` calculates the integer value of the square root of `n` and adds 1 to it.
# # calculat prime number in mathematics
# '''
#     To check if a number is prime, you can follow these steps:
#     1. Start with a number n greater than 1.        
#     2. Check if n is divisible by any integer from 2 to the square root of n (inclusive).
#     3. If n is divisible by any of these integers, it is not prime.
#     4. If n is not divisible by any of these integers, it is prime.
#     For example, to check if 29 is prime:
#     1. Start with n = 29.
#     2. Check divisibility from 2 to the square root of 29 (which is approximately 5.39).    
#     3. Check divisibility by 2, 3, 4, and 5.
#     4. 29 is not divisible by any of these numbers, so it is prime.
# '''
# #5. write a function to calculate prime numbers between 1 to n
# def prime_numbers(n):
#     """This function calculates prime numbers between 1 to n."""
#     primes = []
#     for num in range(2, n + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes
# # calling the function
# n = 20
# print(f"Prime numbers between 1 and {n} are: {prime_numbers(n)}")




#6. write a function to count words in a sentence
def count_words(sentence):
    """This function counts the number of words in a sentence."""
    words = sentence.split()
    return len(words)   
# calling the function
sentence = "Hello world, this is a test sentence."
print(f"The number of words in the sentence is: {count_words(sentence)}")   
# # use len() to count the number of words in a sentence
# # len() function uses
# # The len() function in Python returns the number of items in an object, such as a string, list, or tuple.

# #7. replace all spaces in a string with underscores
# def re(str):
#     """This function replaces all spaces in a string with underscores."""
#     return str.replace(' ','-')
# str="Hello world this is a test sentence."
# print(re(str))


data="rudra is a good boy"
flow=data.split()
word_count =len(flow)
print(word_count)