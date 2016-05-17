#!/usr/bin/python

from __future__ import print_function
import os

def main():
	bahasa = ['Python', 'Ruby', 'Perl', 'PHP']
	for b in bahasa:
		print(b)

	os.system("read -p '$*'");

if __name__ == "__main__":
	main()
