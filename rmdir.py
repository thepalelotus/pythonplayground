#!/usr/bin/python3.8

import os, sys

def rmDir():
	i = sys.argv[1]
	try:
		os.rmdir(i)
	except:
		print("Something went wrong!")
		sys.exit[1]

if __name__ == "__main__":
	rmDir()
