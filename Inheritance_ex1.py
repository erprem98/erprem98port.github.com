class User:   #Parent class

    # Child class can access variable methods but can not access private variables
    def login(self):
        print("login")

    def register(self):
        print("Register")


class Student(User):           #Child class
    def enroll(self):
        print("Enroll")            


    def review(self):
        print("review")  



stu1=Student()
stu1.register()  
stu1.review()
stu1.enroll()      
