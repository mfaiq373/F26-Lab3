# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file

mylist = []
while len(mylist) < 6 :
   num = int(input("please enter any number: "))
   print("user entered: ",num)
   mylist.append(num*10)
print(mylist)
print(mylist[::-1])