#!/usr/bin/env python3

from checking import Checking
from creditCard import CreditCard
from loans import Loans
from savings import Savings


cc = CreditCard()
loan = Loans()
savings = Savings()
check = Checking()

isProgramGoing = True

while isProgramGoing:
    userInput = input("Welcome to the Banking Service.\n"
        "What would you like to do?:\n"
        "Check savings account: 'SA'\n"
        "Check checking account: 'CA'\n"
        "Check credit card: 'CC'\n"
        "Check loan: 'CL'\n"
        "Exit: 'EX'\n"
    )
    if userInput.lower() == "ex" or userInput.lower() == "":
        isProgramGoing = False
        break
    elif userInput.lower() == "sa":
        savings.savingsChecker()
    elif userInput.lower() == "ca":
        check.checkingChecker()
    elif userInput.lower() == "cc":
        cc.ccChecker()
    elif userInput.lower() == "cl":
        loan.loansChecker()
    else:
        input("Please enter in a valid two character choice from the list. Thank you.")

print("Thank you for using our banking app. Have a nice day.")