SQL_PARSER
==========

Parsing SQL commands and implementing it through files


Language Used :
--------------

* Python
* Shell Scripting

Database Used :
---------------

* Flat File System

Libraries Used :
----------------
	
* logging
* csv
* sys
* os
* collections

How to Run :
-----------
<pre>
				python main.py
				# Run Script for Main querie
				python aggregate.py		
				# Running python code for aggregate functions
</pre>


Functions Implemented
-----------------------

* Select : with multiple and single parameter
* Where : working for multiple conditions
* Join : Able to join 2 files at a time
* Conditional Join 
* Aggregate functions like min,max,average,count
* rename
* Union , Intersection and Set difference
* Unique Operation added 

Functions to be Implemented
---------------------------



Example queries:
----------------

* In main.py

	* select * from sortindex where id (cond->=5|and|<=7)
	* select id,Algorithm_Name from sortindex
	* select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex)
	* select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex) where sortindex.id (cond-==4)
	* select sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex^where{sortindex.id}^==5) 
	* select sortindex.id from (Join-sortdata,sortindex^where{sortindex.id,sortdata.id}^sortindex.id,sortdata.id[,==,])
	* select {id}[min],{id}[max],{id}[avg],{id}[count] from sortindex
	* UNI
		*select id from sortindex 
		*select id from sortindex where id (cond->=5|and|<=7)
	*INT
		*select id from sortindex 
		*select id from sortindex where id (cond->=5|and|<=7)
	*DIFF
		*select id from sortindex 
		*select id from sortindex where id (cond->=5|and|<=7)
	* uqselect * from sortindex where id (cond->=5|and|<=7)
	* uqselect sortindex.id,sortindex.Algorithm_Name from (Join-sortdata,sortindex) where sortindex.id (cond-==4)

* In aggregate.py 

	* groupby id sortdata.csv
	* rename sortindex.csv -1 sortindex1.csv -1
	* rename sortindex.csv id,Algorithm_Name,Best_Case_Running_Time,Average_Case_Running_Time,Worst_Case_Running_Time,Worst_Case_Space_Complexity sortindex.csv ID,Algorithm_Name,Best_Case_Running_Time,Average_Case_Running_Time,Worst_Case_Running_Time,Worst_Case_Space_Complexity
