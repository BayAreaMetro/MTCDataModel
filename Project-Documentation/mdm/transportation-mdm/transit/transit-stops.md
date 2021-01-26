# Transit Stops

Map new, planned and existing rail, ferry, and bus stops. Bus stops should contain a field flagging stops that qualify as a 'Major Transit Stop', as well as a fields which provide route-level attributes for routes served. 

### Project Resources

- [Asana Task](https://app.asana.com/0/229355710745434/1199668765765492)
- [Box Directory (MTC Access Only)](https://mtcdrive.box.com/s/q62u4wfayj347b9xhosvsccyfvdo43ey) 

### Table of Contents
- [Data Sources](#data-sources)
- [Analysis Parameters](#analysis-parameters)
	- [Major Transit Stop Defined](#major-transit-stop-definition)
	- [Commute Time Periods](#commute-time-periods)
	- [General Transit Feed Specification (GTFS)](#general-transit-feed-specification)
- [Methodology](#methodology)
	- [Planned and Potential Stops Methodology](#planned-and-potential-transit-stops-methodology)
	- [Existing Transit Stops Methodology](#existing-transit-stops-methodology)
- [Expected Outcomes](#expected-outcomes)
- [Results](#results)
	- [Web Layer](#web-layer)
	- [Data Dictionary](#data-dictionary)
- [Related Work](#related-work)

## Data Sources

- [511 Regional GTFS API January 2020](https://511.org/open-data/transit)
	- [Historic GTFS Data (MTC Access Only)](https://mtcdrive.box.com/s/fv546rcqzt7e05fnyaamvtveh06l5wkg)
- [All Potential PBA 2050 Blueprint Stations (MTC Access Only)](https://mtcdrive.box.com/s/n11exdzc4ee4btfvu2mxa7yv8oq6wguu)


## Analysis Parameters

The transit stop dataset should include all transit stops for the Bay Area, including attributes that indicate routes served, and average route headway for morning and afternoon peak commute periods. These data should also contain a flag for whether or not the stop is a "Major Transit Stop", and the status of the stop. For a full data dictionary, see [Transit Stops Schema](#results).  

### Major Transit Stop Definition

A "Major Transit Stop" is defined in [California Public Resource Code, Section 21064.3](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PRC&sectionNum=21064.3.&highlight=true&keyword=%22major%20transit%20stop%22): 

as a site containing any of the following:

- A. An existing rail or bus rapid transit station.
- B. A ferry terminal served by either a bus or rail transit service.
- C. The intersection of two or more major bus routes with a frequency of service interval of 15 minutes or less during the morning and afternoon peak commute periods.

### Commute Time Periods

|Definition   |Time Period    |
|-------------|---------------|
|Morning Peak | 6:00 - 10:00 |
|Afternoon Peak | 15:00 - 19:00|


### General Transit Feed Specification

General Transit Feed Specification (GTFS) static data was used to create the Existing Transit Stops dataset. The General Transit Feed Specification (GTFS), also known as GTFS static or static transit to differentiate it from the GTFS realtime extension, defines a common format for public transportation schedules and associated geographic information. GTFS "feeds" let public transit agencies publish their transit data and developers write applications that consume that data in an interoperable way.

The specification is made up of a number of text files. The data model below defines the relationships between those files. For more information, please review the [GTFS Static Reference Guide](https://developers.google.com/transit/gtfs)

![gtfs_diagram](files/Relations-among-different-text-files-of-a-GTFS-feed.png)

## Methodology

Planned and Potential Transit stops and Existing Transit Stops developed from [GTFS](#general-transit-feed-specification) data were developed seperately and merged together. In the following two sections, the methodologies used to develop each dataset is outlined. 

### Planned and Potential Transit Stops Methodology

Planned transit stops refer to fully funded projects that have been approved for construction or are currently under construction, while proposed transit stops refer to potential new transit stops that have not yet been fully funded or approved but are currently under study by MTC and ABAG for inclusion in Plan Bay Area 2050. Point features for planned or proposed stops were manually created based on qualitative descriptions of stop locations provided by project sponsors. Note that stop locations are approximate and subject to change as projects progress through environmental review and detailed planning work.

- The ppa_id and ppa_name field values are from the Horizon Project Performance Assessment: List of Transportation Projects (Feb 2020) located at https://mtc.ca.gov/sites/default/files/ProjectPerformance_List.pdf
- The transit type values in route_type were changed from their original values to match the types used by GTFS

### Existing Transit Stops Methodology

Existing transit stops represent all rail, bus, ferry, and light rail stops and were created from static General Transit Feed Specification data downloaded from the [Bay Area 511 GTFS API](https://511.org/open-data/transit). To create the existing transit stops, ESRI Public Transit tools were leveraged as well as open source python libraries such as Pandas. GTFS data was downloaded in early January 2020. Stops and associated headway information for transit routes served by stops are reflect the transit schedule information provided in the feed at the time of download and may not reflect current schedules. 

The process was scripted in a jupyter notebook running in an ArcGIS Pro environment. You can review the processing script [here (MTC Access Only)](https://mtcdrive.box.com/s/k52n8u1v7zuefm5xgd29pqe97hd37hsa). To run the script, you will need to download the ArcGIS Pro project which contains the ESRI toolboxes, jupyter nootebooks as well as the data you would need to repeat the process which can be accessed [here (MTC Access Only)](https://mtcdrive.box.com/s/q62u4wfayj347b9xhosvsccyfvdo43ey).   

**Resource Links**
- [ESRI Public Transit Tools](https://github.com/Esri/public-transit-tools)
- [General Transit Feed Specification (GTFS) Reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)

## Expected Outcomes

- Existing Planned, and Potential Transit Stops with Routes Meeting AM/PM Peak Headways
	- Existing Transit Stops Data Dictionary

## Results

### Web Layer

[Existing Planned, and Potential Transit Stops Web Layer (Internal Portal)](https://arcgis.ad.mtc.ca.gov/portal/home/item.html?id=2c25d8c01ea64a768329673721c42a0b#overview)

### Data Dictionary

[Existing Transit Stops Dictionary](files/transit_stops_existing_planned_schema.csv)

## Related Work

- [Plan Bay Area 2050 Growth Framework](Plan-Bay-Area-2050-Growth-Framework)
- [Legislative Transit Data](https://github.com/BayAreaMetro/Data-Analysis-Projects/blob/master/legislative_transit_data.md)
- [Transportation MDM](https://github.com/BayAreaMetro/DataServices/tree/master/Project-Documentation/mdm/transportation-mdm)
- [511 GTFS Transportation Data](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/511_GTFS.md)
