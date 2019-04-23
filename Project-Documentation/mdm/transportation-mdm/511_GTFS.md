-- Draft --

# 511 GTFS API Data

## Overview

The [511 API](https://511.org/developers/list/apis/) provides access to transit and traffic data, including static GTFS feeds and real-time GTFS vehicle locations and trip updates. A more detailed description of the available data (and how to access it) is in the [Detailed Data Documentation](#detailed-data-documentation) at the end of this document.

There are three components to the 511 GTFS Project:

1. Static GTFS data
2. Real-time GTFS data
3. Headway Explorer tool (interactive tool for visualizing and exploring headway data)

**Data Set Name:** Regional Transit Database

**Data Set Description:**

1. Static GTFS data: updated monthly
2. Real-time: ?[every minute]
3. Headway Explorer: based on Static GTFS data

**Data Steward:** 

**Sharing Permissions**

**Category:** Transportation

**Subcategory:** Transit

**Format**

**Primary Use**

**Source:** Transit operators (via MTC 511)

**Unit of Analysis**

**Update Frequency:**

1. Static GTFS data: monthly
2. Real-time: ?[every minute]
3. Headway Explorer: monthly (based on Static GTFS data)


## Data Collection

Real-time GTFS data will be constantly pulled from the 511 API, while static GTFS data will be pulled regularly but infrequently.

## Data Processing

**Figure 1. Data Processing Steps**
![Data Processing Model]() -- Lucidcharts

## Entity Relationship Diagram and Attribute Definitions
The documentation and metadata details for this data can be viewed here: 

**Figure 2. Entity Relationship Diagram**
![511 GTFS Feed Data Model]() --Lucidcharts

## Links to Resources

- [511 Developer Resources](https://511.org/developers/list/resources/)

- Create 511.org Developer API Key [here](https://511.org/developers/list/tokens/create)
- [Documentation pdf](http://assets.511.org/pdf/nextgen/developers/Open_511_Data_Exchange_Specification_v1.26_Transit.pdf) for 511 Transit API (found [here](https://511.org/developers/list/apis/))

- [Real-time GTFS API reference](https://developers.google.com/transit/gtfs-realtime/reference/)

- [Vehicle Position API reference](https://developers.google.com/transit/gtfs-realtime/reference/#VehiclePosition)

## Detailed Data Documentation

### 511 Transit GTFS API

The 511 Transit GTFS API is the **static** API for Operator IDs and GTFS feeds. Its API Base is http://api.511.org/transit.

#### GTFS Operator List API:

This is the 511 API for pulling a table of Operator IDs and names.  

**API Base**: http://api.511.org/transit/operators

**API call format**: http://api.511.org/transit/operators?api_key={YOUR 511 API KEY}&Format=XML


**NOTE**:

The Transit Operator table on [Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543) (available to MTC employees only) has fewer operators than the 511 GTFS Operator List (additional operators in **bold** in the 511 GTFS Operator List) and has suffixes (in *italics* in the boxnote Transit Operator table) appended to some agency names.


**Operator ID Listing from [Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543)**

Agency ID | Agency Name
:---: | :---:
3D | Tri Delta Transit
AC | AC Transit
AM | Capitol Corridor Joint Powers Authority
BA | Bay Area Rapid Transit
CC | County Connection
CE | Altamont Corridor Express
CM | Commute.org Shuttles
CT | Caltrain
DE | Dumbarton Express Consortium
EM | Emery Go-Round
FS | Fairfield and Suisun Transit
GF | Golden Gate Ferry
GG | Golden Gate Transit
MA | Marin Transit
MS | Stanford Marguerite Shuttle
PE | Petaluma Transit
RV | Rio Vista Delta Breeze
SA | Sonoma Marin Area Rail Transit
SB | San Francisco Bay Ferry
SC | VTA
SF | San Francisco Municipal Transportation Agency
SM | SamTrans
SO | Sonoma County Transit *LastGenerated*
SR | Santa Rosa CityBus *LastGenerated*
ST | SolTrans *LastGenerated*
TD | Tideline Marine Group Inc *LastGenerated*
UC | Union City Transit *LastGenerated*
VC | Vacaville City Coach *LastGenerated*
VN | Napa *LastGenerated*
WC | WestCat (Western Contra Costa) *LastGenerated*
WH | Livermore Amador Valley Transit Authority *LastGenerated*


**Operator ID Listing from 511 GTFS Operator List API**

Agency ID | Agency Name
:---: | :---:
3D | Tri Delta Transit
**5E** | **511 Emergency**
**5F** | **511 Flap Sign**
**5O** | **511 Operations**
**5S** | **511 Staff**
AC | AC Transit
AM | Capitol Corridor Joint Powers Authority
BA | Bay Area Rapid Transit
CC | County Connection
CE | Altamont Corridor Express
CM | Commute.org Shuttles
CT | Caltrain
DE | Dumbarton Express Consortium
EM | Emery Go-Round
FS | Fairfield and Suisun Transit
GF | Golden Gate Ferry
GG | Golden Gate Transit
MA | Marin Transit
MS | Stanford Marguerite Shuttle
**NV** | **Vine (Napa County)**
PE | Petaluma Transit
RV | Rio Vista Delta Breeze
SA | Sonoma Marin Area Rail Transit
SB | San Francisco Bay Ferry
SC | VTA
SF | San Francisco Municipal Transportation Agency
SM | SamTrans
SO | Sonoma County Transit
SR | Santa Rosa CityBus
**SS** | **Free South City Shuttle**
ST | SolTrans
TD | Tideline Marine Group Inc
UC | Union City Transit
VC | Vacaville City Coach
VN | Napa
WC | WestCat (Western Contra Costa)
WH | Livermore Amador Valley Transit Authority


#### 511 GTFS DataFeed Download API

This is the API for pulling static GTFS feeds for each operator ID. By default the data downloads as a Zip Archive  of the GTFS Data Feed (`agency.txt`, `calendar.txt`, etc.) for a singular operator.

**API Base**: http://api.511.org/transit/datafeeds?

**API call format**: http://api.511.org/transit/datafeeds?api_key={YOUR 511 API KEY}&operator_id={OPERATOR ID}  

**Example API call**: http://api.511.org/transit/datafeeds?api_key={YOUR 511 API KEY}&operator_id=3D


### 511 Transit GTFS-Realtime API

The 511 Transit GTFS-Realtime API is the **dynamic** API real-time GTFS trip updates and vehicle locations. Its API Base is http://api.511.org/Transit.


#### GTFS-Realtime Trip Updates API

**API Base**: http://api.511.org/Transit/TripUpdates?

**API call format**: http://api.511.org/Transit/TripUpdates?api_key={YOUR 511 API KEY}&agency={OPERATOR ID}

**Example API call**: http://api.511.org/Transit/TripUpdates?api_key={YOUR 511 API KEY}&agency=AC

The agencies for which there are no real-time GTFS Trip Update data available on the 511 API are below. The error messages are listed for each agency.

```python
 {<HTTPError 404: 'Not Found'>: ['5E', '5F', '5O', '5S', 'CE', 'AM',
							     'CM', 'EM', 'SS', 'GF', 'PE', 'RV',
							     'SB', 'SA', 'MS', 'TD', 'UC', 'VC',
							     'NV']
  }
 ```

#### GTFS-Realtime Vehicle Positions API

**API Base**: http://api.511.org/Transit/VehiclePositions?

**API call format**: http://api.511.org/Transit/VehiclePositions?api_key={YOUR 511 API KEY}&agency={OPERATOR ID}

**Example API call**: http://api.511.org/Transit/VehiclePositions?api_key={YOUR 511 API KEY}&agency=AC

The agencies for which there are no real-time GTFS Vehicle Position data available on the 511 API are below. The error messages are listed for each agency.

```python
{<HTTPError 404: 'Not Found'>: ['5E', '5F', '5O', '5S', 'CE', 'AM',
									  'CM', 'EM', 'SS', 'GF', 'PE', 'RV',
									  'SB', 'SA', 'MS', 'TD', 'UC', 'VC',
									  'NV'],
 <HTTPError 500: 'Internal Server Error'>: ['WH']
 }
```
