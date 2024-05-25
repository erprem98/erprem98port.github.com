class Atm:
#function written inside a class is known as method

 def __init__(self): 
    self.pin=""
    self.__balance=0
    self.menu()
   
 def menu(self):
   
   user_input=input("""
    Hello,how would you like to proceed?
     1. Enter 1 to create pin
     2. Enter 2 to deposit
     3. Enter 3 to withdraw
     4. Enter 4 to check balance
     5. Enter 5 to exit                                                                           
                    """)
   
   if user_input=="1":
    #print("Create pin")
    self.create_pin()
   elif user_input=="2":
     #print("Deposit")
     self.deposit()
   elif user_input=="3":
    #  print("withdraw")
    self.withdraw()
   elif user_input=="4":
    #  print("check balance") 
    self.check_balance()

   else:
     print("Exit ")  
 def create_pin(self):
   self.pin=input("enter your pin")
   print("Pin set successfully")

 def deposit(self):
   tmp = input("Enter your pin")
   if tmp==self.pin:
     amount = int(input("Enter the amount to deposit"))
     self.balance= self.balance+amount
     print("Amount deposit successfully")
   else:
     print("Invalid pin")  

 def withdraw(self):
   temp = input("Enter your pin")
   if temp==self.pin:
     amount=int(input("Amount to withdraw"))
     if amount<self.balance:
      self.balance= self.balance-amount
      print("Transaction completed successfully")
     else:
       print("Insufficient funds") 
   else:
     print("Invalid Pin")    

 def check_balance(self):
   if self.pin==input("Enter your PIN"):
     print("Available Balance is ",self.balance)
   else:
     print("Invalid pin")

obj=Atm()
obj.check_balance()

#Self is current object of that class
#Self is used because within a class one method or function can not access or communicate other methods
# so to access other functions self is used






     
                    


  





