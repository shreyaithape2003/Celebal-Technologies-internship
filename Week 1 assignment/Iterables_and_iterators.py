"""The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.
You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.
Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format
The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.
All the letters in the list are lowercase English letters.

Sample Input
4 
a a c d
2
Sample Output
0.8333"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


def calculate_probability(n, letters, k):
    # Generate all combinations of indices of length k
    indices = list(range(n))
    combs = list(combinations(indices, k))

    # Count the combinations that contain at least one 'a'
    count = 0
    for comb in combs:
        if any(letters[i] == "a" for i in comb):
            count += 1

    # Calculate the probability
    probability = count / len(combs)

    return probability


# Read input
n = int(input())
letters = input().split()
k = int(input())

# Calculate and print the probability
probability = calculate_probability(n, letters, k)
print(f"{probability:.4f}")
