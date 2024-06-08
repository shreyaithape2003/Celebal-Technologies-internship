"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example
The query_name is 'beta'. beta's average score is .

Input Format
The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0
56.00"""

# Read the number of students
n = int(input())

# Initialize an empty dictionary to store the student records
student_marks = {}

# Read each student's data
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

# Read the name of the student to query
query_name = input()

# Compute the average of the marks for the queried student
if query_name in student_marks:
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    # Print the average with 2 decimal places
    print(f"{average:.2f}")
else:
    # If the student's name is not found, print a message (this part is optional based on problem constraints)
    print("Student not found")
