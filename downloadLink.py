#! /usr/bin/python3

import requests, sys, re

if len(sys.argv) < 1:
	print("No link specified")
	sys.exit()

try:
	res = requests.get(sys.argv[1])
	res.raise_for_status()
except:
	print("File was not found.")
	sys.exit()

print(re.findall(".*/(.*?)$", sys.argv[1])[0])
file = open(re.findall(".*/(.*?)$", sys.argv[1])[0], "wb")
for chunk in res.iter_content(1000):
	file.write(chunk)
file.close()