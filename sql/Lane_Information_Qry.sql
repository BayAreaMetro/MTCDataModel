--Sql Guidance: https://www.w3schools.com/SQL/


-- See the following url(s) for more details:
-- http://gis.mtc.ca.gov/home/tomtom/multinet_shp_4-8_fs_v1-1-7.pdf
-- https://mtcdrive.box.com/s/pzbp3xkjli8d2km30jhy51v9xarq6ta4

-- Lane Type Information
SELECT 
NW.ID, 
NW.FRC, 
NW.NAME, 
NW.SHIELDNUM, 
NW.RTEDIR, 
NW.TOLLRD, 
NW.SLIPRD, 
NW.LANES, 
NW.RAMP, 
NW.PARTSTRUC, 
CASE 
When LI.LANETYP is NULL THEN 'Not Specified'
When LI.LANETYP = 2 THEN 'Exit/Entrance Lane' 
When LI.LANETYP = 3 THEN 'Shoulder Lane/Emergency Lane'
When LI.LANETYP = 4 THEN 'Parking Lane'
When LI.LANETYP = 6 THEN 'HOV Lane'
END as Lane_Type, 
LI.MINVEHOC as MIN_Vehicle_Occupancy, 
LI.SINGOC as Single_Occupancy, 
NW.COUNTYFIP,
NW.Shape
FROM     
TomTom.MN_NW AS NW LEFT OUTER JOIN
TomTom.MN_LI AS LI ON NW.ID = LI.ID
WHERE  
(NW.COUNTYFIP IN (1,13,41,55,75,81,85,95,97)) and  LANETYP is not null --NW.FRC IN (1,2,3)
Order By LI.LANETYP ASC