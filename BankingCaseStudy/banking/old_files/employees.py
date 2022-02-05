#!/usr/bin/env python3

class Employees:
    """
    Employee class captures an employee for the bank.

    Attributes
    --------
    idEmp: int
        ID of an employee.

    firstName: str
        First name of an employee.

    lastName: str
        Last name of an employee.

    position: str
        Position of an employee.

    activity: bool
        If the employee currently works for the company.

    salary: float
        Salary of employee.

    """

    def __init__(self, new_id, firstName, lastName, position, activity, salary):
        self.idEmp = new_id
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.activity = activity
        self.salary = salary

    @property                                                               #id Property Creation
    def idEmp(self):
        """int: ID of an employee"""
        return self._idEmp

    @idEmp.setter
    def idEmp(self, new_id):
        if new_id <= 0:
            raise ValueError("Please enter a valid ID.")
        else:
            self._idEmp = new_id

    @property                                                               #firstName Property Creation
    def firstName(self):
        """str: First name of employee."""
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        if not firstName:
            raise ValueError("First name was empty")
        elif len(firstName) > 25:
            raise ValueError("First name was too long")
        else:
            self._firstName = firstName
    
    @property                                                               #lastName Property Creation
    def lastName(self):
        """str: Last name of employee."""
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        if not lastName:
            raise ValueError("Last name was empty")
        elif len(lastName) > 25:
            raise ValueError("Last name was too long")
        else:
            self._lastName = lastName

    @property                                                               #position Property Creation
    def position(self):
        """str: Position name of employee."""
        return self._position

    @position.setter
    def position(self, position):
        if not position:
            raise ValueError("Please enter in a position.")
        else:
            self._position = position

    @property                                                               #activity Property Creation
    def activity(self):
        """bool: If the employee currently works for the company."""
        return self._activity
    
    @activity.setter
    def activity(self, activity):
        self._activity = activity

    @property                                                               #salary Property Creation
    def salary(self):
        """float: Salary of employee"""
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary <= 0:
            raise ValueError("Please enter a valid salary.")
        else:
            self._salary = salary

    def __repr__(self):
        return "Employees(\nidEmp = {idEmp}\nfirstName = '{firstName}'\nlastName = '{lastName}'\nposition = '{position}'\nactivity = {activity}\nsalary = {salary}\n)".format(
            idEmp = self.idEmp, firstName = self.firstName, lastName = self.lastName, 
            position = self.position, activity = self.activity, salary = self.salary
        )