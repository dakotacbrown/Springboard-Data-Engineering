from json_parser import json_parser
from accounts import Accounts
import json


class Savings:

    def __init__(self):
        self.df_savings = json_parser('data/savings.json')
        self.savingsHolder = [saving for saving in self.df_savings[0].apply(lambda item: Accounts("savings", item['account_num'], item['firstName'], item['lastName'], item['balance']) , axis=1)]


    def savingsChecker(self):
        isCcChecker = True
        while isCcChecker:
            userInput = input("Check savings account was selected.\n"
            "What would you like to do?:\n"
            "Account Info (Balance, Deposit, Withdraw): 'AI'\n"
            "Apply for Savings Account: 'AS'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                self.convertToJson()
                isCcChecker = False
                break
            elif userInput.lower() == 'ai':
                self.checkBalance()
            elif userInput.lower() == 'as':
                self.savingsApply()

    def checkBalance(self):
        isBalChecker = True
        while isBalChecker:
            savNum = input("Check balance was selected.\n"
            "Please enter your 5-digit savings account number: ")
            try:
                val = int(savNum)
                try:
                    if len(str(val)) == 5:
                        lastName = input("Please enter your last name: ")
                        checker = [save for save in self.savingsHolder if save.acc_num == int(savNum) and save.lastName.lower() == lastName.lower()]
                        if not checker:
                            userInput = input("You were not found in our system.\n" 
                            "Would you like to apply for a savings account? Y or N: ")
                            if userInput.lower() == 'y':
                                self.savingsApply()
                                isBalChecker = False
                                break
                            else:
                                input("Returning to the previous menu. (Press enter to continue.)")
                                isBalChecker = False
                                break
                        elif checker:
                            print("Current savings account balance: ${balance}.".format(balance = checker[0].balance))
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
                    "If you are not currently a member, would you like to apply for a savings account? Y or N: ")
                    if userInput.lower() == 'y':
                        self.savingsApply()
                        isBalChecker = False
                        break
                    else:
                        break
            except ValueError:
                userInput = input("Please enter a valid 5-digit account number.\n"
                "If you are not currently a member, would you like to apply for a credit card? Y or N: ")
                if userInput.lower() == 'y':
                    self.savingsApply()
                    isBalChecker = False
                    break
                else:
                    break

    def savingsApply(self):
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            checker = [cc for cc in self.savingsHolder if cc.firstName.lower() == firstName.lower() and cc.lastName.lower() == lastName.lower()]
            if checker:
                print("Hello {firstName} {lastName}, you already have a savings account with us.\n Current balance: ${balance}."
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
                acc_type = "savings"
                savingsNum = int(self.savingsHolder[-1].acc_num) + 1
                balance = 0.00
                self.savingsHolder.append(Accounts(acc_type, int(savingsNum), firstName, lastName, balance))
                print("Thank you {firstName} {lastName}. You account has been created!\n" 
                "Please write down the information below for your records.\n"
                "Savings Account Number: {savingsNum}\n"
                "Savings Account Balance: ${balance}.".format(firstName = firstName, lastName = lastName, savingsNum = savingsNum, balance = balance)
                )
                input("Please press enter to continue.")

    def deposit(self, person):
        while True:
            amount = input("Please enter the amount you would like to deposit: ")
            try:
                val = float(amount)
                try:
                    if float(val) > 0:
                        self.savingsHolder.remove(person)
                        person.deposit(val)
                        self.savingsHolder.append(person)
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
                        self.savingsHolder.remove(person)
                        person.withdraw(val)
                        self.savingsHolder.append(person)
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
        sorted(self.savingsHolder, key = lambda i: i['acc_num'])
        ccDict = {"savings" : [{"account_num" : int(saving.acc_num), "firstName" : saving.firstName, "lastName" : saving.lastName, "balance": float(saving.balance)} for saving in self.savingsHolder]}

        with open('data/savings.json', 'w') as outfile:
            json.dump(ccDict, outfile)