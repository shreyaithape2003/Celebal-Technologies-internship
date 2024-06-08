"""In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
For a better understanding of the problem, check the explanation.

Input Format
A single line of input consisting of the string .

Output Format
A single line of output consisting of the modified string.

Constraints
All the characters of  denote integers between  and .

Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)"""

from itertools import groupby

def compress_string(s):
    # Initialize an empty list to store the result
    result = []
    
    # Group consecutive occurrences of characters
    for key, group in groupby(s):
        count = len(list(group))
        character = int(key)
        
        # Append the formatted result to the list
        if count > 0:
            result.append(f"({count}, {character})")
        else:
            result.append(f"(0, {character})")
    
    # Join the result list into a single string with space separation
    output = " ".join(result)
    
    # Print the output
    print(output)

# Sample Input
s = "1222311"

# Call the function with the sample input
compress_string(s)
