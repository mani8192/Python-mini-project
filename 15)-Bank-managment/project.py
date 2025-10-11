# step 3 -- import json file --
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():  
            with open(database) as fs:
                data = json.load(fs)  
        else:
            print("no such file exist")   
    except Exception as err:
        print(f"an Exception accured as {err}")
        
    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
            
    @classmethod
    def __accountgenrater(cls):
        alpha = random.choices(string.ascii_letters, k=3)  
        num = random.choices(string.digits, k=3)            
        spchar = random.choices("@#$&*!", k=1)           
        id = alpha + num + spchar
        random.shuffle(id)                                  
        return "".join(id)
        
    # -create a account ------@1
    def Createaccount(self):
        info= {
            "name" : input("Tell your name :-"),
            "age" : int(input("Tell your age")),
            "E-mail" : input("Tell your E-mail"),
            "Pin" : int(input("Tell your Pin :-")),
            "account" : Bank.__accountgenrater(),   # string account
            "balance" :0,
        } 
        
        if info['age'] < 18 or len(str(info['Pin'])) != 4: 
            print("you can not create your account")
        
        else:
            print("account has been created Successfully")
            for i in info:
                print(f"{i} :{info[i]}")
            print("please note down your account number")
            Bank.data.append(info)
            Bank.__update()
            
            
    # ---------@2
    def depositmoney(self):
        accountNo = input("pleasse tell your account number :-")  
        pin = int(input('Please Enter a Pin number here:-'))
        
        userdata = [i for i in Bank.data if i['account'] ==  accountNo and  i['Pin'] == pin]
        
        if not userdata:   
            print("sorry no data found")
            
        else:
            amount = int(input("How much you want to deposit :-"))
            
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 ")
                
            else:
                userdata[0]['balance'] += amount  
                Bank.__update()
                print("amount deposit successfuly")
    
    #  withdrawal amount --
    def withdrowmoney(self):
        accountNo = input("pleasse tell your account number :-")  
        pin = int(input('Please Enter a Pin number here:-'))
        
        userdata = [i for i in Bank.data if i['account'] ==  accountNo and  i['Pin'] == pin]
        
        if not userdata:   
            print("sorry no data found")
            
        else:
            amount = int(input("How much you want to withdrow:-"))
            
            if userdata[0]['balance'] < amount:
                print("sorry you don't have much money ")
                
            else:
                userdata[0]['balance'] -= amount  
                Bank.__update()
                print("amount withdrew successfuly")
                
                
    #  show user details ---
    def show_details(self):
        accountNo = input("pleasse tell your account number :-")  
        pin = int(input('Please Enter a Pin number here:-'))
        
        userdata = [i for i in Bank.data if i['account'] ==  accountNo and  i['Pin'] == pin]
        if not userdata:
            print("sorry no data found")
            return

        print("your information are \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]} ")
    
    
    
    #  update details --
    def update_details(self):
        accountNo = input("pleasse tell your account number :-")  
        pin = int(input('Please Enter a Pin number here:-'))
        
        userdata = [i for i in Bank.data if i['account'] ==  accountNo and  i['Pin'] == pin]
        
        if not userdata:
            print("no such data found")
            return
            
        print("you can't change the age , account number , balance")
        print("fill the details for change or leave it empty if no change")
            
        newdata = {
            "name" : input("Enter new name or press enter to skip:- "),
            "E-mail": input("Enter a new E-mail or press enter to skip :-"),
            "Pin": input("enter a new pin or press enter to skip:-")
        }    
        
        if newdata['name'] == "":
            newdata["name"] = userdata[0]["name"]
        if newdata["Pin"] == "":
            newdata["Pin"] = userdata[0]["Pin"]
        if newdata["E-mail"] == "":
            newdata["E-mail"] = userdata[0]["E-mail"]
            
        newdata["age"] = userdata[0]["age"]
        newdata["account"] = userdata[0]["account"]
        newdata["balance"] = userdata[0]["balance"]
        
        if isinstance(newdata["Pin"], str):
            newdata["Pin"] = int(newdata["Pin"])
            
        for i in newdata:
            userdata[0][i] = newdata[i]
                
        Bank.__update()
        print("details update successful")
    

    # delete account ---
    def delete_account(self):
        accountNo = input("pleasse tell your account number :-")  
        pin = int(input('Please Enter a Pin number here:-'))

        userdata = [i for i in Bank.data if i['account'] ==  accountNo and  i['Pin'] == pin]

        if not userdata:
            print("sorry no data found")
        else:
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("Your account has been deleted successfully")

         
user = Bank()
#step 1 -- Account Details --
print("Press 1 for  Creating an account :- ")
print("Press 2 for Depositing the money in the bank :-")
print("Press 3 for Withdrawing the money :-")
print("Press 4 Account details :-")
print("Press 5 for updating the details :-")
print("Press 6 for deleting your Account :-")

# Step 2  Access all details
check = int(input("Tell your response :-"))

if check == 1:
    user.Createaccount()
    
if check == 2:
    user.depositmoney()
    
if check == 3:
    user.withdrowmoney()
    
if check == 4:
    user.show_details()
    
if check == 5:
    user.update_details()  

if check == 6:
    user.delete_account()