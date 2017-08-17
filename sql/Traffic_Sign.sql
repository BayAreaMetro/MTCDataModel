--Traffic Sign
--All values for SignType seem to be Undefined

--Attribute Review Qry
SELECT 
SIGNTYP, 
COUNTYFIP,
Count(SIGNTYP) as TotalByClass
FROM     TomTom.MN_TS AS TS
Group By SIGNTYP, COUNTYFIP
Order By COUNTYFIP

SELECT 
OBJECTID, 
ID, 
SIGNTYP, 
POSITION, 
SIGNCLASS, 
COUNTYFIP, 
Shape
FROM     TomTom.MN_TS AS TS