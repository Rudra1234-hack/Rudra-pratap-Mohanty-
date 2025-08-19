# marks =[10, 20, 30, 40, 50]
# # for mark in marks:
# #     print("Mark:", mark)
# #     if mark >= 40:
# #         print("Pass") 
# #     else:
# #         print("Fail")




# # # stoping_point = 30
# # for mark in marks:
# #     print("Mark:", mark)
# #     if mark== 30:
# #         break
    
    
    
# # range
# # for i in range(10):
# #     print("number:", i)


# # for i in range(1, 11):
# #     print("number:", i)


# # nexted loops
# for i in range(1, 4):
#     for j in range(1, 4):
#         print("i:", i, "j:", j)
    
# 1. Write a program that prints the sum of all numbers from 1 to 50 using a for loop.
sum=0
for i in range (1,51):
    sum+=i
    
print("sum of the total numbers is:",sum)
print(" ")

# 2. Use a for loop to print the multiplication table of 5.
for i in range(1,11):
    print("5 x",i,"=", 5 * i)
print(" ")

#3. Given a list of integers [2, 4, 6, 8, 10] loop to print each number squared.
num=[2,4,6,8,10]
for i in num:
    print("Square of", i, "is", i*i)
print(" ")
#4. Write a program using a for loop to print all even numbers between 1 and 20.
for i in range(1,21):
    if i%2==0:
        print("all even number between 1 to 21 is :",i)
print(" ")