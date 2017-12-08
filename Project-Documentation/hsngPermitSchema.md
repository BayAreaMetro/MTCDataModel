# Housing Schema - Residential Permit Attribute Table

## Problem Statement
Develop structure for residential permit attribute table in housing schema of enterprise database. Purpose is to set rules and restrictions on permit attribute values to make it easier to write queries against the table.

## Outcome
The Housing Schema is in a PostgreSQL database. The attribute table structure, rules, and restrictions is found below. Full definitions for field name and domain values are found in the metadata associated with the data and services available on the internal data portal.

<html>
<table style="width:100%>
 <tr>
  <th>Field</th>
  <th>Simple Definition</th>
  <th>Note, Rule, Restrictions</th>
  <th>Field <br/> Type</th>
  <th>Field <br/> Length</th>
  <th>Field <br/> Configuration</th>
  <th>Default <br/> Value</th>
 </tr>
 <tr>
  <td>joinid</td>
  <td>Connects feature to attributes</td>
  <td>Organized by county. Each year, first new value needs to be incremented by 10 over previous year's final value.</td>
  <td>Text</td>
  <td>11</td>
  <td>char(11) NOT NULL</td>
  <td> </td>
 </tr>
</table>
</html>

## Results
