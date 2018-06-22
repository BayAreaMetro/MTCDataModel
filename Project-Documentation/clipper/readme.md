<!-- MarkdownTOC bracket="round" autolink="true"  -->

- [Goal](#goal)
- [Method](#method)
- [Outcome](#outcome)
	- [Tables on the `ctp` schema:](#tables-on-the-ctp-schema)
	- [Key Fields](#key-fields)
		- [Generationtime](#generationtime)
		- [operator_id to name](#operator_id-to-name)
		- [operators \(transfers\) to name](#operators-transfers-to-name)
		- [route_id to name](#route_id-to-name)
		- [locations \(origins\) id to name](#locations-origins-id-to-name)
		- [locations \(destinations\) id to name](#locations-destinations-id-to-name)

<!-- /MarkdownTOC -->


# Goal

Document anonymized clipper tables on the datalake. 

# Method

The `clipper` schema on the datalake is a large collection of analysis tables from the [usf-practicum](https://github.com/BayAreaMetro/usf-practicum). 

In order to clarify and optimize the table names, usage, and query perfomance for planning department requests, we created a new schema (on the datalake) called `ctp` with:

- the transactions table partitioned by year
- the main tables for common analytical/planning tasks 

These tables now have sortkeys on important join fields, documented below. We've also simplified some column names, with a focus on describing analytical outcomes rather than business transactions. 

# Outcome

## Tables on the `ctp` schema:

|table name|description|
|-----------|--------|
|`y2015`|anonymized transactions for year 2015|
|`y2016`|anonymized transactions for year 2016|
|`y2017`|anonymized transactions for year 2017|
|`locations`|describes the `locationid` columns from transactions|
|`operators`|describes the `operatorid` columns from transactions|
|`routes`|describes the `routeid` column from transactions|

## Key Fields

### Generationtime

This is the timestamp of the transaction on the transaction tables. It is in UTC timezone.

Key join fields for the transactions table. Basically, the relationships that give the id's on the anonymized transactions table human-readable names. 

### operator_id to name
operators, operatorid=operatorid
    
### operators (transfers) to name
transferoperator=operatorid

### route_id to name
operatorid=operatorid,
routeid=routeid
  
### locations (origins) id to name
originlocation=locationcode,
operatorid=operatorid
  
### locations (destinations) id to name
destinationlocation=locationcode
operatorid=participantid



