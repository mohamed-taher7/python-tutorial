#regex or regular expression: Regular expressions are extremely useful in extracting information from text such as code, log files, spreadsheets, or even documents.
"""
it's better to take tutorial if you're new to it
https://regexone.com/
"""

import re #regex module

Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 


>>>>>>>>>>>>>>>>>>>>>>here
