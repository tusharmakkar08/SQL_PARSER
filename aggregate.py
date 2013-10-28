#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  aggregate.py
#  
#  Copyright 2013 tusharmakkar08 <tusharmakkar08@gmail.com>
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
import sys

""" Main Code Starts Here """

try:
	open('example1.log', 'w').close()
except IOError:
	pass
	
logging.basicConfig(filename='example1.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

def groupby(att,filen):
	logging.debug("Entered groupby with filename=%s attr=%s"%(filen,attr))
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
	os.system("rm tring.csv")
	
def rename(filen,attr,newfilen,newattr):
	logging.debug("Entered Rename with filename=%s attr=%s newfilename=%s newattr=%s"%(filen,attr,newfilen,newattr))
	if attr=='-1':
		k="mv "+filen+" "+newfilen
		os.system(k)
		print "------Done-----"
	else:
		k="mv "+filen+" "+newfilen
		os.system(k)
		sreader=csv.reader(open(newfilen,"rb"))
		swriter=csv.writer(open("tring1.csv","wb"))
		j=0
		for row in sreader:
			if j==0:
				ti=newattr.split(',')
				print ti
				swriter.writerow(ti)
			else:
				swriter.writerow(row)
			j+=1
		sreader=csv.reader(open("tring1.csv","rb"))
		swriter=csv.writer(open(newfilen,"wb"))
		for row in sreader:
			swriter.writerow(row)
		os.system("rm tring1.csv")

def main():
	while 1:
		a=raw_input("Enter Regular Expression for Groupby or Renaming Statement and -1 for exit \n").strip().split()
		if a[0]=="-1":
			break
		if(a[0]=="groupby"):
			groupby(a[1],a[2])
		if(a[0]=="rename"):
			rename(a[1],a[2],a[3],a[4])
	logging.debug("---------------------------------------------------------------------")
	return 0

if __name__ == '__main__':
	main()

"""
	Format:
		- groupby attr filename
		- rename tablename attrname new_tablename new_attrname
"""

"""
	Example Queries:
		- groupby id sortdata.csv
		- rename sortindex.csv -1 sortindex1.csv -1
		- rename sortindex.csv id,Algorithm_Name,Best_Case_Running_Time,Average_Case_Running_Time,Worst_Case_Running_Time,Worst_Case_Space_Complexity sortindex.csv ID,Algorithm_Name,Best_Case_Running_Time,Average_Case_Running_Time,Worst_Case_Running_Time,Worst_Case_Space_Complexity
"""
