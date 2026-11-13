Stu_Id = input ("Enter your ID :")
Course_name = input ("Enter your course :")
Stu_name = input ("Enter your name:")
Stu_age = int (input ("Enter your age :"))
if Stu_Id == "CS104" and Stu_age >= 18:
    print ( "Student name:" , Stu_name )
    print ( "Course name :" , Course_name)
    print ("The age is :" , Stu_age )
    print ("Login Successful !")
    print ("Welcome to Campus Marketplace!! ")
else:
    print ("Invalid Student ID !")
    print ("Access Denied !")
   

