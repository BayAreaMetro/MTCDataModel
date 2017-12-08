# Housing Schema - Residential Permit Attribute Table

## Problem Statement
Develop structure for residential permit attribute table in housing schema of enterprise database. Purpose is to set rules and restrictions on permit attribute values to make it easier to write queries against the table.

## Outcome
The attribute table structure, rules, and restrictions is found below. Full definitions for field name and domain values are found in the metadata associated with the data and services available on the internal data portal.

| Field Name |   Basic description   |       Note/Rule/Restrictions       |  Field  | Field  | Postgres | Default |
|            |                       |                                    |  Type   | Length |  Column  |  Value  |
| ---------- | --------------------- | ---------------------------------- | ------- | ------ | -------- | ------- |
| joinid     | Connects feature to   | IDs formated by county. First new  |  Text   |   11   | char(11) |         |
|            | attribute             | value for each year should be      |         |        | NOT NULL |         |
|            |                       | incremented by 10 over previous    |         |        |          |         |
|            |                       | year's end value.                  |         |        |          |         |
| ---------- | --------------------- | ---------------------------------- | ------- | ------ | -------- | ------- |
| permyear   | Permit year           | YYYY format                        |  Text   |   4    | char(4)  |         |
|            |                       |                                    |         |        | NOT NULL |         |
| ---------- | --------------------- | ---------------------------------- | ------- | ------ | -------- | ------- |

## Results
