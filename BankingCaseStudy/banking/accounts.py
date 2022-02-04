#!/usr/bin/env python3

class Accounts(object):
    """
    Account class that can create an account, view balance, deposit, and withdraw money.

    Attributes
    --------
    acc_type: str
        Type of account: savings or checking.

    acc_num: int
        Account number of a customer.

    firstName: str
        First name of an account owner.

    lastName: str
        Last name of an account owner.

    balance: float
        Balance of account.
    """
    def __init__(self, new_acc_type, new_acc_num, new_firstName, new_lastName, new_balance):
        self.acc_type = new_acc_type
        self.acc_num = new_acc_num
        self.firstName = new_firstName
        self.lastName = new_lastName
        self.balance = new_balance

    @property                                                               #acc_type Property Creation
    def acc_type(self):
        """str: First name of a customer."""
        return self._acc_type

    @acc_type.setter
    def acc_type(self, acc_type):
        if not acc_type:
            raise ValueError("No account type chosen. Please choose one of two options: 'savings' or 'checking'.")
        elif acc_type not in ["savings", "checking"]:
            raise ValueError("Please choose one of two options: 'savings' or 'checking'.")
        else:
            self._acc_type = acc_type

    @property                                                               #acc_num Property Creation
    def acc_num(self):
        """int: ID of a customer."""
        return self._acc_num
    
    @acc_num.setter
    def acc_num(self, acc_num):
        self._acc_num = acc_num

    @property                                                               #firstName Property Creation
    def firstName(self):
        """str: First name of a customer."""
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        if not firstName:
            raise ValueError("First name was empty.")
        elif len(firstName) > 25:
            raise ValueError("First name was too long.")
        else:
            self._firstName = firstName
            
    @property                                                               #lastName Property Creation
    def lastName(self):
        """str: Last name of a customer."""
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        if not lastName:
            raise ValueError("Last name was empty.")
        elif len(lastName) > 25:
            raise ValueError("Last name was too long.")
        else:
            self._lastName = lastName

    @property                                                               #balance Property Creation
    def balance(self):
        """int: Balance of account."""
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        """
        Withdrawl takes an amount and subtracts it from the class's balance.

        Parameters
        ----------
        amount: int
            How much needs to be removed from balance.

        Returns
        -------
        Updates the class's balance.
        """
        if self._balance == 0.0:
            print("Your balance is at $0. You cannot withdraw money.")
        elif self._balance < 0.0:
            print("You have withdrawn your account. A $10 fee has been added.")
            self._balance = self._balance - (amount + 10)
        else:
            self._balance = self._balance - amount

    def deposit(self, amount):
        """
        Deposit takes an amount and adds it to the class's balance.

        Parameters
        ----------
        amount: int
            How much needs to be added to balance.

        Returns
        -------
        Updates the class's balance.
        """
        self._balance = self._balance + amount

    def __repr__(self):
        return "Accounts(\nacc_type = '{acc_type}'\nacc_num = {acc_num}\nfirstName = '{firstName}'\nlastName = '{lastName}'\nbalance = {balance}\n)".format(
            acc_type = self.acc_type, acc_num = self.acc_num, firstName = self.firstName, 
            lastName = self.lastName, balance = self.balance
        )