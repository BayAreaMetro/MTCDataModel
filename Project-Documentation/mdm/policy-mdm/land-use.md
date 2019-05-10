-- Draft --
# Regional Land Use Data

## Description
MTC collects land use data from local jurisdictions for use in the development of regional growth strategies, and long range transportation planning efforts. These Land Use Policies are designated by local jurisdictions to manage future development and growth within their respective jurisdictions.

## Purpose and Use  
Used in MTC Land Use Modeling, Housing Policy and Long Range Planning Research.

## Data Collection
This data was compiled using local information collected from each of the 109 jurisdictions in the San Francisco Bay Area Region.  A Document inventory was developed to track key information collected and used to process this data for regional modeling and policy based uses.

### Regional General Plan and Zoning Document Inventory
This dataset is used to manage the collection of key documents used in the preparation of the Planning and Zoning 2018 dataset. It contains key information used to develop the Regional General Plan and Zoning Datasets such as source documents, maps and links to jurisdiction general plan and zoning documents. 

[Click Here to View the Inventory](https://mtc.data.socrata.com/dataset/Regional_General_Plan_Zoning_Document_Inventory/akeh-uvij). 

### Regional Parcel Characteristics Inventory
This... (Joshua to update documentation for this work here...)


Currently this view is private and for internal agency viewers exclusively and Requires Socrata Login Credentials to view.  Contact a DataViz Team Member Should you require access to this inventory list.  This list is also available to authenticated users of the BASIS System (Will be enabled soon). 

[Data Lens - Read Only](https://mtc.data.socrata.com/view/dwzg-k3ei)

## Data Processing
This data is generated using a combination of sources and methods (mainly ArcGIS Spatial Processing and MSSQL Spatial Queries). The inital data processing was performed on the Top 20 jurisdictions in the region with the largest population.  Digital data was collected from these jurisdictions and processed using ArcGIS and MSSQL Server using a simple point in poly method which assigns land use codes to parcel geometry based upon the location of the polygon centroid of each parcel in relation to the land use polygons contained in the source spatial datasets for these jurisdictions. See the figure below for a high level view of the data processing that was performed. 

Further processing included direct parcel assignment of land use for both zoning and general plan designations as presented on local jurisdiction planning documents, as well as using the assessor's parcel characteristics data for existing land uses on a given parcel, in most cases this is defined as use codes.  

## Datasets
Three datasets have been prepared using this process.  They are as follows:  
- Existing Land Uses (Source: County Assessor's Parcel Characteristics that identify use code)
- Regional Zoning (Source: Local Jurisdiction Planning Documents, Assessor's Parcel Characteristics for zoning)
- Regional General Plan (Source: Local Jurisdiction Planning Documents)

**Figure 1. Data Processing Steps**
![Data Processing Model](images/gp-zn-data-modeling.png)

#### Entity Relationship Diagram and Attribute Definitions
The documentation and metadata details for this data can be viewed here: [General Plan and Zoning 2018](https://mtc.data.socrata.com/Land-Use/General-Plan-and-Zoning-2018/udk3-z2d5)

**Figure 2. Entity Relationship Diagram**
![Land Use Data Model](images/Land-Use-Data-ERD.png)
Click [Here](https://www.lucidchart.com/documents/view/1fe3f1ba-8879-428e-8eb6-66157baf78b7/1) for interactive versions of Figures 1 and 2.

**Note**:
Attribute Definitions can be viewed [Here](https://mtc.data.socrata.com/Land-Use/General-Plan-and-Zoning-2018/udk3-z2d5).

This data is related to the [Parcels 2018 Dataset](https://mtc.data.socrata.com/Cadastral/Region-Parcels-2018-/fqea-xb6g) table using the joinid field.

Data Steward: DataViz Team
