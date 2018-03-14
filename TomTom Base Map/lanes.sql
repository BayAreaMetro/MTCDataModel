CREATE VIEW tomtom_2016.nw_lanes AS
SELECT 
n.id,
n.frc,
n.name,
n.shieldnum,
n.freeway,
n.tollrd,
n.oneway,
n.lanes,
n.ramp,
n.partstruc,
FROM tomtom_2016.tt_nw as n LEFT OUTER JOIN
tomtom_2016.tt_ll as ll ON n.id = ll.id
Where n.frc = 0
