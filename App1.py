# Write a Python program which accepts the radius of a circle from the user and computes area.

radius = float(input("Enter the radius of the circle: "))
area_circle = 3.1416*radius*radius
print("The area of the circle with radius", radius, "is: ", area_circle)




#write a Python program to accept a filename from the user and print the extension of that.

file_name = input("Input the filename: ")
fn_extension = file_name.split(".")
print ("The extension of the given file is : " + fn_extension[-1])