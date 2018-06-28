create schema ctp;
create table ctp.y2015
SORTKEY(operatorid,
        routeid,
        originlocation, 
        destinationlocation, 
        transferoperator,
        generationtime)
AS SELECT *
FROM clipper.sfofaretransaction 
    WHERE generationtime > '2015-01-01 00:00:00'
    AND generationtime < '2016-01-01 00:00:00';

create table ctp.y2016
SORTKEY(operatorid,
        routeid,
        originlocation, 
        destinationlocation, 
        transferoperator,
        generationtime)
AS SELECT *
FROM clipper.sfofaretransaction 
    WHERE generationtime > '2016-01-01 00:00:00'
    AND generationtime < '2017-01-01 00:00:00';

create table ctp.y2017
SORTKEY(operatorid,
        routeid,
        originlocation, 
        destinationlocation, 
        transferoperator,
        generationtime)
AS SELECT *
FROM clipper.sfofaretransaction 
    WHERE generationtime > '2017-01-01 00:00:00'
    AND generationtime < '2018-01-01 00:00:00';


create table ctp.operators
SORTKEY(operatorid)
AS SELECT participantname as operatorname,
participantid as operatorid
FROM clipper.participants;

create table ctp.routes
SORTKEY(operatorid,
        routeid)
AS SELECT routename,
routeid as routeid,
participantid as operatorid
FROM clipper.routes;

create table ctp.locations
SORTKEY(operatorid,
        locationcode)
AS SELECT participantlocationcode as operatoridlocationcode,
participantid as operatorid,
locationcode,
locationname,
locationtype
FROM clipper.locations;