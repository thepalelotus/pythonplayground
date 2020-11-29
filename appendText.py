#!/usr/bin/python3.8

import sys

filePath = sys.argv[1]

userInput = input("What do you wish to write?\n")

def appendFile():
	try:
		file = open(filePath, 'a')
		file.write("\n")
		file.write(userInput)
	except:
		print("Something went wrong!")

if __name__ == "__main__":
	appendFile()
