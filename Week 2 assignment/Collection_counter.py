"""A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
Task is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Output Format
Print the amount of money earned by .

Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output
200"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter


def compute_earnings(shoe_sizes, customer_requests):
    # Create a Counter to store the inventory of shoes
    inventory = Counter(shoe_sizes)
    earnings = 0

    # Process each customer's request
    for size, price in customer_requests:
        if inventory[size] > 0:  # If the shoe is available
            earnings += price
            inventory[size] -= 1  # Decrease the inventory count

    return earnings


if __name__ == "__main__":
    # Read input
    n = int(input())
    shoe_sizes = list(map(int, input().split()))
    m = int(input())
    customer_requests = [tuple(map(int, input().split())) for _ in range(m)]

    # Compute and print the total earnings
    result = compute_earnings(shoe_sizes, customer_requests)
    print(result)
