#!/usr/bin/env python3

class Customers:
    """
    Customer class captures a customer for the bank.

    Attributes
    --------
    idCus: int
        ID of a customer.

    firstName: str
        First name of a customer.

    lastName: str
        Last name of a customer.

    address: str
        Address of a customer.
    """

    def __init__(self, new_id, firstName, lastName, address):
        self.idCus = new_id
        self.firstName = firstName
        self.lastName = lastName
        self.address = address

    @property                                                               #id Property Creation
    def idCus(self):
        """int: ID of a customer."""
        return self._idCus
    
    @idCus.setter
    def idCus(self, new_id):
        self._idCus = new_id

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

    @property                                                               #address Property Creation
    def address(self):
        """str: Address of a customer."""
        return self._address

    @address.setter
    def address(self, address):
        if not address:
            raise ValueError("Address was empty. Please enter a valid address.")
        else:
            self._address = address

    def __repr__(self):
        return "Customers(\nidCus = {idCus}\nfirstName = '{firstName}'\nlastName = '{lastName}'\naddress = '{address}'\n)".format(
            idCus = self.idCus, firstName = self.firstName, 
            lastName = self.lastName, address = self.address
        )
