<!-- MarkdownTOC bracket="round" autolink="true"  -->

- [Goal](#goal)
- [Background](#background)
- [Tables](#tables)
	- [`ctp` schema:](#ctp-schema)
		- [Key Fields](#key-fields)
			- [Generationtime](#generationtime)
			- [Human-readable names for transactions](#human-readable-names-for-transactions)
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

This field is on the transaction tables (e.g. `ctp.y2015`). 

It is the timestamp of the transaction on the transaction tables. 

It is in UTC timezone.

#### Human-readable names for transactions

The following is a sketch of how to put human-readable names on transactions or summaries of them. 

What follows are pseudocode joins in SQL. 

If possible, these joins should happen after a relevant filter on the transactions table, for performance reasons. 

The first example is a pseudocode query in SQL, with the rest leaving the user to determine the full queries. These can be combined as needed, and rewritten for another language as needed. 

These are meant as examples and the user should check them as neede before use. 

##### operator_id to name

```
select ctp.operators.operatorname,
ctp.y2015.operatorid
from ctp.y2015 left join
ctp.operators on
ctp.y2015.operatorid=ctp.operators.operatorid
```  

##### operators (transfers) to name

```
select ctp.operators.operatorname as transferoperatorname,
ctp.y2015.operatorid
from ctp.y2015 left join
ctp.operators on
ctp.y2015.transferoperator=ctp.operators.operatorid
```

##### route_id to name

```
select ctp.routes.routename,
ctp.y2015.operatorid
from ctp.routes left join
ctp.y2015.operatorid=ctp.routes.operatorid AND 
ctp.y2015.routeid=ctp.routes.routeid
```

##### locations (origins) id to name

```
select ctp.locations.locationname,
ctp.y2015.operatorid
from ctp.y2015 left join
ctp.routes ON
ctp.y2015.originlocation=ctp.locations.locationcode 
AND ctp.y2015.operatorid=locationsoperatorid
```

#### locations (destinations) id to name

```
ctp.y2015.destinationlocation=ctp.locations.locationcode 
AND ctp.y2015.operatorid=ctp.locations.participantid
```

