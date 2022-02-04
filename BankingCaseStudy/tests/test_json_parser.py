#!/usr/bin/env python3

from json_parser import json_parser

def test_default():
    """
    Test to see if parser works with default value.
    """
    result_employees = json_parser('data/employees.json')
    assert result_employees

def test_size_set():
    """
    Test to see if parser works with size value on non-nested json.
    """
    result_customers = json_parser('data/customers.json', size=1)
    assert result_customers

def test_size_set():
    """
    Test to see if parser works with size value on single nested json.
    """
    result_services = json_parser('data/services.json', size=2)
    assert result_services

def test_type_and_length():
    """
    Test to see right return type and not empty.
    """
    result_customers = json_parser('data/customers.json')
    result_employees = json_parser('data/employees.json', size =1)
    result_accounts = json_parser('data/accounts.json', size=2)
    result_holder = [result_customers, result_employees, result_accounts]

    #test to see if you get the correct return type
    assert (type(result) is tuple for result in result_holder)

    #test to see if you get an empty tuple
    assert (len(result) > 0 for result in result_holder)