#!/usr/bin/python3.8

import os
import sys

def mkDir():
	i = sys.argv[1]
	try:
		os.mkdir(i)
	except:
		print("Something went wrong!")

if __name__ == "__main__":
	mkDir()
