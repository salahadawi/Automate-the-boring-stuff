#! /usr/bin/python3

import webbrowser, sys

if len(sys.argv) < 1:
	print("No address specified.")
	sys.exit()
address = " ".join(sys.argv[1:])
addressURL = "http://google.com/maps/place/" + address
webbrowser.open(addressURL)