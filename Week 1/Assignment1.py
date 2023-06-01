# rian-kh
# Coursera: Introduction to Data Science in Python (University of Michigan)
# Week 1: Assignment 1

# Part A
# Find a list of all of all of the names in the following string using regex.

import re

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # Your code here
    list = re.findall("[A-Z]{1}[a-z]+(?=[^.])", simple_string)
    return list



# Part B
# The dataset file in assets/grades.txt contains a line separated list of people
# with their grade in a class. Create a regex to generate a list of just those
# students who received a B in the course.

def grades():

    # Your code here
    with open("assets/grades.txt", "r") as file:
        grades = file.read()

    list = re.findall(".+(?=: B)", grades)
    return list



# Part C
# Consider the standard web log file in assets/logdata.txt.
# This file records the access a user makes when visiting a web page (like this one!).
# Each line of the log has the following items:
#   a  host (e.g., '146.204.224.152')
#   a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
#   the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
#   the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
#
# example_dict = {"host":"146.204.224.152",
#                 "user_name":"feest6811",
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}

def logs():

    # Your code here

    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()

    pattern = """
    (?P<host>[\d\.]+)
    (\s-\s)
    (?P<user_name>[^\s]+)
    (\s\[)
    (?P<time>.+(?=\]))
    (]\s\")
    (?P<request>.+(?=\"))
    """

    list = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        list.append(item.groupdict())

    return list



