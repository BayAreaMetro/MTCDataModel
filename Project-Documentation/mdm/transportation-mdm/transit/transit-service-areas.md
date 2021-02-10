-- Draft --

# Transit Service Areas

Generate Transit Service Areas which area areas 1/2 mile from Transit Stops.

## Project Resources

- [Asana Task (MTC Access Only)](https://app.asana.com/0/229355710745434/1199878663450901)
- [Box Directory (MTC Access Only)](https://mtcdrive.box.com/s/nt7o21j7m4rbdhyk8n1lymepxvtzf2kv)


### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
- [Methodology](#methodology)
- [Results](#results)
- [Tags](#tags)

## Data Sources

Existing Transit Stops Using GTFS Data Downloaded January 2020
[Transit Stops - Existing and Planned (2021) (MTC Access Only)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=2c25d8c01ea64a768329673721c42a0b#overview)

## Analysis Parameters

- Transit Service Areas should include the following attributes:
	- Agency ID
	- Agency Name
	- Route Type

- Transit Service Areas should be based on existing transit stops. 

## Methodology

[Transit Service Areas Processing Notebook](https://mtcdrive.box.com/s/mhk0ntgh6q85hjpqrtiglgian47d5832)

Transit Service Areas were created by adding a 1/2 mile buffer around existing transit stops, then dissolving buffer polygon boundaries by agency_id, agency_nm, and route_type columns. 


## Results

- [Transit Service Areas GeoJSON (MTC Access Only)](https://mtcdrive.box.com/s/7jhv3g004q1pzf6pvdztpu249142vr0s)
- [Transit Service Areas Feature Layer (MTC Access Only)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=5dc9826630c64288aedba80cad24c77d#overview)

## Tags
