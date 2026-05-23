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
    