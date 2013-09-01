#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

""" Main Code Starts Here """

def wheref(filename,condition):
	"""
		Code for where in select
	"""
	print filename,condition
	
def joinf(tables,conditions):
	"""
		Code for joining tables
	"""
	if conditions!="-1":
		pass
	else:
		try:
			filename1=tables[0]+".csv"
			filename2=tables[1]+".csv"
			with open(filename1) and open(filename2):
				sreader1=csv.reader(open(filename1,"rb"))  #reader for the given file
				sreader2=csv.reader(open(filename2,"rb"))  #reader for the given file
				swriter=csv.writer(open("mix.csv","wb"))
				co=0
				for i in sreader2 :
					sreader1=csv.reader(open(filename1,"rb"))  #reader for the given file
					co1=0
					for j in sreader1:
						if co==0 and co1==0:	# For adding details
							k=[];k1=[]
							for t in i:
								k.append(tables[0]+"."+t)
							for t in j:
								k1.append(tables[1]+"."+t)
							swriter.writerow(k+k1)
						if co!=0 and co1!=0:
							swriter.writerow(i+j)
						co1+=1
					co+=1
				
		except IOError:
			print "File Not Found"
		
def parsing(filename,inp):
	"""
		Code for parsing the functions
	"""
	newstr="" 		# newstr made to remove paranthesis
	
	for i in inp:
		if i!='(' and i!=')'and i!='-' and i!="[" and i!="]" and i!="'":
			newstr+=i
		if i=="-":
			newstr+=" "
					
	trialList=newstr.strip().split()
	tableName=trialList[1].strip().split(",")
	if trialList[0]=="Join"or trialList[0]=="JOIN"or trialList[0]=="join":
		if len(trialList)<=2:
			joinf(tableName,"-1")
		else:
			joinf(tablename,trialList[3:])
	if trialList[0]=='cond'or trialList[0]=="COND" or trialList[0]=="Cond":
		wheref(filename,trialList[1])
		
			
def selectf(listvar1,var2,varwhere):
	"""
		Code for selecting from table
	"""
	try:
		if var2[0]=="(":
			parsing("-1",var2)
			selectf(listvar1,"mix",varwhere)
			#os.remove("mix.csv")	# To be added in final code
			return
		else:
			filename=var2+".csv"
		with open(filename):
			if varwhere!="-1":
				parsing(filename,str(varwhere))
			else:
				sreader=csv.reader(open(filename,"rb"))  #reader for the given file
				var1=listvar1.strip().split(',') #Splitting the columns in var1
				if var1[0]=="*": # For All columns
					co=0 		# Temporary Variable
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
					kinglist=[]  # List containing the index of columns in the table
					for j in var1:
						oldlength=len(kinglist)
						co=0
						for i in row_name:
							if i==j:
								kinglist.append(co)
								break
							co+=1
						if len(kinglist)==oldlength:
							print j,"Column Not Found"
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
		while i+2<L: 	# i+2 because in other cases it gives error
			if a[i]=="SELECT"or a[i]=="select"or a[i]=="Select" and a[i+2]=="FROM"or a[i+2]=="from"or a[i+2]=="From" :
				var1=a[i+1]
				var2=a[i+3]
				try:
					if a[i+5]=="where"or"WHERE"or"Where":
						var3=a[i+6:]
				except:
					var3="-1"
					pass
				selectf(var1,var2,var3)
				i+=3
			i+=1
	return 0

if __name__ == '__main__':
	main()

"""
	Format till now : 
	Select "any_no_of_arguments" from 
	"either_single_filename_or_
	(Join-filenames_with_comma_seperated where conditions)" where 
	(cond-any|no|of|conditions|using|"|")
"""
