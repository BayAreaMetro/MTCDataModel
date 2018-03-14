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
ll.dividertyp,
ll.seqnr,
ll.id,
pm.id,
li.id,
ln.id,
le.id
FROM tomtom_2016.tt_nw as n LEFT OUTER JOIN
tomtom_2016.tt_ll as ll ON n.id = ll.id LEFT OUTER JOIN
tomtom_2016.tt_ld as ld ON ll.id = ld.id LEFT OUTER JOIN
tomtom_2016.tt_ln as ln ON ld.id = ln.id LEFT OUTER JOIN
tomtom_2016.tt_li as li ON ln.id = li.id LEFT OUTER JOIN
tomtom_2016.tt_pm as pm ON li.id = pm.id LEFT OUTER JOIN
tomtom_2016.tt_le as le ON pm.id = le.id LEFT OUTER JOIN
Where n.frc = 0
