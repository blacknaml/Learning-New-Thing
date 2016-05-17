#!/usr/bin/python

from __future__ import print_function
import os, py_compile

def main():
	os.chdir("/home/ellaits/Developments/python")
	py_compile.compile("hello.py")
	print("File hello.pyc telah dibuat ... ")
	os.system("read");

	if __name__ == "__main__":
		main()
