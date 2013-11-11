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
import logging
from itertools import groupby

""" Main Code Starts Here """

try:
	open('example.log', 'w').close()
except IOError:
	pass
	
logging.basicConfig(filename='example.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

def Diff(list1,list2):
	"""
		Set Difference function
	"""
	logging.debug("Entering Difference function with list1=%s and list2=%s"%(list1,list2))
	k=[];k2=[]
	for i in list1:
		k.append(i)
	for i in list2:
		if i in k:
			k2.append(i)
	k1=[]
	for i in list1:
		k1.append(i)
	for i in list2:
		if i not in k1:
			k.append(i)
	for i in k:
		if i not in k2:
			print i
	logging.debug("------------Difference function End------------")

def Int(list1,list2):
	"""
		Intersection function
	"""
	logging.debug("Entering Intersection function with list1=%s and list2=%s"%(list1,list2))
	k=[]
	for i in list1:
		k.append(i)
	k1=[]
	for i in list2:
		if i in k:
			k1.append(i)
	for i in k1:
		print i
	logging.debug("------------Intersection function End------------")

def Uni(list1,list2):
	"""
		Union function
	"""
	logging.debug("Entering Union function with list1=%s and list2=%s"%(list1,list2))
	k=[]
	for i in list1:
		k.append(i)
	for i in list2:
		if i not in k:
			k.append(i)
	for i in k:
		print i
	logging.debug("------------Union function End------------")
	
def minag(attr,filename):
	"""
		Minimum aggregate function
	"""
	logging.debug("Entering Min aggregate function with attr=%s and filename=%s"%(attr,filename))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	k=99999999
	for row in sreader:
		try:
			k=min(int(row[attr]),k)
		except:
			k=99999999
	print k

def maxag(attr,filename):
	"""
		Maximum aggregate function
	"""
	logging.debug("Entering Max aggregate function with attr=%s and filename=%s"%(attr,filename))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	k=-99999999
	for row in sreader:
		try:
			k=max(int(row[attr]),k)
		except:
			k=-99999999
	print k

def avgag(attr,filename):
	"""
		Average aggregate function
	"""
	logging.debug("Entering Average aggregate function with attr=%s and filename=%s"%(attr,filename))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	k=0.00;num=-2
	for row in sreader:
		try:
			num+=1
			k+=int(row[attr])
		except :
			pass
	print k/(num*1.00)
	
def countag(attr,filename):
	"""
		Counting aggregate function
	"""
	logging.debug("Entering Count aggregate function with attr=%s and filename=%s"%(attr,filename))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	num=0
	for row in sreader:
		try:
			num+=1
		except:
			num=0
	print num-2
	
def joinwhere(listvar1,conditions,flagi):
	"""
		Code for joining with conditions
	"""
	cond=conditions[1:]
	stringforcolumn=conditions[0][6:len(conditions[0])-1].split(",")
	#print stringforcolumn
	columnids=[]
	for t in stringforcolumn:
		co=0
		flag=0
		sreader=csv.reader(open("mix.csv","rb"))  #reader for the given file
		for i in sreader:
			if co==0:
				co1=0
				for j in i:
					#print j
					if j==t:
						flag=1
						break
					co1+=1
			if flag==1:
				break
			co+=1
		columnids.append(co1)
	logging.debug("Column id's=%s"%(columnids))
	if len(columnids)==1:
		wheref("mix.csv",conditions[1],stringforcolumn[0])
		if flagi==0:
			selectf(listvar1,"mix1","-1")
		else:
			selectfuq(listvar1,"mix1","-1")
	else:
		#print conditions[1],columnids
		wherecomp("mix.csv",conditions[1],columnids)
		if flagi==0:
			selectf(listvar1,"mix2","-1")
		else:
			selectfuq(listvar1,"mix2","-1")
		
def wherecomp(filename,condition,columnid):
	"""
		Code for where in select for joins
	""" 
	logging.debug("Entered where with filename=%s condition=%s and columnid=%s"%(filename,condition,columnid))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	newcond=condition.strip().split("|")
	newstr=""
	for i in newcond:
		newstr+=i+" "
	newlistking=newstr.split()
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	evalt=""
	logging.debug("Newlistking=%s"%(newlistking))
	swriter=csv.writer(open("mix2.csv","wb"))
	co=0
	for i in sreader:
		if co==0:
			swriter.writerow(i)
			break
	co=0
	swriter=csv.writer(open("mix2.csv","a"))
	t=newlistking[0].split(',')
	for i in sreader:
		co1=0
		neweval=""
		for j in i :
			if (co1 in columnid):
				neweval+=j+" "
			co1+=1
		kt=neweval.split(" ")
		str1=kt[0]+t[2]+kt[1]
		if kt[1]!="" and eval(str1):
			swriter.writerow(i)
		
def wheref(filename,condition,column):
	"""
		Code for where in select
	"""
	logging.debug("Entered where with filename=%s condition=%s and column=%s"%(filename,condition,column))
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	newcond=condition.strip().split("|")
	co=0
	flag=0
	for i in sreader:
		if co==0:
			co1=0
			for j in i:
				if j==column:
					flag=1
					break
				co1+=1
		if flag==1:
			break
		co+=1
	columnid=co1
	newstr=""
	for i in newcond:
		newstr+=i+" "
	newlistking=newstr.split()
	sreader=csv.reader(open(filename,"rb"))  #reader for the given file
	evalt=""
	logging.debug("Newcond=%s and Newlistking=%s and columnid=%s"%(newcond,newlistking,co1))
	swriter=csv.writer(open("mix1.csv","wb"))
	co=0
	for i in sreader:
		if co==0:
			swriter.writerow(i)
			break
	co=0
	swriter=csv.writer(open("mix1.csv","a"))
	for i in sreader:
		co1=0
		for j in i:
			evalt=""
			for ting in newlistking:
				if ting!="and" and ting!="or" and columnid==co1 and co!=0:
					evalt+="%r%r"%(j,ting)
				if (ting=="and" or ting=="or") and columnid==co1 and co!=0:
					evalt+=" "+ting+" "
			neweval=""
			#logging.debug("evalt=%s"%(evalt))
			for ink in evalt:
				if ink!="'":
					neweval+=ink
			#if co!=0 and columnid==co1:
			#	print neweval,eval(neweval)
			if columnid==co1 and co!=0 and eval(neweval):
				swriter.writerow(i)
			co1+=1
		co+=1
		
	
def joinf(listvar1,tables,conditions,varwhere,flagi):
	"""
		Code for joining tables
	"""
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
							k.append(tables[1]+"."+t)
						for t in j:
							k1.append(tables[0]+"."+t)
						swriter.writerow(k+k1)
					if co!=0 and co1!=0:
						swriter.writerow(i+j)
					co1+=1
				co+=1
	except IOError:
		print "File Not Found"
	if conditions!="-1":
		logging.debug("Entered joinf with tables=%s and conditions=%s"%(tables,conditions))
		joinwhere(listvar1,conditions,flagi)
	else:
		if flagi==0:
			selectf(listvar1,"mix",varwhere)
		else:
			selectfuq(listvar1,"mix",varwhere)
		
def parsing(listvar1,filename,inp,column,varwhere,flagi):
	"""
		Code for parsing the functions
	"""
	newstr="" 		# newstr made to remove paranthesis
	logging.debug("Entered parsing with filename=%s inp=%s and column=%s"%(filename,inp,column))
	for i in inp:
		if i!='(' and i!=')'and i!='-' and i!="[" and i!="]" and i!="'" and i!="^":
			newstr+=i
		if i=="-" or i=="^":
			newstr+=" "
					
	trialList=newstr.strip().split()
	logging.debug("triallist=%s in parsing"%(trialList))
	tableName=trialList[1].strip().split(",")
	if trialList[0]=="Join"or trialList[0]=="JOIN"or trialList[0]=="join":
		if len(trialList)<=2:
			logging.debug("Entering joinf with tablename=%s and no condition"%(tableName))
			joinf(listvar1,tableName,"-1",varwhere,flagi)
		else:
			logging.debug("Entering joinf with tablename=%s and condition=%s"%(tableName,trialList[2:]))
			joinf(listvar1,tableName,trialList[2:],varwhere,flagi)
	if trialList[0]=='cond'or trialList[0]=="COND" or trialList[0]=="Cond":
		logging.debug("Entering wheref with filename=%s,condition=%s,column=%s"%(filename,trialList[1],column))
		wheref(filename,trialList[1],column)
		

out=[]
def selectf(listvar1,var2,varwhere):
	"""
		Normal select Code for selecting from table
	"""
	global out
	logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(listvar1,var2,varwhere))
	try:
		if var2[0]=="(":
			parsing(listvar1,"-1",var2,"-1",varwhere,0)
		#	os.remove("mix.csv")	# To be added in final code
			return
		else:
			filename=var2+".csv"
		with open(filename):
			if varwhere!="-1":
				parsing(listvar1,filename,str(varwhere[1]),varwhere[0],varwhere,0)
				selectf(listvar1,"mix1","-1")
		#		os.remove("mix1.csv")	# To be added in final code
			else:
				logging.debug("Entered main of scanf")
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
					opli={}
					for j in var1:
						oldlength=len(kinglist)
						co=0;flag=0
						if j[0]=="{":
							flag=1
							k="";flag1=0;op=""
							for jo in j:
								if jo=='[':
									flag1=1
								if (jo!="{" and jo!="}") and flag1==0:
									k+=jo
								if flag1==1 and jo!=']' and jo!='[':
									op+=jo
						if flag==1:
							j=k
						for i in row_name:
							if i==j:
								if flag==1:
									opli[op]=co
								kinglist.append(co)
								break
							co+=1
						if len(kinglist)==oldlength:
							print j,"Column Not Found"
					if len(kinglist)==0:
						print "------NO RESULT----"
					else:
						out=[]
						if flag!=1:
							for row in sreader:
								k=[]
								for j in kinglist:
									k.append(row[j])
									print row[j],
								out.append(k)
								print
						else:
							for op in opli:
								print op,"is ",
								if op=='min':
									minag(opli[op],filename)
								if op=='max':
									maxag(opli[op],filename)
								if op=='count':
									countag(opli[op],filename)
								if op=='avg':
									avgag(opli[op],filename)
	except IOError:	
		print "File Not Found"

def selectfuq(listvar1,var2,varwhere):
	"""
		Select Unique Code for selecting from table
	"""
	global out
	logging.debug("Entering Selectfuq for single query from main with var1=%s var2=%s and var3=%s"%(listvar1,var2,varwhere))
	try:
		if var2[0]=="(":
			parsing(listvar1,"-1",var2,"-1",varwhere,1)
		#	os.remove("mix.csv")	# To be added in final code
			return
		else:
			filename=var2+".csv"
		with open(filename):
			if varwhere!="-1":
				parsing(listvar1,filename,str(varwhere[1]),varwhere[0],varwhere,1)
				selectfuq(listvar1,"mix1","-1")
		#		os.remove("mix1.csv")	# To be added in final code
			else:
				logging.debug("Entered main of scanf")
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
					opli={}
					for j in var1:
						oldlength=len(kinglist)
						co=0;flag=0
						if j[0]=="{":
							flag=1
							k="";flag1=0;op=""
							for jo in j:
								if jo=='[':
									flag1=1
								if (jo!="{" and jo!="}") and flag1==0:
									k+=jo
								if flag1==1 and jo!=']' and jo!='[':
									op+=jo
						if flag==1:
							j=k
						for i in row_name:
							if i==j:
								if flag==1:
									opli[op]=co
								kinglist.append(co)
								break
							co+=1
						if len(kinglist)==oldlength:
							print j,"Column Not Found"
					if len(kinglist)==0:
						print "------NO RESULT----"
					else:
						out=[]
						if flag!=1:
							for row in sreader:
								k=[]
								for j in kinglist:
									k.append(row[j])
								out.append(k)
							print [ key for key,_ in groupby(out)]
						else:
							for op in opli:
								print op,"is ",
								if op=='min':
									minag(opli[op],filename)
								if op=='max':
									maxag(opli[op],filename)
								if op=='count':
									countag(opli[op],filename)
								if op=='avg':
									avgag(opli[op],filename)
	except IOError:	
		print "File Not Found"
		
		
def selectft(listvar1,var2,varwhere):
	"""
		Multiple Select Code for selecting from table
	"""
	global out
	logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(listvar1,var2,varwhere))
	try:
		if var2[0]=="(":
			parsing(listvar1,"-1",var2,"-1",varwhere,0)
		#	os.remove("mix.csv")	# To be added in final code
			return
		else:
			filename=var2+".csv"
		with open(filename):
			if varwhere!="-1":
				parsing(listvar1,filename,str(varwhere[1]),varwhere[0],varwhere,0)
				selectf(listvar1,"mix1","-1")
		#		os.remove("mix1.csv")	# To be added in final code
			else:
				logging.debug("Entered main of scanf")
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
					opli={}
					for j in var1:
						oldlength=len(kinglist)
						co=0;flag=0
						if j[0]=="{":
							flag=1
							k="";flag1=0;op=""
							for jo in j:
								if jo=='[':
									flag1=1
								if (jo!="{" and jo!="}") and flag1==0:
									k+=jo
								if flag1==1 and jo!=']' and jo!='[':
									op+=jo
						if flag==1:
							j=k
						for i in row_name:
							if i==j:
								if flag==1:
									opli[op]=co
								kinglist.append(co)
								break
							co+=1
						if len(kinglist)==oldlength:
							print j,"Column Not Found"
					if len(kinglist)==0:
						print "------NO RESULT----"
					else:
						out=[]
						if flag!=1:
							for row in sreader:
								k=[]
								for j in kinglist:
									k.append(row[j])
			#						print row[j],
								out.append(k)
				#				print
						else:
							for op in opli:
								print op,"is ",
								if op=='min':
									minag(opli[op],filename)
								if op=='max':
									maxag(opli[op],filename)
								if op=='count':
									countag(opli[op],filename)
								if op=='avg':
									avgag(opli[op],filename)
	except IOError:	
		print "File Not Found"

def selectfuqt(listvar1,var2,varwhere):
	"""
		Multiple select unique Code for selecting from table
	"""
	global out
	logging.debug("Entering Selectfuq for nested queries from main with var1=%s var2=%s and var3=%s"%(listvar1,var2,varwhere))
	try:
		if var2[0]=="(":
			parsing(listvar1,"-1",var2,"-1",varwhere,1)
		#	os.remove("mix.csv")	# To be added in final code
			return
		else:
			filename=var2+".csv"
		with open(filename):
			if varwhere!="-1":
				parsing(listvar1,filename,str(varwhere[1]),varwhere[0],varwhere,1)
				selectfuq(listvar1,"mix1","-1")
		#		os.remove("mix1.csv")	# To be added in final code
			else:
				logging.debug("Entered main of scanf")
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
					opli={}
					for j in var1:
						oldlength=len(kinglist)
						co=0;flag=0
						if j[0]=="{":
							flag=1
							k="";flag1=0;op=""
							for jo in j:
								if jo=='[':
									flag1=1
								if (jo!="{" and jo!="}") and flag1==0:
									k+=jo
								if flag1==1 and jo!=']' and jo!='[':
									op+=jo
						if flag==1:
							j=k
						for i in row_name:
							if i==j:
								if flag==1:
									opli[op]=co
								kinglist.append(co)
								break
							co+=1
						if len(kinglist)==oldlength:
							print j,"Column Not Found"
					if len(kinglist)==0:
						print "------NO RESULT----"
					else:
						out=[]
						if flag!=1:
							for row in sreader:
								k=[]
								for j in kinglist:
									k.append(row[j])
								out.append(set(k))
							print set(k)
						else:
							for op in opli:
								print op,"is ",
								if op=='min':
									minag(opli[op],filename)
								if op=='max':
									maxag(opli[op],filename)
								if op=='count':
									countag(opli[op],filename)
								if op=='avg':
									avgag(opli[op],filename)
	except IOError:	
		print "File Not Found"


def main():
	global out
	while 1:
		a=raw_input("Enter Regular Expression Statement and -1 for exit \n").strip().split()
		if a[0]=="-1":
			break
		if a[0]=="mqselect":
			a1=raw_input("Enter Regular Expression Statement  \n").strip().split()
			L=len(a1);i=0
			print "answer for given nested query is"
			while i+2<L: 	# i+2 because in other cases it gives error
				if a1[i]=="SELECT"or a1[i]=="select"or a1[i]=="Select" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectft(var1,var2,var3)
					i+=3
				if a1[i]=="UQSELECT"or a1[i]=="uqselect"or a1[i]=="Uqselect" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuqt(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			var3=raw_input("Enter conditions  in id's \n").split(" ")
			if var3[1]==">=":
				for t in out:
					if t[0]>=var3[2]:
						print t[0]
			if var3[1]==">":
				for t in out:
					if t[0]>var3[2]:
						print t[0]
			if var3[1]=="<=":
				for t in out:
					if t[0]<=var3[2]:
						print t[0]
			if var3[1]=="==":
				for t in out:
					if t[0]==var3[2]:
						print t[0]
			if var3[1]=="<":
				for t in out:
					if t[0]<var3[2]:
						print t[0]
		if(a[0]=="UNI"):
			a1=raw_input("Enter Regular Expression Statement  \n").strip().split()
			a2=raw_input("Enter Regular Expression Statement  \n").strip().split()
			L=len(a1);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a1[i]=="SELECT"or a1[i]=="select"or a1[i]=="Select" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a1[i]=="UQSELECT"or a1[i]=="uqselect"or a1[i]=="Uqselect" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			print 
			print
			t1=out
			L=len(a2);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a2[i]=="SELECT"or a2[i]=="select"or a2[i]=="Select" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a2[i]=="UQSELECT"or a2[i]=="uqselect"or a2[i]=="Uqselect" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			t2=out
			logging.debug("Lists are list1=%s and list2=%s"%(t1,t2))
			Uni(t1,t2)
		if(a[0]=="INT"):
			a1=raw_input("Enter Regular Expression Statement  \n").strip().split()
			a2=raw_input("Enter Regular Expression Statement  \n").strip().split()
			L=len(a1);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a1[i]=="SELECT"or a1[i]=="select"or a1[i]=="Select" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a1[i]=="UQSELECT"or a1[i]=="uqselect"or a1[i]=="Uqselect" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			print 
			print
			t1=out
			L=len(a2);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a2[i]=="SELECT"or a2[i]=="select"or a2[i]=="Select" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a2[i]=="UQSELECT"or a2[i]=="uqselect"or a2[i]=="Uqselect" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			t2=out
			logging.debug("Lists are list1=%s and list2=%s"%(t1,t2))
			Int(t1,t2)
		if(a[0]=="DIFF"):
			a1=raw_input("Enter Regular Expression Statement \n").strip().split()
			a2=raw_input("Enter Regular Expression Statement  \n").strip().split()
			L=len(a1);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a1[i]=="SELECT"or a1[i]=="select"or a1[i]=="Select" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a1[i]=="UQSELECT"or a1[i]=="uqselect"or a1[i]=="Uqselect" and a1[i+2]=="FROM"or a1[i+2]=="from"or a1[i+2]=="From" :
					var1=a1[i+1]
					var2=a1[i+3]
					try:
						if a1[i+4]=="where"or a1[i+4]=="WHERE"or a1[i+4]=="Where":
							var3=a1[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			print 
			print
			t1=out
			L=len(a2);i=0
			while i+2<L: 	# i+2 because in other cases it gives error
				if a2[i]=="SELECT"or a2[i]=="select"or a2[i]=="Select" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectf(var1,var2,var3)
					i+=3
				if a2[i]=="UQSELECT"or a2[i]=="uqselect"or a2[i]=="Uqselect" and a2[i+2]=="FROM"or a2[i+2]=="from"or a2[i+2]=="From" :
					var1=a2[i+1]
					var2=a2[i+3]
					try:
						if a2[i+4]=="where"or a2[i+4]=="WHERE"or a2[i+4]=="Where":
							var3=a2[i+5:]
					except:
						var3="-1"
					logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
					selectfuq(var1,var2,var3)
					i+=3
				i+=1
				logging.debug("---------------------------------------------------------------------")
			t2=out
			logging.debug("Lists are list1=%s and list2=%s"%(t1,t2))
			Diff(t1,t2)
		L=len(a);i=0
		while i+2<L: 	# i+2 because in other cases it gives error
			if (a[i]=="SELECT"or a[i]=="select"or a[i]=="Select") and (a[i+2]=="FROM"or a[i+2]=="from"or a[i+2]=="From") :
				var1=a[i+1]
				var2=a[i+3]
				try:
					if a[i+4]=="where"or a[i+4]=="WHERE"or a[i+4]=="Where":
						var3=a[i+5:]
				except:
					var3="-1"
				logging.debug("Entering Selectf from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
				selectf(var1,var2,var3)
				i+=3
			if(a[i]=="UQSELECT"or a[i]=="uqselect"or a[i]=="Uqselect") and (a[i+2]=="FROM"or a[i+2]=="from"or a[i+2]=="From") :
				var1=a[i+1]
				var2=a[i+3]
				try:
					if a[i+4]=="where"or a[i+4]=="WHERE"or a[i+4]=="Where":
						var3=a[i+5:]
				except:
					var3="-1"
				logging.debug("Entering SelectfUQ from main with var1=%s var2=%s and var3=%s"%(var1,var2,var3))
				selectfuq(var1,var2,var3)
				i+=3
			i+=1
			logging.debug("---------------------------------------------------------------------")
	return 0

if __name__ == '__main__':
	main()

"""
	Format till now : 
	Select "any_no_of_arguments" from 
	"either_single_filename_or_
	(Join-filenames_with_comma_seperated^where^conditions)" where name_of_column
	(cond-any|no|of|conditions|using|"|")
"""

"""
	Example queries:
		- select * from sortindex where id (cond->=5|and|<=7)
		- select id,Algorithm_Name from sortindex
		- select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex)
		- select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex) where sortindex.id (cond-==4)
		- select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex^where{sortindex.id}^==5) 
		- select sortindex.id from (Join-sortdata,sortindex^where{sortindex.id,sortdata.id}^sortindex.id,sortdata.id[,==,])
		- select {id}[min],{id}[max],{id}[avg],{id}[count] from sortindex
		- UNI
			select id from sortindex 
			select id from sortindex where id (cond->=5|and|<=7)
		-INT
			select id from sortindex 
			select id from sortindex where id (cond->=5|and|<=7)
		-DIFF
			select id from sortindex 
			select id from sortindex where id (cond->=5|and|<=7)
		- uqselect * from sortindex where id (cond->=5|and|<=7)
		- uqselect sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex) where sortindex.id (cond-==4)
		- mqselect
		  select id from sortindex where id (cond->=5|and|<=7) 
		  0 >= 6
"""
