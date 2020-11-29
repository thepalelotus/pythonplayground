#!/usr/bin/python3.8

import sys

filePath = sys.argv[1]

userInput = input("What do you wish to write?\n")

def writeFile():
	try:
		file = open(filePath, 'w')
		file.write(userInput)
	except:
		print("Something went wrong!")

if __name__ == "__main__":
	writeFile()
