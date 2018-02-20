import time
import datetime
'''this programme is for educational purposes to help the very few people
who dont understand how banking works, and also to just help me improve my coding skills'''

print("#----------------ONLINE BANKING SAMPLE SIMULATION----------------#")

class Clients:
    """this class keeps the clients of the bank passwords user names account balances and resent trasactions
    it also has transaction performing functions included in it fuctions include password changes etc.."""
    def __init__(self, first_name, last_name,title, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance = float(0)
        self.title = title
        self.bank_charge = 10
        self.transaction = " "
        self.login = 0
        self.transactions = []

#balance inquiry fuction to tell the user how much they have left
    def bal_inquiry(self):
        print("Your balance is $", self.balance)
        self.transaction = "A balance inquiry at ",datetime.date
        self.transactions.append(self.transaction)

#Allow the User to change password
    def pass_change(self):
        strikes = 0
        old_pass = input("Enter your old password")
        while strikes < 3 and old_pass != self.password:
            print("The password you entered was incorrect try again ")
            old_pass = input("Enter your old password: ")
            strikes += 1

        if strikes < 3:
            new_pass = input("Enter your new password: ")
            new_pass2 = input("Re-enter your new password: ")
            while new_pass != new_pass2:
                print("The password you entered is invalid try again")
                new_pass = input("Enter your new password: ")
                new_pass2 = input("Re-enter your new password: ")

            self.password = new_pass
        else:
            print("Sorry you have missed your password to many times Account will now be shut down")
            time.sleep(2)
            print("Thank You for Using this simulation")
            quit()

#Allow user to withdraw cash
    def withdraw(self):
        cash_request = int(input("Enter cash amount: "))
        net_withdrawal = cash_request + self.bank_charge
        while self.balance < net_withdrawal:
            print("Sorry you have insufficient funds in your account to complete the transaction")
            print("You can withdraw $",self.balance - 10)
            cash_request = int(input("Enter cash amount: "))

        self.balance -= net_withdrawal
        print("\nWithdrawal was successful")
        print("Please note you have also incurred a $10 bank charge")
        self.transaction = "Withdrew", cash_request, "on ", datetime.date
        self.transactions.append(self.transaction)

# Allow user to deposit cash
    def deposit(self):
        cash_input = int(input("Enter the cash amount: "))
        self.balance += cash_input
        print("Cash deposit was successful")
        self.transaction = "Deposited $", cash_input,"on ",datetime.date
        self.transactions.append(self.transaction)

#Users latest transactions
    def mini_statement(self):
        print("The following are your latest trasactions: ")
        for trans in self.transactions:
            print("-", trans)

#The-User_Interface
    def user_interface(self):
        while User.login == 1:
            print("Good day", self.title,self.first_name,self.last_name," serving you is our pleasure")
            Transaction = int(input("""select a transaction from the list below:
            1-Change pin
            2-Check balance
            3-Withdraw cash
            4-Deposit cash
            5-Mini Statement
             """))
            if Transaction == 1:
                User.pass_change()
            elif Transaction == 2:
                User.bal_inquiry()
            elif Transaction == 3:
                User.withdraw()
            elif Transaction == 4:
                User.deposit()
            elif Transaction == 5:
                User.mini_statement()

            self.login = int(input("""Do you want to perform another trasaction? 
            1- Yes
            2- No
            """))


#Login or create account
print("First let's create you an account so you can start banking with us")


First_name = input("Enter first name: ")
Last_name = input("Enter last name: ")
Title = int(input("""Select the appropriate title from the list below:
1-Mr
2-Mrs
3-Miss"""))
Password = input("Enter password: ")
Password2 = input("Retype password: ")

while Password != Password2:
    print("The password you enter is invalid please try again")
    Password = input("Enter password: ")
    Password2 = input("Retype password: ")

User = Clients(First_name,Last_name,Title,Password)
print("Please wait while setting up your account...")
time.sleep(3)
print("\nYour account has successfully been set up, you can now start banking")
User.login = 1
User.user_interface()






