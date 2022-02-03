#!/usr/bin/env python3

import pandas as pd

def json_parser():
    """
    Parses various json files and turns them into pandas data frames.

    Returns
    -------
    Tuple of panda dataframes
    """
    
    df_employees = pd.json_normalize(pd.read_json('data/employees.json')['employees'])
    df_customers = pd.json_normalize(pd.read_json('data/customers.json')['customers'])
    df_savings = pd.json_normalize(pd.read_json('data/accounts.json')['accounts']['savings'])
    df_checking = pd.json_normalize(pd.read_json('data/accounts.json')['accounts']['checking'])
    df_loans = pd.json_normalize(pd.read_json('data/services.json')['services']['loans'])
    df_credit = pd.json_normalize(pd.read_json('data/services.json')['services']['credit_cards'])

    return tuple([df_employees, df_customers, df_savings, df_checking, df_loans, df_credit])
