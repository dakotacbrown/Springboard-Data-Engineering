from json_parser import json_parser
from services import Services
import json
import random
import string


class CreditCard:

    def __init__(self):
        self.df_credit_cards = json_parser('data/credit_cards.json')
        self.ccHolder = [cc for cc in self.df_credit_cards[0].apply(lambda item: Services("credit card", item['cc_num'], item['firstName'], item['lastName'], item['credit_limit'], item['need_to_pay']), axis=1)]


    def ccChecker(self):
        isCcChecker = True
        while isCcChecker:
            userInput = input("Check credit card was selected.\n"
            "What would you like to do?:\n"
            "Check Statement: 'CS'\n"
            "Apply for Card: 'AC'\n"
            "Main Menu: 'MM'\n"
            )
            if userInput.lower() == "mm" or userInput.lower() == "":
                self.convertToJson()
                isCcChecker = False
                break
            elif userInput.lower() == 'cs':
                self.checkStatement()
            elif userInput.lower() == 'ac':
                self.ccApply()

    def checkStatement(self):
        isCsChecker = True
        while isCsChecker:
            ccNum = input("Check statement was selected.\n"
            "Please enter your 16-digit credit card number: ")
            if len(str(ccNum)) != 16:
                userInput = input("Please enter a valid 16-digit credit card number.\n"
                "If you are not currently a member, would you like to apply for a credit card? Y or N (If not, press enter.): ")
                if userInput.lower() == 'y':
                    self.ccApply()
                    isCsChecker = False
                    break
                elif userInput.lower() != 'n':
                    input("Returning to the previous menu. (Press enter to continue.)")
                    isCsChecker = False
                    break
            else:
                lastName = input("Please enter your last name: ")
                checker = [cc for cc in self.ccHolder if cc.acc_num == int(ccNum) and cc.lastName.lower() == lastName.lower()]
                if not checker:
                    userInput = input("You were not found in our system.\n" 
                    "Would you like to apply for a credit card? Y or N: ")
                    if userInput.lower() == 'y':
                        self.ccApply()
                        isCsChecker = False
                        break
                    else:
                        input("Returning to the previous menu. (Press enter to continue.)")
                        isCsChecker = False
                        break
                elif checker:
                    print("Current statement balance: ${balance}.".format(balance = checker[0].repay))
                    if checker[0].repay > 0.0:
                        userInput = input("Would you like to pay on your balance? Y or N: ")
                        if userInput.lower() == 'y':
                            self.payCard(checker[0])
                            input("Returning to the previous menu. (Press enter to continue.)")
                            isCsChecker = False
                            break
                        else:
                            input("Returning to the previous menu. (Press enter to continue.)")
                            isCsChecker = False
                            break
                    else:
                        input("Returning to the previous menu. (Press enter to continue.)")
                        break


    def ccApply(self):
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            checker = [cc for cc in self.ccHolder if cc.firstName.lower() == firstName.lower() and cc.lastName.lower() == lastName.lower()]
            if checker:
                print("Hello {firstName} {lastName}, you already have a card with us.\n Current statement balance: ${balance}."
                .format(firstName = firstName, lastName = lastName, balance = checker[0].repay))
                if checker[0].repay > 0.0:
                    userInput = input("Would you like to pay on your balance? Y or N: ")
                    if userInput.lower() == 'y':
                        self.payCard(checker[0])
                        input("Returning to the previous menu. (Press enter to continue.)")
                    else:
                        input("Returning to the previous menu. (Press enter to continue.)")
                else:
                    input("Returning to the previous menu. (Press enter to continue.)")
            else:
                acc_type = "credit card"
                ccNum = '4' + ''.join(random.choices(string.digits, k=15))
                creditLimit = 1500.00
                need_to_pay = 0.0
                self.ccHolder.append(Services(acc_type, int(ccNum), firstName, lastName, creditLimit, need_to_pay))
                print("Thank you {firstName} {lastName}. You have been approved!\n" 
                "Please write down the information below for your records.\n"
                "Credit Card Number: {ccNum}\n"
                "Credit Limit: ${creditLimit}.".format(firstName = firstName, lastName = lastName, ccNum = ccNum, creditLimit = creditLimit)
                )
                input("Please press enter to continue.")

    def payCard(self, person):
        amount = input("Please enter the amount you would like to pay: ")
        while float(amount) < 0 or not isinstance(amount, float):
            amount = input("Please enter a valid amount.\n You need to repay: ${repay}, or would you like to quit? Y or amount: ".format(repay = person.repay))
            if amount.lower() == "y" or amount.lower() == "":
                break
        if not isinstance(float(amount), float):
            input("Please press enter to continue.")
        else:
            self.ccHolder.remove(person)
            person.pay_on(float(amount))
            self.ccHolder.append(person)

    def convertToJson(self):
        ccDict = {"credit_cards" : [{"cc_num" : int(cc.acc_num), "firstName" : cc.firstName, "lastName" : cc.lastName, "credit_limit": float(cc.balance), "need_to_pay" : float(cc.repay)} for cc in self.ccHolder]}

        with open('data/credit_cards.json', 'w') as outfile:
            json.dump(ccDict, outfile)