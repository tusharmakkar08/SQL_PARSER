#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  aggregate.py
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
import os
import logging
import collections

""" Main Code Starts Here """

try:
	open('example1.log', 'w').close()
except IOError:
	pass
	
logging.basicConfig(filename='example1.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

def groupby(att,filen):
	sreader=csv.reader(open(filen,"rb"))
	co=0
	for row in sreader:
		if co==0:
			row_name=row
			break
	sreader=csv.reader(open(filen,"rb"))
	for i in row_name:
		if i==att:
			break
		co+=1
	sreader=csv.reader(open(filen,"rb"))
	k={}
	for row in sreader:
		try:
			k[row[co]].append(row)
		except KeyError :
			k[row[co]]=[]
			k[row[co]].append(row)
	od = collections.OrderedDict(sorted(k.items()))
	lo=raw_input("Do you want to see output ? Y/N \n")
	if(lo=='Y'):
		print od
	swriter=csv.writer(open("tring.csv","wb"))
	for ke,v in od.iteritems():
		swriter.writerow(v)
	while(1):
		tik=raw_input("1 for printing count for each group and 0 for break\n")
		if(tik=='0'):
			break;
		else:
			for ke,v in od.iteritems():
				if(ke=='id'):
					break
				print ke,len(v)
	
	

def main():
	while 1:
		a=raw_input("Enter Regular Expression (Aggregate) Statement and -1 for exit \n").strip().split()
		if a[0]=="-1":
			break
		if(a[0]=="groupby"):
			groupby(a[1],a[2])
		
	return 0

if __name__ == '__main__':
	main()

"""
	Example queries:
		- groupby attr filename
"""

