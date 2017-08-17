--Sql Guidance: https://www.w3schools.com/SQL/


-- See the following url(s) for more details:
-- http://gis.mtc.ca.gov/home/tomtom/multinet_shp_4-8_fs_v1-1-7.pdf
-- https://mtcdrive.box.com/s/pzbp3xkjli8d2km30jhy51v9xarq6ta4

-- Lane Information
SELECT
NW.ID, 
NW.FRC, 
NW.NAME, 
NW.SHIELDNUM, 
NW.RTEDIR,
NW.FREEWAY, 
NW.TOLLRD, 
NW.SLIPRD,
NW.LANES, 
NW.RAMP, 
NW.PARTSTRUC,
NW.FOW,
NW.SOL,
CASE
WHEN NW.CARRIAGE = '' THEN 'N/A'
WHEN NW.CARRIAGE = 1 THEN 'Car Pool'
WHEN NW.CARRIAGE = 2 THEN 'Express'
WHEN NW.CARRIAGE = 3 THEN 'Local'
END as VehicleMobilityType, 
NW.CHARGE, 
CASE 
When LI.LANETYP is NULL THEN 'Not Specified'
When LI.LANETYP = 2 THEN 'Exit/Entrance Lane' 
When LI.LANETYP = 3 THEN 'Shoulder Lane/Emergency Lane'
When LI.LANETYP = 4 THEN 'Parking Lane'
When LI.LANETYP = 6 THEN 'HOV Lane'
END as Lane_Type, 
CASE
WHEN LI.MINVEHOC = -1 THEN 'N/A' 
WHEN LI.MINVEHOC = 2 THEN 'Driver +1' 
WHEN LI.MINVEHOC = 3 THEN 'Driver +2' 
WHEN LI.MINVEHOC = 4 THEN 'Driver +3' 
WHEN LI.MINVEHOC = 5 THEN 'Driver +4' 
WHEN LI.MINVEHOC = 6 THEN 'Other' 
END as MIN_Vehicle_Occupancy, 
CASE
WHEN LI.SINGOC= -1 THEN 'N/A'
WHEN LI.SINGOC= 1 THEN 'Clean Fuel Type'
WHEN LI.SINGOC= 2 THEN 'Toll Payment'
END as Single_Occupancy,
CASE
WHEN LD.DIRECTION = 0 THEN 'No Direction Indicated' 
WHEN LD.DIRECTION = 1 THEN 'Straight' 
WHEN LD.DIRECTION = 2 THEN 'Slight Right' 
WHEN LD.DIRECTION = 4 THEN 'Right' 
WHEN LD.DIRECTION = 8 THEN 'Sharp Right' 
WHEN LD.DIRECTION = 16 THEN 'U-turn Left' 
WHEN LD.DIRECTION = 32 THEN 'Sharp Left' 
WHEN LD.DIRECTION = 64 THEN 'Left' 
WHEN LD.DIRECTION = 128 THEN 'Slight Left' 
WHEN LD.DIRECTION = 256 THEN 'U-Turn Right' 
END as Lane_Direction,
LE.LANEEND as Lane_End,
LF.DFLANE,
Case
When LF.VT = 0 THEN 'All Vehicle Types'
When LF.VT = 11 THEN 'Passenger Cars'
When LF.VT = 12 THEN 'Residential Vehicles'
When LF.VT = 16 THEN 'Taxi'
When LF.VT = 17 THEN 'Public Bus'
END as Vehicle_Type,
LT.TIMEDOM,
CASE 
When LL.DIVIDERTYP = 0 THEN 'No Divider'
When LL.DIVIDERTYP = 1 THEN 'Interrupted Line with Long Lines'
When LL.DIVIDERTYP = 2 THEN 'Double Solid Line'
When LL.DIVIDERTYP = 3 THEN 'Single Solid Line'
When LL.DIVIDERTYP = 4 THEN 'Combination of Single Solid & Interrupted Line'
When LL.DIVIDERTYP = 5 THEN 'Combination of an Interrupted and a Solid Line'
When LL.DIVIDERTYP = 6 THEN 'Interrupted Line with Short Lines'
When LL.DIVIDERTYP = 15 THEN 'Toll Booth'
When LL.DIVIDERTYP = 99 THEN 'Unknown'
END as Lane_Divider_Type, 
CASE
When PM.PAYMENT = 1 THEN 'Cash'
When PM.PAYMENT = 2 THEN 'Credit Card'
When PM.PAYMENT = 4 THEN 'Bank Card'
When PM.PAYMENT = 8 THEN 'Electronic Purse'
When PM.PAYMENT = 16 THEN 'Electronic Toll Collection'
When PM.PAYMENT = 32 THEN 'Coins Only (exact change)'
When PM.PAYMENT = 64 THEN 'Variable'
END as Toll_Payment,
NW.COUNTYFIP,
NW.Shape
FROM     
TomTom.MN_LE AS LE RIGHT OUTER JOIN
TomTom.MN_NW AS NW LEFT OUTER JOIN
TomTom.MN_PM AS PM ON NW.ID = PM.ID LEFT OUTER JOIN
TomTom.MN_LN ON NW.ID = TomTom.MN_LN.ID ON LE.ID = NW.ID LEFT OUTER JOIN
TomTom.MN_LT AS LT RIGHT OUTER JOIN
TomTom.MN_LF AS LF ON LT.ID = LF.ID ON NW.ID = LF.ID LEFT OUTER JOIN
TomTom.MN_LL AS LL ON NW.ID = LL.ID LEFT OUTER JOIN
TomTom.MN_LD AS LD ON NW.ID = LD.ID LEFT OUTER JOIN
TomTom.MN_LI AS LI ON NW.ID = LI.ID
WHERE  
--1,13,41,55,75,81,85,95,97
(NW.COUNTYFIP IN (1)) --and  LANETYP is not null --NW.FRC IN (1,2,3)
Order By LI.LANETYP ASC

--SELECT NW.ID, NW.FRC, NW.NAME, NW.SHIELDNUM, NW.RTEDIR, NW.FREEWAY, NW.TOLLRD, NW.LANES, LD.DIRECTION, NW.PARTSTRUC, NW.COUNTYFIP, NW.Shape
--FROM     TomTom.MN_LE AS LE RIGHT OUTER JOIN
--                  TomTom.MN_NW AS NW LEFT OUTER JOIN
--                  TomTom.MN_PM AS PM ON NW.ID = PM.ID LEFT OUTER JOIN
--                  TomTom.MN_LN ON NW.ID = TomTom.MN_LN.ID ON LE.ID = NW.ID LEFT OUTER JOIN
--                  TomTom.MN_LT AS LT RIGHT OUTER JOIN
--                  TomTom.MN_LF AS LF ON LT.ID = LF.ID ON NW.ID = LF.ID LEFT OUTER JOIN
--                  TomTom.MN_LL AS LL ON NW.ID = LL.ID LEFT OUTER JOIN
--                  TomTom.MN_LD AS LD ON NW.ID = LD.ID LEFT OUTER JOIN
--                  TomTom.MN_LI AS LI ON NW.ID = LI.ID
--WHERE  (NW.COUNTYFIP IN (1, 13, 41, 55, 75, 81, 85, 95, 97))
