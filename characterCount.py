#! /usr/bin/python3

import pprint
print("Type a message to count letters from:")
message = input()
count = {}
	
for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1
pprint.pprint(count)