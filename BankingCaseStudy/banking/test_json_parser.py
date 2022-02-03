#!/usr/bin/env python3

import json_parser

def test_json_parser():
    """
    Basic test cases for json_parser
    """

    result = json_parser.json_parser()
    assert type(result) is tuple

