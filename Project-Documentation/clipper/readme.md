<!-- MarkdownTOC bracket="round" autolink="true"  -->

- [Goal](#goal)
- [Background](#background)
- [Tables](#tables)
	- [`ctp` schema:](#ctp-schema)
		- [Key Fields](#key-fields)
			- [Generationtime](#generationtime)
			- [Join Fields](#join-fields)
				- [operator_id to name](#operator_id-to-name)
				- [operators \(transfers\) to name](#operators-transfers-to-name)
				- [route_id to name](#route_id-to-name)
				- [locations \(origins\) id to name](#locations-origins-id-to-name)
			- [locations \(destinations\) id to name](#locations-destinations-id-to-name)

<!-- /MarkdownTOC -->


# Goal

Document anonymized clipper tables on the datalake. 

# Background

The `clipper` schema on the datalake is a large collection of analysis tables from the [usf-practicum](https://github.com/BayAreaMetro/usf-practicum). 

In order to clarify and optimize the table names, usage, and query perfomance for planning department requests, we created a new schema (on the datalake) called `ctp` with:

- the transactions table partitioned by year
- the main tables for common analytical/planning tasks 

These tables now have sortkeys on important join fields, documented below. We've also simplified some column names, with a focus on describing analytical outcomes rather than business transactions. 

# Tables

## `ctp` schema:

|table name|description|
|-----------|--------|
|`y2015`|anonymized transactions for year 2015|
|`y2016`|anonymized transactions for year 2016|
|`y2017`|anonymized transactions for year 2017|
|`locations`|describes the `locationid` columns from transactions|
|`operators`|describes the `operatorid` columns from transactions|
|`routes`|describes the `routeid` column from transactions|

### Key Fields

#### Generationtime

This field is on the transaciton tables (e.g. `y2015`). 

It is the timestamp of the transaction on the transaction tables. 

It is in UTC timezone.

#### Join Fields 

Put human-readable names on transactions or summaries of them. 

What follows are pseudocode joins.

If possible, these joins should happen after a relevant filter on the transactions table, for performance reasons. 

The first example is a pseudocode query in SQL, with the rest leaving the user to determine the full queries. These can be combined as needed, and rewritten for another language as needed. 

These are meant as examples and the user should check them as neede before use. 

##### operator_id to name

```
select operators.operatorname,
y2015.operatorid
from y2015 left join
operators on
y2015.operatorid=operators.operatorid
```  

##### operators (transfers) to name

```
select operators.operatorname as transferoperatorname,
y2015.operatorid
from y2015 left join
operators on
y2015.transferoperator=operators.operatorid
```

##### route_id to name

```
select routes.routename,
y2015.operatorid
from routes left join
y2015.operatorid=routes.operatorid AND 
y2015.routeid=routes.routeid
```

##### locations (origins) id to name

```
select locations.locationname,
y2015.operatorid
from y2015 left join
routes ON
y2015.originlocation=locations.locationcode 
AND y2015.operatorid=locationsoperatorid
```

#### locations (destinations) id to name

```
y2015.destinationlocation=locations.locationcode 
AND y2015.operatorid=locations.participantid
```

