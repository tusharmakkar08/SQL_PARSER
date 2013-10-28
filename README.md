SQL_PARSER
==========

Parsing SQL commands and implementing it through files

Functions Implemented
-----------------------

* Select : with multiple and single parameter
* Where : working for multiple conditions
* Join : Able to join 2 files at a time
* Conditional Join 
* Aggregate functions like min,max,sum,average,count


Functions to be Implemented
---------------------------

* rename

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

* In aggregate.py 

	* groupby id sortdata.csv
