#!/usr/bin/env python3

import pandas as pd

def json_parser(json_path, size=1):
    """
    Parses various json files and turns them into pandas data frames.

    Parameters
    ----------
    json_path: str
        Takes the path to the json file you want parsed.
    size: int, optional
        Takes how nested a json file is, this only works for size 1 and 2.

    Returns
    -------
    Tuple of pandas dataframes from the json file that was read.
    """

    if json_path[-5:] != '.json':                                                           #Checks if received correct file type
        raise ValueError("Wrong file type given. Function only accepts JSON.")
    else:
        if size > 2 or size < 1:                                                            #If size value is too small or large throw an error
            raise ValueError("Size can only be between 1 and 2 for this data parser.")
        elif size == 1:
            data_from_1d_json = pd.read_json(json_path)                                     #Get the json info from the file for size=1
            if type(data_from_1d_json.iloc[0][0]) == list:                                  #If a list is received, wrong size given
                raise ValueError("Size parameter too small, please specify 2 instead.")
            else:
                json_1d_normalized = pd.json_normalize(data_from_1d_json.iloc[:, 0])
                return tuple([json_1d_normalized])                                          #Parse the column from the dataframe and return
        elif size == 2:
            data_from_2d_json = pd.read_json(json_path)                                     #Get the json info from the file for size=2
            if type(data_from_2d_json.iloc[0][0]) == dict:                                  #If dictionary received, wrong size given
                raise ValueError("Size parameter too large, please specify 1 instead.")
            else:
                json_2d_normalized1 = pd.json_normalize(data_from_2d_json.iloc[0][0])
                json_2d_normalized2 = pd.json_normalize(data_from_2d_json.iloc[1][0])
                return tuple([json_2d_normalized1, json_2d_normalized2])                    #Parse the two columns from the dataframe and return