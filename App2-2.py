#Write a Python program to print all positive numbers in a range.

# First creating the list, taking the input from the user 

list_1= []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele_ment = int(input())
 
    list_1.append(ele_ment) # adding the element
     
print(list_1)

# Now print all positive numbers in the the list created by the user
for num in list_1:  
    if num >= 0:
       print(num, end = " ")


