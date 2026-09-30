# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][1] 
e1 = matrix[0][1]
e2 = matrix[2][2]

print("the element at second row and second colomn is: ",element)
print("the element at first row and second colomn is: ",element)
print("the element at third row and third colomn is: ",element)

for i in matrix:
    print(i)

for i in range(3):
    print(matrix[i])
