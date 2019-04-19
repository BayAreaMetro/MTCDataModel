-- Draft --

# 511 API GTFS (Realtime Transit Data Pipeline)

(example project documentation [here](https://github.com/BayAreaMetro/RegionalTransitDatabase/blob/master/docs/transit_priority_areas.md))

## Problem Statement

Create a Realtime Transit Data Pipeline that captures transit service feeds from transit providers in the region and saves this information to a database for future analysis.

More specifically, create a Python pipeline that pulls static and real-time GTFS data from the 511 API and posts the results to Redshift.

### Project Management 

**Project links:**

- [Asana task](https://app.asana.com/0/1118125447711060/1118125279909441) (**visible to MTC employees only**)
- [Project Box folder](https://mtcdrive.app.box.com/folder/72791032857) (**visible to MTC employees only**)

## Data Sources

- [MTC 511 API](https://511.org/developers/list/apis/): Documentation [here](https://github.com/BayAreaMetro/DataServices/blob/master/Project-Documentation/mdm/transportation-mdm/511_GTFS.md)


## Methodology

Create 511.org Developer API Key [here](https://511.org/developers/list/tokens/create)

## Expected Outcomes



## Results




## Appendix:

### Code resources:

- Posting Pandas DataFrame to Redshift (skip intermediate posting to S3): http://measureallthethin.gs/blog/connect-python-and-pandas-to-redshift/  
- Building Lambda deployment packages with Docker: https://blog.quiltdata.com/an-easier-way-to-build-lambda-deployment-packages-with-docker-instead-of-ec2-9050cd486ba8
