<!-- MarkdownTOC bracket="round" autolink="true"  -->

- [Overview](#overview)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Tables](#tables)
        - [Key Tables](#key-tables)

<!-- /MarkdownTOC -->


# Goal

Document anonymized clipper tables on the datalake. 

One of the key lessons learned from the [usf-practicum](https://github.com/BayAreaMetro/usf-practicum) was that the data lake tables need to be more fully documented in order to ease ad-hoc analytical work on clipper data. 

The primary goal of this directory is to:
* document tables and variable names  
* document relationships between tables  
* note idiosyncrasies of the data (missing values, etc)  

# Overview

## Entity Relationship Diagram

![](clipper-data-store-erd.png)

[Interactive version (PDF)](https://github.com/BayAreaMetro/DataServices/raw/master/Project-Documentation/clipper/clipper-data-store-erd.pdf)

## Tables

- [sfofaretransaction](sfofaretransaction.md) - this is the main table of transactions

#### Key Tables 

- [products](https://mtcdrive.box.com/s/g5a95emac8qpcwaaz4cew5nzjpfto268) - this table provides metadata on products that can be joined to transactions  
    - issuer ID corresponds to participants
- [routes](https://mtcdrive.box.com/s/r95mtasr7f7b4muy4zy1efnvr4sc62y9) - this table provides metadata on routes that can be joined to transactions
- [participants](https://mtcdrive.box.com/s/rfvfg8groylba24s69s13vn7w3rvu0k7) - this table provides metadata on participants that can be joined to transactions
    - participants consist of both transit operators and vendors of Clipper  
- [locations](https://mtcdrive.box.com/s/iyaleoyl4k5ltarce33k6fqb8mgs66hz) - this table provides metadata on locations that can be joined to transactions=======






