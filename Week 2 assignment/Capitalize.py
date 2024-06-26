"""You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name, .

Constraints
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format
Print the capitalized string, .

Sample Input
chris alan
Sample Output
Chris Alan"""

#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    # Capitalize the first letter of each word without removing extra spaces
    capitalized_name = " ".join(word.capitalize() for word in s.split(" "))
    return capitalized_name


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
