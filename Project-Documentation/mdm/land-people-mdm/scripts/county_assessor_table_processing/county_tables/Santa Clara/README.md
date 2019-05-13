# Santa Clara


## County Data Sources

### sf902

Category: Unknown

APN: non-unique (Total: 518,463 ; Unique APNs: 489,475)

Building ID (unique):  APN + HOUSE_NUMBER + UNIT_NUMBER + SITUS_SEQ_NUM

`dfsf902['building_id'] = ('A' + dfsf902['APN'].astype(str)
                          + 'H' + dfsf902['HOUSE_NUMBER'].astype(str)
                          + 'U' + dfsf902['UNIT_NUMBER'].astype(str)
                         + 'SS' + dfsf902['SITUS_SEQ_NUM'].astype(str))`


### mf901

Category: Assessor's Master File

APN: unique


### pc851agm

Category: Agricultural

APN: unique


### pc851ci

Category: Commercial/Industrial

APN: non-unique (Total: 22,964; Unique APNs: 21,366)

Building ID (non-unique): APN + BUILDING_NUM

`dfpc851ci['building_id'] = ('A' + dfpc851ci['APN'].astype(str)
                          + 'B' + dfpc851ci['BUILDING_NUM'].astype(str))`

Note: Non-unique building ID appears to be same record with different versions of data (e.g. dfpc851ci.iloc[9424:9426])

(Identify with `dfpc851ci.groupby('building_id').size().sort_values(ascending=False).head()`)




### pc851mf

Category: Multi-Family

APN: non-unique (Total: 21,078; Unique APNs: 20,752)

Building ID (non-unique): APN + BUILDING_NUM

`dfpc851mf['building_id'] = ('A' + dfpc851mf['APN'].astype(str)
                          + 'B' + dfpc851mf['BUILDING_NUM'].astype(str))`

Note: Non-unique building ID appears to be same record with different versions of data (e.g. dfpc851mf.iloc[16039:16041]) 


### pc851sf

Category: Single-Family

APN: non-unique (Total: 431,115; Unique APNs: 428,923)

Building ID (non-unique): APN + BUILDING_NUM

`dfpc851sf['building_id'] = ('A' + dfpc851sf['APN'].astype(str)
                          + 'B' + dfpc851sf['BUILDING_NUM'].astype(str))`

Note: Non-unique building ID appears to be same record with different versions of data (e.g. dfpc851sf.iloc[12130:12133]) 

## Urbansim Column Mapping

### Buildings

`urbansim_buildings_colmapping = {'apn': 'apn_county_provided',
                                 'citystate': 'jurisdiction_county_provided',
#                                  '': 'parcel_id',  # same as joinid?
#                                  'building_num': 'building_id',  # unique to each building: computed from original tables
                                 'use_code': 'building_type', # need mapping to types defined by urbansim
                                 'usable_sq_feet': 'building_sqft',
                                 'total_area - building_sqft': 'non_residential_sqft',  # non_residential_sqft = total_area - building_sqft
                                 'number_units': 'residential_units',
                                 'year_built': 'year_built',
                                 'securedimprove': 'assessed_building_value',
                                 'date_updated': 'assessed_date',
#                                  '': 'last_sale_price',  # not provided by Santa Clara
                                 'datetransfer': 'last_sale_date',
                                 "case when rentable_area/total_area < .5 then 'own' else 'rent' end": 'tenure',  # if less than 50% rented, then 'own'
#                                  '': 'rent_type'  # not provided by Santa Clara
                                }
`

