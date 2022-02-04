#!/usr/bin/env python3

from accounts import Accounts
from customers import Customers
from employees import Employees
from json_parser import json_parser
from services import Services
import pandas as pd
import keyboard
import random
import string

global position_and_sal                                                     #Dictionary of positions and salaries in company
position_and_sal = {
    "Teller" : 75000.00,
    "Manager" : 100000.00,
    "District Manager": 150000.00,
    "Regional Manager": 500000.00
}
#self._position = random.choice(list(position_and_sal))
#self._salary = position_and_sal[self._position]
#'4' + ''.join(random.choices(string.digits, k=15))

df_accounts = json_parser('data/accounts.json', size=2)
df_customers = json_parser('data/customers.json')
df_employees = json_parser('data/employees.json')
df_services = json_parser('data/services.json', size=2)


ccHolder = df_services[0].apply(lambda item: Services("credit card", item['cc_num'], item['firstName'], item['lastName'], item['credit_limit'], item['need_to_pay']), axis=1)
checkingHolder = df_accounts[0].apply(lambda item: Accounts("checking", item['account_num'], item['firstName'], item['lastName'], item['balance']) , axis=1)
customersHolder = df_customers[0].apply(lambda item: Customers(item['id'], item['firstName'], item['lastName'], item['address']) , axis=1)
employeesHolder = df_employees[0].apply(lambda item: Employees(item['id'], item['firstName'], item['lastName'], item['position'], item['active'], item['salary']) , axis=1)
loansHolder = df_services[1].apply(lambda item: Services("loans", item['loan_id'], item['firstName'], item['lastName'], item['balance'], item['need_to_pay']), axis=1)
savingsHolder = df_accounts[1].apply(lambda item: Accounts("savings", item['account_num'], item['firstName'], item['lastName'], item['balance']) , axis=1)

def savingsChecker():
    isSavingsChecker = True
    while isSavingsChecker:
        try:
            userInput = input("Welcome to the Banking Service.\n"
            "What would you like to do?:\n"
            "Check Balance: 'CB'\n"
            "Withdraw Money: 'WM'\n"
            "Deposit Money: 'DM'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                isSavingsChecker = False
                break
        except:
            pass
        else:
            pass
        finally:
            pass

def checkingChecker():
    isCheckingChecker = True
    while isCheckingChecker:
        try:
            userInput = input("Welcome to the Banking Service.\n"
            "What would you like to do?:\n"
            "Check Balance: 'CB'\n"
            "Withdraw Money: 'WM'\n"
            "Deposit Money: 'DM'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                isCheckingChecker = False
                break
        except:
            pass
        else:
            pass
        finally:
            pass

def loanChecker():
    isLoanChecker = True
    while isLoanChecker:
        try:
            userInput = input("Welcome to the Banking Service.\n"
            "What would you like to do?:\n"
            "Check Balance: 'CB'\n"
            "Pay On Loan: 'PL'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                isLoanChecker = False
                break
        except:
            pass
        else:
            pass
        finally:
            pass

def loanChecker():
    isLoanChecker = True
    while isLoanChecker:
        try:
            userInput = input("Welcome to the Banking Service.\n"
            "What would you like to do?:\n"
            "Check Balance: 'CB'\n"
            "Pay On Loan: 'PL'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                isLoanChecker = False
                break
        except:
            pass
        else:
            pass
        finally:
            pass

isProgramGoing = True

while isProgramGoing:
    try:
        userInput = input("Welcome to the Banking Service.\n"
            "What would you like to do?:\n"
            "Become a new member: 'NM'\n"
            "Check savings account: 'SA'\n"
            "Check checking account: 'CA'\n"
            "Check credit card: 'CC'\n"
            "Check loan: 'CL'\n"
            "Apply today!: 'AP'\n"
            "Exit: 'EX'\n"
        )
        if userInput.lower() == "ex" or userInput.lower() == "":
            isProgramGoing = False
            break
        elif userInput.lower() == "sa":
            savingsChecker()
        elif userInput.lower() == "ca":
            savingsChecker()
    except:
        pass
    else:
        userInput = input("Please enter in a valid two character choice from the list. Thank you.")
        continue
    finally:
        pass

print("Thank you for using our banking app. Have a nice day.")