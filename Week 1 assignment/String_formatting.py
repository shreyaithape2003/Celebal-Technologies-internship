"""Given an integer, , print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary

Function Description
Complete the print_formatted function in the editor below.
print_formatted has the following parameters:
int number: the maximum value to print

Prints
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format
A single integer denoting .

Sample Input
17
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001"""


def print_formatted(number):
    # Determine the width for formatting, based on the binary representation of the number
    width = len(bin(number)) - 2

    # Iterate over each number from 1 to number
    for i in range(1, number + 1):
        # Format the number in decimal, octal, hexadecimal, and binary
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        # Print the formatted string with appropriate width
        print(f"{dec:>{width}} {octa:>{width}} {hexa:>{width}} {bina:>{width}}")


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
