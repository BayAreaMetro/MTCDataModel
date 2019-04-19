-- Draft --

# 511 API GTFS (Realtime Transit Data Pipeline)

## Kearey's specs:

### Proposal:  
Create a Realtime Transit Data Pipeline that captures transit service feeds from transit providers in the region and saves this information to a database for future analysis.

More specifically, create a Python pipeline that pulls static and real-time GTFS data from the 511 API and posts the results to Redshift.

### Steps:
- Create transportation-mdm folder in mdm
- Post data documentation here: https://github.com/BayAreaMetro/DataServices/tree/master/Project-Documentation/mdm


### Code resources:

- Posting Pandas DataFrame to Redshift (skip intermediate posting to S3): http://measureallthethin.gs/blog/connect-python-and-pandas-to-redshift/  
- Building Lambda deployment packages with Docker: https://blog.quiltdata.com/an-easier-way-to-build-lambda-deployment-packages-with-docker-instead-of-ec2-9050cd486ba8


### Setup:

Create 511.org Developer API Key [here](https://511.org/developers/list/tokens/create)


### Links to Resources:  

- [Transit Service Data Processing boxnote](https://mtcdrive.app.box.com/notes/437400246543) (**only available to MTC employees**)

- [Tom's python script](https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/rtd/etl/get_511_current_gtfs_metadata_and_gtfs.py)

- [MTC's 511 GTFS API Data Documentation](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/511_GTFS.md)

