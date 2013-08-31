#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 tusharmakkar08 <tusharmakkar08@tusharmakkar08-Satellite-C660>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

""" Importing Modules """

import csv

""" Main Code Starts Here """

def selectf(listvar1,var2):
	try:
		filename=var2+".csv"
		with open(filename):
			sreader=csv.reader(open(filename,"rb"))
			var1=listvar1.strip().split(',')
			if var1[0]=="*":
				co=0
				for row in sreader:
					if co!=0:
						print row
					co+=1
			else:
				co=0
				for row in sreader:
					if co==0:
						row_name=row
						break
				co=0
				kinglist=[]
				for i in row_name:
					for j in var1:
						#print i,j
						if i==j:
						#	print "lol",i,j
							kinglist.append(co)
					co+=1
#				print kinglist
				if len(kinglist)==0:
					print "Column Not Found"
				else:
					for row in sreader:
						for j in kinglist:
							print row[j],
						print
	except IOError:
		print "File Not Found"
		

def main():
	while 1:
		a=raw_input("Enter Regular Expression Statement and -1 for exit \n").strip().split()
		if a[0]=="-1":
			break
		L=len(a);i=0
		while i<L:
			if a[i]=="SELECT"or"select"or"Select" and a[i+2]=="FROM"or"from"or"From":
				var1=a[i+1]
				var2=a[i+3]
				selectf(var1,var2)
				i+=3
			i+=1
	return 0

if __name__ == '__main__':
	main()

