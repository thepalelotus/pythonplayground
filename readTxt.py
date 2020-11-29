#!/usr/bin/python3.8

import sys

filePath = sys.argv[1]

def readFile():
	try:
		file = open(filePath, 'r')
		fileRead = file.read()
		print(fileRead)

	except:
		print("Something went wrong!")

if __name__ == "__main__":
	readFile()
