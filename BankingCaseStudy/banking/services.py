#!/usr/bin/env python3

from accounts import Accounts

class Services(Accounts):
    """
    Services class that can create an account, view balance, deposit, and withdraw money.

    Attributes
    --------
    acc_type: str
        Type of account: loans or credit card.

    acc_num: int
        Account number of loan or credit card number.

    firstName: str
        First name of an account owner.

    lastName: str
        Last name of an account owner.

    balance: float
        Balance or credit limit of account.
    
    repay: float
        How much is remaining on the loan or current credit card statement.
    """
    def __init__(self, new_acc_type, new_acc_num, new_firstName, new_lastName, new_balance, need_to_repay):
        Accounts.__init__(self, new_acc_type, new_acc_num, new_firstName, new_lastName, new_balance)
        self.repay = need_to_repay

    @property                                                               #pay Property Creation
    def repay(self):
        """int: ID of a customer."""
        return self._repay
    
    @repay.setter
    def repay(self, repay):
        self._repay = repay

    @Accounts.acc_type.getter                                               #acc_type Property Creation
    def acc_type(self):
        """str: First name of a customer."""
        return self._acc_type

    @Accounts.acc_type.setter
    def acc_type(self, acc_type):
        if not acc_type:
            raise ValueError("No account type chosen. Please choose one of two options: 'loans' or 'credit card'.")
        elif acc_type not in ("loans", "credit card"):
            raise ValueError("Please choose one of two options: 'loans' or 'credit card'.")
        else:
            self._acc_type = acc_type
    
    @Accounts.acc_num.getter                                                #acc_num Property Creation
    def acc_num(self):
        """int: ID of a customer."""
        return self._acc_num
    
    @Accounts.acc_num.setter
    def acc_num(self, new_acc_num):
        if self._acc_type == "loans":
            self._acc_num = new_acc_num
        elif self._acc_type == "credit card":
            if len(str(new_acc_num)) != 16:
                raise ValueError(str(len(str(new_acc_num))) + " Account number must be 16 digits.")
            else:
                self._acc_num = new_acc_num

    def pay_on(self, amount):
        """
        Pay On takes an amount and subtracts it from the class's remaining loan/credit card balance.

        Parameters
        ----------
        amount: int
            How much needs to be removed from balance.

        Returns
        -------
        Updates the class's remaining loan/credit card balance.
        """
        if self._repay == 0.0:
            print("Your remaining balance is at $0. You have nothing to pay.")
        else:
            self._repay = self._repay - amount
            if self._repay <= 0.0:
                self._repay = 0.0
                print("Your remaining balance is at $0. You paid off your balance.")
            else:
                print("You still have ${0} to pay on {1}.".format(self._repay, self._acc_type))
    
    def __repr__(self):
        return "Services extends Accounts(\nacc_type = '{acc_type}'\nacc_num = {acc_num}\nfirstName = '{firstName}'\nlastName = '{lastName}'\nbalance = {balance}\nrepay = {repay}\n)".format(
            acc_type = self.acc_type, acc_num = self.acc_num, firstName = self.firstName, lastName = self.lastName,
            balance = self.balance, repay = self.repay
        )
