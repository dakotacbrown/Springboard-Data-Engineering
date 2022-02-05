from json_parser import json_parser
from accounts import Accounts
import json


class Checking:

    def __init__(self):
        self.df_check = json_parser('data/checking.json')
        self.checkHolder = [check for check in self.df_check[0].apply(lambda item: Accounts("checking", item['account_num'], item['firstName'], item['lastName'], item['balance']) , axis=1)]


    def checkingChecker(self):
        isCcChecker = True
        while isCcChecker:
            userInput = input("Check checking account was selected.\n"
            "What would you like to do?:\n"
            "Account Info (Balance, Deposit, Withdraw): 'AI'\n"
            "Apply for Checking Account: 'AC'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                self.convertToJson()
                isCcChecker = False
                break
            elif userInput.lower() == 'ai':
                self.checkBalance()
            elif userInput.lower() == 'ac':
                self.checkingApply()

    def checkBalance(self):
        isBalChecker = True
        while isBalChecker:
            checkNum = input("Check balance was selected.\n"
            "Please enter your 5-digit checking account number: ")
            try:
                val = int(checkNum)
                try:
                    if len(str(val)) == 5:
                        lastName = input("Please enter your last name: ")
                        checker = [check for check in self.checkHolder if check.acc_num == int(checkNum) and check.lastName.lower() == lastName.lower()]
                        if not checker:
                            userInput = input("You were not found in our system.\n" 
                            "Would you like to apply for a checking account? Y or N: ")
                            if userInput.lower() == 'y':
                                self.checkingApply()
                                isBalChecker = False
                                break
                            else:
                                input("Returning to the previous menu. (Press enter to continue.)")
                                isBalChecker = False
                                break
                        elif checker:
                            print("Current checking account balance: ${balance}.".format(balance = checker[0].balance))
                            userInput = input("Would you like to make a deposit or withdraw? D or W: ")
                            if userInput.lower() == 'd':
                                self.deposit(checker[0])
                                input("Returning to the previous menu. (Press enter to continue.)")
                                isBalChecker = False
                                break
                            elif userInput.lower() == 'w':
                                self.withdraw(checker[0])
                                input("Returning to the previous menu. (Press enter to continue.)")
                                isBalChecker = False
                                break
                            else:
                                input("Returning to the previous menu. (Press enter to continue.)")
                                break
                    else:
                        raise ValueError()
                except ValueError:
                    userInput = input("Please enter a valid 5-digit account number.\n"
                    "If you are not currently a member, would you like to apply for a checking account? Y or N: ")
                    if userInput.lower() == 'y':
                        self.checkingApply()
                        isBalChecker = False
                        break
            except ValueError:
                userInput = input("Please enter a valid 5-digit account number.\n"
                "If you are not currently a member, would you like to apply for a checking? Y or N: ")
                if userInput.lower() == 'y':
                    self.checkingApply()
                    isBalChecker = False
                    break

    def checkingApply(self):
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            checker = [cc for cc in self.checkHolder if cc.firstName.lower() == firstName.lower() and cc.lastName.lower() == lastName.lower()]
            if checker:
                print("Hello {firstName} {lastName}, you already have a checking account with us.\n Current balance: ${balance}."
                .format(firstName = firstName, lastName = lastName, balance = checker[0].balance))
                userInput = input("Would you like to make a deposit or withdraw? D or W: ")
                if userInput.lower() == 'd':
                    self.deposit(checker[0])
                    input("Returning to the previous menu. (Press enter to continue.)")
                elif userInput.lower() == 'w':
                    self.withdraw(checker[0])
                    input("Returning to the previous menu. (Press enter to continue.)")
                else:
                    input("Returning to the previous menu. (Press enter to continue.)")
            else:
                acc_type = "checking"
                checkingNum = int(self.checkHolder[-1].acc_num) + 1
                balance = 0.00
                self.checkHolder.append(Accounts(acc_type, int(checkingNum), firstName, lastName, balance))
                print("Thank you {firstName} {lastName}. You account has been created!\n" 
                "Please write down the information below for your records.\n"
                "checking Account Number: {checkingNum}\n"
                "checking Account Balance: ${balance}.".format(firstName = firstName, lastName = lastName, checkingNum = checkingNum, balance = balance)
                )
                input("Please press enter to continue.")

    def deposit(self, person):
        while True:
            amount = input("Please enter the amount you would like to deposit: ")
            try:
                val = float(amount)
                try:
                    if float(val) > 0:
                        self.checkHolder.remove(person)
                        person.deposit(val)
                        self.checkHolder.append(person)
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    amount = input("Please enter a valid amount, or would you like to quit? Y or N: ")
                    if amount.lower() == "y" or amount.lower() == "":
                        input("Please press enter to continue.")
                        break
            except ValueError:
                amount = input("Please enter a valid amount, or would you like to quit? Y or N: ")
                if amount.lower() == "y" or amount.lower() == "":
                    input("Please press enter to continue.")
                    break

    def withdraw(self, person):
        while True:
            amount = input("Please enter the amount you would like to withdraw: ")
            try:
                val = float(amount)
                try:
                    if float(val) > 0:
                        self.checkHolder.remove(person)
                        person.withdraw(val)
                        self.checkHolder.append(person)
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    amount = input("Please enter a valid amount, or would you like to quit? Y or N: ")
                    if amount.lower() == "y" or amount.lower() == "":
                        input("Please press enter to continue.")
                        break
            except ValueError:
                amount = input("Please enter a valid amount, or would you like to quit? Y or N: ")
                if amount.lower() == "y" or amount.lower() == "":
                    input("Please press enter to continue.")
                    break


    def convertToJson(self):
        sorted(self.checkHolder, key = lambda i: i['acc_num'])
        ccDict = {"checking" : [{"account_num" : int(check.acc_num), "firstName" : check.firstName, "lastName" : check.lastName, "balance": float(check.balance)} for check in self.checkHolder]}

        with open('data/checking.json', 'w') as outfile:
            json.dump(ccDict, outfile)