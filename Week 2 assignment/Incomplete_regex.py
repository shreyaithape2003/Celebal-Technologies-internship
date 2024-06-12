"""You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format
The first line contains integer , the number of test cases.
The next  lines contains the string .

Output Format
Print "True" or "False" for each test case without quotes.

Sample Input
2
.*\+
.*+
Sample Output
True
False"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


if __name__ == "__main__":
    # Read number of test cases
    n = int(input().strip())

    # Process each test case
    for _ in range(n):
        regex_pattern = input().strip()
        if is_valid_regex(regex_pattern):
            print("True")
        else:
            print("False")
