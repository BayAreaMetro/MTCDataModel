-- Draft --

# Transit Priority Areas

This document provides a high-level overview which defines transportation priority areas and the methodology applied to create the resulting dataset. 

## Project Resources

[Asana](https://app.asana.com/0/229355710745434/1195212354291165)

### Table of Contents

- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
	- [Transit Priority Area Definition](#transit-priority-area-definition)
	- [Major Transit Stop Definition](#major-transit-stop-definition)
- [Methodology](#methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)
- [Tags](#tags)

## Data Sources

-[Transit Stops](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/transit/transit-stops.md)

## Analysis Parameters

### Transit Priority Area Definition

A “Transit priority area” is defined in [Californaia Public Resource Code, Section 21099](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PRC&sectionNum=21099.&highlight=true&keyword=transit%20priority%20area+major%20transit):

as an area within one-half mile of a major transit stop that is existing or planned, if the planned stop is scheduled to be completed within the planning horizon included in a Transportation Improvement Program or applicable regional transportation plan.

### Major Transit Stop Definition

A "Major Transit Stop" is defined in [California Public Resource Code, Section 21064.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PRC&sectionNum=21064.3.&highlight=true&keyword=%22major%20transit%20stop%22): 

as a site containing any of the following:

- A. An existing rail or bus rapid transit station.
- B. A ferry terminal served by either a bus or rail transit service.
- C. The intersection of two or more major bus routes with a frequency of service interval of 15 minutes or less during the morning and afternoon peak commute periods. **We specified intersection as 500 feet in distance from one another. This captures stops that serve routes that may not use the same exact stop location or stops located within the intersection of two or more streets. This distance is more conservative than distances used for this anaysis in the past which was 1056 feet or .2 miles. Intersection for the purposes of this analysis was interpreted to mean where two or more major bus routes intersect along two or more intersecting streets. Distances greater than 500 feet would potentially capture stops at street intersections outside or away from the intersection where a given stop is located** 

## Methodology

[Transit Priority Area Notebook](https://github.com/BayAreaMetro/BASIS-Data-Processing/blob/master/policy/regional-policies/transit_priority_area_processing_01_2021.ipynb)

The dataset was developed from the [Transit Stops](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/transit/transit-stops.md) dataset. Stops flagged as 'major stop' were buffered by 1/2 mile.  

The process was scripted in a jupyter notebook running in an ArcGIS Pro environment. You can review the processing script [here (MTC Access Only)](https://github.com/BayAreaMetro/BASIS-Data-Processing/blob/master/policy/regional-policies/transit_priority_area_processing_01_2021.ipynb). To run the script, you will need to download the ArcGIS Pro project which contains the jupyter nootebook as well as the data you would need to repeat the process which can be accessed [here (MTC Access Only)](https://mtcdrive.box.com/s/q62u4wfayj347b9xhosvsccyfvdo43ey).

## Expected Outcomes

- Transportation Priority Area Web Layer

## Results

- [Transportation Priority Area Web Layer](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=d7945556230c43bb95de899e487ff602)

## Tags
