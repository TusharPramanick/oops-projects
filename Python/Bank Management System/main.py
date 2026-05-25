import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    dummyData = []

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                dummyData = json.loads(fs.read())
        else:
            print("No such file exists")
            
    except Exception as err:
        print(f"An exception occured as {err}")
        
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.dummyData))
    
    @classmethod
    def __accountGeneration(cls):
        alphabets = random.choices(string.ascii_letters, k=3)
        numbers = random.choices(string.digits, k=3)
        specialChr = random.choices("!@#$%^&*", k=1)
        
        id = alphabets + numbers + specialChr
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        userInfo = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "pin": int(input("Enter your 4-digit pin: ")),
            "email": input("Enter your email: "),
            "accountNumber": Bank.__accountGeneration(),
            "balance": 0
        }

        if userInfo['age'] < 18 or len(str(userInfo['pin'])) != 4:
            print("Sorry you cannot create an account")
        else:
            print("Your account has been successfully created")
            for i in userInfo:
                print(f"{i} : {userInfo[i]}")
                
            print("Keep your details safe somewhere")
            
            Bank.dummyData.append(userInfo)
            Bank.__update()
        
    def depositMoney(self):
        accountNumber = input("Enter your bank account number: ")
        pin = int(input("Enter your pin number: "))
        
        targetUser = [i for i in Bank.dummyData if i['accountNumber'] == accountNumber and i['pin'] == pin]
        
        if targetUser == []:
            print("Sorry you don't have a account in our bank")
            
        else:
            amount = int(input("Enter the amount you want to deposit in your account: "))
            if amount > 10000 or amount < 0:
                print("Enter amount must be between 10000 and 0, Please retry again")
            
            else:
                targetUser[0]['balance'] += amount
                Bank.__update()
                print("Amount has been Deposited Successfully")
                
    def withdrawMoney(self):
        accountNumber = input("Enter your bank account number: ")
        pin = int(input("Enter your pin number: "))
        
        targetUser = [i for i in Bank.dummyData if i['accountNumber'] == accountNumber and i['pin'] == pin]
        
        if targetUser == []:
            print("Sorry you don't have a account in our bank")
            
        else:
            amount = int(input("Enter the amount you want to withdraw from your account: "))
            if amount > targetUser[0]['balance']:
                print("Enter amount must be less than or equal to your current balance, Please retry again")
            
            else:
                targetUser[0]['balance'] -= amount
                Bank.__update()
                print("Amount has been withdrawn Successfully")
                
    def accountDetails(self):
        accountNumber = input("Enter your bank account number: ")
        pin = int(input("Enter your pin number: "))
        
        targetUser = [i for i in Bank.dummyData if i['accountNumber'] == accountNumber and i['pin'] == pin]
        if targetUser == []:
            print("Sorry you don't have a account in our bank")
            
        else:
            print("Your Account Details are \n")
            for i in targetUser[0]:
                print(f"{i} : {targetUser[0][i]}")
    
    def updateDetails(self):
        accountNumber = input("Enter your bank account number: ")
        pin = int(input("Enter your pin number: "))
        
        targetUser = [i for i in Bank.dummyData if i['accountNumber'] == accountNumber and i['pin'] == pin]
        if targetUser == []:
            print("Sorry you don't have a account in our bank")
            
        else:
            print("Your can't change the age, account number, Balance")
            print("Fill in the details you want to change or keep it empty if no change is required")
            
            newData = {
                'name' : input("Enter the new name or press enter: "),
                'email' : input("Enter the new email or press enter: "),
                'pin': input("Enter the pin and make sure it's in or press enter: ")
            }
            
            if newData['name'] == "":
                newData['name'] = targetUser[0]['name']
            if newData['email'] == "":
                newData['email'] = targetUser[0]['email']
            if newData['pin'] == "":
                newData['pin'] = targetUser[0]['pin']
                
            newData['age'] = targetUser[0]['age']
            newData['balance'] = targetUser[0]['balance']
            newData['accountNumber'] = targetUser[0]['accountNumber']
            
            if type(newData['pin']) == str:
                newData['pin'] = int(newData['pin'])
            
            for i in newData:
                if newData[i] == targetUser[0][i]:
                    continue
                else:
                    targetUser[0][i] = newData[i]
            
            Bank.__update()
            print("Your account details has been updated successfully")

        
    def deleteAccount(self):
        accountNumber = input("Enter your bank account number: ")
        pin = int(input("Enter your pin number: "))
        
        targetUser = [i for i in Bank.dummyData if i['accountNumber'] == accountNumber and i['pin'] == pin]
        
        if targetUser == []:
            print("Sorry you don't have a account in our bank")
            
        else:
            index = Bank.dummyData.index(targetUser[0])
            Bank.dummyData.pop(index)
            print("Your Account has been deleted Successfully!")
            Bank.__update()
            

user = Bank()

print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("Enter your choice: "))

match check:
    case 1:
        user.createAccount()
    
    case 2:
        user.depositMoney()
        
    case 3:
        user.withdrawMoney()
        
    case 4:
        user.accountDetails()
        
    case 5:
        user.updateDetails()
        
    case 6:
        user.deleteAccount()