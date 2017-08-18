--Traffic Sign
--All values for SignType seem to be Undefined

--Attribute Review Qry
SELECT 
SIGNTYP, 
COUNTYFIP,
Count(SIGNTYP) as TotalByClass
FROM     TomTom.MN_TS AS TS
WHERE  
(COUNTYFIP IN (1,13,41,55,75,81,85,95,97))
Group By SIGNTYP, COUNTYFIP
Order By COUNTYFIP


--Traffic Signs
SELECT 
OBJECTID, 
ID, 
SIGNTYP, 
POSITION, 
SIGNCLASS, 
COUNTYFIP, 
Shape
FROM     
TomTom.MN_TS AS TS
WHERE  
(COUNTYFIP IN (1,13,41,55,75,81,85,95,97))