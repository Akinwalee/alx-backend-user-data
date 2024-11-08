#!/usr/bin/env python3
"""
Filter and replace PII data
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    Filter the given by obfustacating the sepcified fields
    """

    pattern = r'(?<={})({}=[^{}]*)(?={})'.format(
                separator, '|'.join(fields), separator, separator)
    repl = r'\1{}'.format(redaction)
    new_str = re.sub(pattern, repl, message)

    return (new_str)
