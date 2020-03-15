#! /usr/bin/python3

import re, sys

if (len(sys.argv) < 2):
	print("No file specified.")
	sys.exit()

phoneRegex = re.compile("""
((((\d{3})|(\(\d{3}\)))(-|.))?	#area code with or without parentheses (optional)
\d{3}						#middle 3 digits
(-|.)						#dash or dot
\d{4})						#last 4 digits
""", re.VERBOSE)

emailRegex = re.compile("""
[a-zA-Z._]+				#name part of email
@						#@ symbol
[a-zA-Z._]+				#domain part of email
.						#dot
[a-zA-Z]+
""", re.VERBOSE)

try:
	f = open(sys.argv[1], "r")
except:
	print("File '" + sys.argv[1] + "' does not exist.")
	sys.exit()

input = f.read()

foundNumbers = re.findall(phoneRegex, input)
foundEmails = re.findall(emailRegex, input)

numbers = []
for number in foundNumbers:
	numbers.append(number[0])

print("\n".join(numbers) + "\n" + "\n".join(foundEmails))
f.close()