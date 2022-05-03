#Now we are going to write the the csv file 
import csv

# now we are gonna define our csv file using a function, so that we can write the csv file of our requirments
def write_into_csv(info_list):
    with open ("student_info.csv", "a", newline = "") as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact", "E-mail"])

        writer.writerow(info_list)
if __name__== "__main__":
    
    condition = True #This is the python program 
    student_num = 1
     
while(condition):
    student_info = input("Enter student info for student #{} (Name Age Contact E-mail) : ".format(student_num))
    
    student_info_list = student_info.split(" ")
   
    print("\nThe entered info is- \nName: {}\nAge: {}\nContact: {}\nE-mail: ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check = input("Is the entered info correct?(yes/no): ")
    if choice_check == "yes":
         write_into_csv(student_info_list)
         condition_check = input("Enter (yes/no) if you want to enter another student info: ")
         if condition_check == "yes":
          condition = True
          student_num = student_num + 1 
         elif condition_check == "no":
          condition = False
    elif choice_check =="no":
        print("\nPlease re-eneter the values.")




