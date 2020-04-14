#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand') # A list of all the operands

# Convert list of strings to integers and then add them together 
try: 
    total = sum(map(int, operands))
    body = "Your total is: {}".format(total)
except (ValueError, TypeError):
    body = "Unable to calculate a sum, please provide interger operands."

print("Content-type: text/plain")
print()
print(body)
