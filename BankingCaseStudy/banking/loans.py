from json_parser import json_parser
from services import Services
import json


class Loans:

    def __init__(self):
        self.df_loans = json_parser('data/loans.json')
        self.loansHolder = [loan for loan in self.df_loans[0].apply(lambda item: Services("loans", item['loan_id'], item['firstName'], item['lastName'], item['balance'], item['need_to_pay']), axis=1)]


    def loansChecker(self):
        isLoansChecker = True
        while isLoansChecker:
            userInput = input("Check loans was selected.\n"
            "What would you like to do?:\n"
            "Check Balance: 'CB'\n"
            "Apply for a Loan: 'AL'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                self.convertToJson()
                isLoansChecker = False
                break
            elif userInput.lower() == 'cb':
                self.checkBalance()
            elif userInput.lower() == 'al':
                self.loanApply()

    def checkBalance(self):
        isBalChecker = True
        while isBalChecker:
            loanNum = input("Check statement was selected.\n"
            "Please enter your 5-digit account number: ")
            try:
                val = int(loanNum)
                try:
                    if len(str(val)) == 5:
                        lastName = input("Please enter your last name: ")
                        checker = [loan for loan in self.loansHolder if loan.acc_num == int(loanNum) and loan.lastName.lower() == lastName.lower()]
                        if not checker:
                            userInput = input("You were not found in our system.\n" 
                            "Would you like to apply for a credit card? Y or N: ")
                            if userInput.lower() == 'y':
                                self.loanApply()
                                isBalChecker = False
                                break
                            else:
                                input("Returning to the previous menu. (Press enter to continue.)")
                                isBalChecker = False
                                break
                        elif checker:
                            print("Current balance: ${balance}.".format(balance = checker[0].repay))
                            if checker[0].repay > 0.0:
                                userInput = input("Would you like to pay on your balance? Y or N: ")
                                if userInput.lower() == 'y':
                                    self.payLoan(checker[0])
                                    input("Returning to the previous menu. (Press enter to continue.)")
                                    isBalChecker = False
                                    break
                                else:
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
                    "If you are not currently a member, would you like to apply for a $5000 loan? Y or N: ")
                    if userInput.lower() == 'y':
                        self.loanApply()
                        isBalChecker = False
                        break
            except ValueError:
                userInput = input("Please enter a valid 5-digit account number.\n"
                "If you are not currently a member, would you like to apply for a $5000 loan? Y or N: ")
                if userInput.lower() == 'y':
                    self.loanApply()
                    isBalChecker = False
                    break

    def loanApply(self):
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            checker = [cc for cc in self.loansHolder if cc.firstName.lower() == firstName.lower() and cc.lastName.lower() == lastName.lower()]
            if checker:
                print("Hello {firstName} {lastName}, you already have a loan with us.\n Current balance: ${balance}."
                .format(firstName = firstName, lastName = lastName, balance = checker[0].repay))
                if checker[0].repay > 0.0:
                    userInput = input("Would you like to pay on your balance? Y or N: ")
                    if userInput.lower() == 'y':
                        self.payLoan(checker[0])
                        input("Returning to the previous menu. (Press enter to continue.)")
                    else:
                        input("Returning to the previous menu. (Press enter to continue.)")
                else:
                    input("Returning to the previous menu. (Press enter to continue.)")
            else:
                acc_type = "loans"
                loanNum = int(self.loansHolder[-1].acc_num) + 1
                loanLimit = 5000.00
                need_to_pay = 5000.00
                self.loansHolder.append(Services(acc_type, loanNum, firstName, lastName, loanLimit, need_to_pay))
                print("Thank you {firstName} {lastName}. You have been approved!\n" 
                "Please write down the information below for your records.\n"
                "Loan Account Number: ${loanNum}\n"
                "Loan Amount: ${loanLimit}.".format(firstName = firstName, lastName = lastName, loanNum = loanNum, loanLimit = loanLimit)
                )
                input("Please press enter to continue.")

    def payLoan(self, person):
        while True:
            amount = input("Please enter the amount you would like to pay: ")
            try:
                val = float(amount)
                try:
                    if float(val) > 0:
                        self.loansHolder.remove(person)
                        person.pay_on(val)
                        self.loansHolder.append(person)
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    amount = input("Please enter a valid amount.\n You need to repay: ${repay}, or would you like to quit? Y or N: ".format(repay = person.repay))
                    if amount.lower() == "y" or amount.lower() == "":
                        input("Please press enter to continue.")
                        break
            except TypeError:
                amount = input("Please enter a valid amount.\n You need to repay: ${repay}, or would you like to quit? Y or N: ".format(repay = person.repay))
                if amount.lower() == "y" or amount.lower() == "":
                    input("Please press enter to continue.")
                    break

    def convertToJson(self):
        sorted(self.loansHolder, key = lambda i: i['acc_num'])
        ccDict = {"loans" : [{"loan_id" : int(loan.acc_num), "firstName" : loan.firstName, "lastName" : loan.lastName, "balance": float(loan.balance), "need_to_pay" : float(loan.repay)} for loan in self.loansHolder]}

        with open('data/loans.json', 'w') as outfile:
            json.dump(ccDict, outfile)