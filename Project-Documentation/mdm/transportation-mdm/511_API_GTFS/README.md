# 511 API GTFS (Realtime Transit Data Pipeline)

## Kearey's specs:

### Proposal:  
Create a Realtime Transit Data Pipeline that captures transit service feeds from transit providers in the region and saves this information to a database for future analysis.

More specifically, create a Python pipeline that pulls static and real-time GTFS data from the 511 API and posts the results to Redshift.

### Steps:
- Create transportation-mdm folder in mdm
- Post data documentation here: https://github.com/BayAreaMetro/DataServices/tree/master/Project-Documentation/mdm


### Code resources:

https://stackoverflow.com/questions/34983043/how-to-load-data-into-amazon-redshift-via-python-boto3

https://community.periscopedata.com/t/80fhrg/using-python-to-write-a-create-table-statement-and-load-a-csv-into-redshift


### Setup:

Create 511.org Developer API Key [here](https://511.org/developers/list/tokens/create)


**Kaya's 511.org Developer API Key**: c29e6173-f8a7-47b1-993a-63b92a316115

**Kearey's 511.org Developer API Key**: d6e9ad64-06b3-41d2-a4b2-2e3f540dd8f6


### Notes:

Swiftly works directly with agencies to monitor real-time bus locations, but as far as we can tell, all the data they provide is also publicly available through the 511 API (currently verifying for AC Transit). 


### Links to Resources:  
[511 Developer Resources](https://511.org/developers/list/resources/)   

[Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543)

[Tom's python script](https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/rtd/etl/get_511_current_gtfs_metadata_and_gtfs.py)

[Documentation pdf](http://assets.511.org/pdf/nextgen/developers/Open_511_Data_Exchange_Specification_v1.26_Transit.pdf) for 511 Transit API (found [here](https://511.org/developers/list/apis/))

[Real-time GTFS API reference](https://developers.google.com/transit/gtfs-realtime/reference/)

[Vehicle Position API reference](https://developers.google.com/transit/gtfs-realtime/reference/#VehiclePosition)



# Data Documentation


## 511 Transit GTFS API

The 511 Transit GTFS API is the **static** API for Operator IDs and GTFS feeds. Its API Base is http://api.511.org/transit.

### GTFS Operator List API:

This is the 511 API for pulling a table of Operator IDs and names.  

**API Base**: http://api.511.org/transit/operators

**API call format**: http://api.511.org/transit/operators?api_key={YOUR 511 API KEY}&Format=XML

**Example API call**: http://api.511.org/transit/operators?api_key=c29e6173-f8a7-47b1-993a-63b92a316115&Format=XML

The function **`get_operator_ids_from_511()`** in `ingest_511_GTFS.py` pulls a dictionary of Operator IDs and names and adds it to `config.py` as 511_OPERATOR_IDS. It is a combination of **`get_511_orgs_dict()`** and **`get_org_acronyms_from_511(dictionary)`** from Tom's file [`get_511_current_gtfs_metadata_and_gtfs.py` ](https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/rtd/etl/get_511_current_gtfs_metadata_and_gtfs.py)


**NOTE**:

The Transit Operator table on [Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543) has fewer operators than the 511 GTFS Operator List (additional operators in **bold** in the 511 GTFS Operator List) and has suffixes (in *italics* in the [boxnote](https://mtcdrive.app.box.com/notes/437400246543) Transit Operator table) appended to some agency names.

##### Operator ID Listing from [Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543)

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


##### Operator ID Listing from 511 GTFS Operator List API
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


### 511 GTFS DataFeed Download API

This is the API for pulling static GTFS feeds for each operator ID. By default the data downloads as a Zip Archive  of the GTFS Data Feed (`agency.txt`, `calendar.txt`, etc.) for a singular operator.

**API Base**: http://api.511.org/transit/datafeeds?

**API call format**: http://api.511.org/transit/datafeeds?api_key={YOUR 511 API KEY}&operator_id={OPERATOR ID}  

**Example API call**: http://api.511.org/transit/datafeeds?api_key=c29e6173-f8a7-47b1-993a-63b92a316115&operator_id=3D

The function **`pull_511_gtfs_static()`** in `ingest_511_GTFS.py` iterates through provided Operator IDs, loads their GTFS feed zipfile into memory, and appends their GTFS feed files to master feed DataFrames. Optionally writes these datafames to csv files (e.g. `stops_all_agencies.csv`), otherwise returns a dictionary of GTFS feed filenames and their master feed DataFrame

e.g. {'agency.txt': pandas DataFrame of concatenated agency.txt files from all agencies,  
      'calendar.txt': pandas DataFrame of concatenated calendar.txt files from all agencies, ...}  
      


## 511 Transit GTFS-Realtime API

This 

example real-time call:  http://api.511.org/Transit/TripUpdates?api_key=c29e6173-f8a7-47b1-993a-63b92a316115&agency=AC

OR

 http://api.511.org/Transit/VehiclePositions?api_key=c29e6173-f8a7-47b1-993a-63b92a316115&agency=AC



### GTFS-Realtime Trip Updates API


### GTFS-Realtime Vehicle Positions API