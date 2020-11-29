#!/usr/bin/python3.8

import sys, os

def listDir():
	i = sys.argv [ 1 ]
	try:
		lsdir = os.listdir ( i )
		print( "\n".join ( lsdir ) )
	except:
		print( "Something went wrong!" )

if __name__ == "__main__":
	listDir()
