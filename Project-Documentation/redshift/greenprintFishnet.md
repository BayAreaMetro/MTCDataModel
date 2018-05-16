# Redshift Database - Greenprint Fishnet

## About the Feature Set
Blah Blah Blah Blah


#### Greenprint fishnet table structure
  
Field Name | Definition | Unit | Math to be Performed | Theme | Glossary Reference 
--- | --- | --- | --- | --- | --- 
wb303d | Yes/No presence of 303d listed waterbody (1 = yes) | Yes/No | > 0 = "Yes" | Water | _**Impaired waterbodies**_ 
ln303d | Yes/No presence of 303d listed stream (1 = yes) | Yes/No | > 0 = "Yes" | Water | _**Impaired waterways - 303d listed streams**_ 
vuln_ac | Acres of areas with high permeability, therefore high recharge potential. Same for both areas with high recharge potential and hydrologically vulnerable areas. | Acres | Sum | Water | _**Areas with high recharge potential**_ and _**Hydrogeologically Vulnerable areas**_ 
pgb | Yes/No area of interest overlaps with a priority groundwater basin (1 = yes) | Yes/No | > 0 = "Yes" | Water | _**Priority groundwater basins**_ 
rca | Yes/No area of interest overlaps with a reservoir catchment area (1 = yes) | Yes/No | > 0 = "Yes" | Water | _**Reservoir catchment areas**_ 
fl100_ac | Acres within a 100 year flood area | Acres | Sum | Water | _**100 year Floodplain**_ 
fl500_ac | Acres within a 500 year flood area | Acres | Sum | Water | _**500-year Floodplain**_ 
drink_ac | Acres of drinking water watershed | Acres | Sum | Water | _**Municipal drinking water supply watersheds**_ 
wq_val | Average value of water quality index. NOTE: null values were replaced with -999, you must filter those out before calculating an average value. | Mean | Mean (compare to Bay Area-wide mean of 0.49033) | Water | _**Water quality index**_ 
runoff | Acre-feet per year of water | Acre-feet per year | Sum | Water | _**Runoff**_ 
recharge | Acre-feet per year of water | Acre-feet per year | Sum | Water | _**Groundwater recharge**_ 
natbay_ac | Acres of natural baylands and coastal resilient areas | Acres | Sum | Water | _**Natural Baylands**_ and _**Coastal Resilience**_ 
slr2050_ac | Acres within 2050 inundation zone | Acres | Sum | Water | _**Sea level rise**_ 
slr2100_ac | Acres within 2100 inundation zone | Acres | Sum | Water | _**Sea level rise - 5' inundation area**_ 
fpb_ct | Count of fish barriers (priority and total, combined) | Count | Sum | Biodiversity & Habitat | _**Fish passage priority and total barriers (combined)**_ 
krc_mi | Miles of key riparian corridor | Miles | Sum | Biodiversity & Habitat | _**Key Riparian Corridor**_ 
block_ac | Acres of large landscape blocks | Acres | Sum | Biodiversity & Habitat | _**Bay Area Critical Linkages - Large Landscape Blocks**_ 
link_ac | Acres of critical linkages | Acres | Sum | Biodiversity & Habitat | _**Bay Area Critical Linkages - Linkage**_ 
bayland_ac | Acres of baylands | Acres | Sum | Biodiversity & Habitat | _**Baylands**_ 
pinch | Yes/No within a half-mile of linkage with pinch points (1 = yes) | Yes/No | > 0 = "Yes" | Biodiversity & Habitat | _**Linkage highway barrier**_ 
vernal_ac | Acres of vernal pools | Acres | Sum | Biodiversity & Habitat | _**Vernal Pools**_ 
wetl_ac | Acres of wetlands | Acres | Sum | Biodiversity & Habitat | _**Wetlands**_ 
ref1_ac | Percent of prioritized natural habitats in your area of interest that will remain in suitable climates | Acres | Sum (ref1_ac), divide by Sum (exp_t_ac) | Biodiversity & Habitat | _**Landscape refugia**_ 
exp_t_ac | Acres of prioritized natural habitats (denominator for ref1_ac, exp1_ac) | Acres | Sum | Biodiversity & Habitat | _**Prioritized natural habitats (Landscape refugia; Exposure)**_ 
exp1_ac | Percent of prioritized natural habitats in your area of interest that will be in marginal climates | Acres | Sum (exp1_ac), divide by Sum (exp_t_ac) | Biodiversity & Habitat | _**Exposure**_ 
cnddb | Yes/No presence of CNDDB listed species (1 = yes) | Yes/No | > 0 = "Yes" | Biodiversity & Habitat | _**CNDDB Rare and Protected Species**_ 
ramp | Average value of habitat mitigation measure (breaks provided). NOTE null values were replaced with -999, you must filter those out before calculating an average value. | Mean | Mean | Biodiversity & Habitat | _**Hotspots of species requiring compensatory mitigation**_ 
clnefi_ac | Acres of important/essential/fragmented lands | Acres | Sum | Biodiversity & Habitat | _**Conservation Lands Network**_ 
rc_d | Acres of regional connectivity - Diffuse | Acres | Sum * 0.222395 | Biodiversity & Habitat | _**Regional Connectivity - Diffuse**_ 
rc_c | Acres of regional connectivity - Channelized | Acres | Sum * 0.222395 | Biodiversity & Habitat | _**Regional Connectivity - Channelized**_ 
rc_i | Acres of regional connectivity - Intensified | Acres | Sum * 0.222395 | Biodiversity & Habitat | _**Regional Connectivity - Intensified**_ 
trl_e_mi | Miles of existing regional trails | Miles | Sum | Recreation | _**Regional Trails - existing**_ 
trl_p_mi | Miles of proposed regional trails | Miles | Sum | Recreation | _**Regional Trails - proposed**_ 
cpad_or_ac | Acres of publicly-accessible fee lands (from BPAD flat file, filtered to lands with Open or Restricted Access) | Acres | Sum | Recreation | _**Publicly accessible recreational lands**_ 
graz_ac | Acres of grazing land, per FMMP | Acres | Sum | Agriculture | _**Suitable Grazing land**_ 
local_ac | Acres of farmland of local importance, per FMMP | Acres | Sum | Agriculture | _**Farmland of Local Importance**_ 
prime_ac | Acres of prime farmland, per FMMP | Acres | Sum | Agriculture | _**Prime farmland**_ 
state_ac | Acres of farmland of state importance, per FMMP | Acres | Sum | Agriculture | _**Farmland of Statewide Importance**_ 
unique_ac | Acres of unique farmland, per FMMP | Acres | Sum | Agriculture | _**Unique farmland**_ 
allfarm_ac | Acres of grazing and all categories of farmland, per FMMP (for use as metric denominator) | Acres | Sum | Agriculture | _**Agricultural lands**_ 
idle0_ac | Percent of farmland (crops) in your area of interest not fallowed in recent years | Acres | Sum (idle0_ac), divide by Sum (idle01_ac) | Agriculture | _**Fallow cropland**_ 
idle01_ac | Total acres of farmland for which fallowing was tracked (metric denominator) | Acres | Sum | Agriculture | _**Fallow cropland**_ 
cropval | Dollar value of crop production, according to Ag Commissioner's data | Dollar value | Sum | Agriculture | _**Crop production**_ 
crnm | Additional acre-feet per year needed for agriculture in a warmer and wetter climate change scenario | Acre-feet per year | Sum | Agriculture | _**Additional water (mm) for irrigation - warmer and wetter**_ 
miroc | Additional acre-feet per year needed for agriculture in a hotter and drier climate change scenario | Acre-feet per year | Sum | Agriculture | _**Additional water (mm) for irrigation - hotter and drier**_ 
cced_ac | Acres of easement lands, CCED 2016 | Acres | Sum | Overview | _**Conservation easement**_ 
cpad_ac | Acres of fee lands, CPAD 2016b | Acres | Sum | Overview | _**Protected lands by fee**_ 
resi_val | Mean value of resilience measure. NOTE: null values were replaced with -999, you must filter those out before calculating an average value | Mean | Mean (compare to Bay Area-wide mean of 0.50497) | Biodiversity & Habitat | _**Landscape Resilience - resilient areas**_ 
natri_ac | Acres of natural river area | Acres | Sum | Water | _**Naturalness of Active River Area**_ 
te_val | Average value of important habitat for threatened and endangered vertebrates (breaks provided). NOTE: null values were replaced with -999, you must filter those out before calculating an average value. | Mean | Mean | Biodiversity & Habitat | _**Important habitat for T&E Vertebrates**_ 
soc0_30 | Metric tons of carbon stock in soil | Metric tons | Sum | Carbon | _**Soil Carbon Storage**_ 
ba_agc | Metric tons of carbon stock above ground | Metric tons | Sum | Carbon | _**Aboveground live carbon storage**_ 
fl500na_ac | Naturalness of area within 500-year floodplain | Acres | Sum | Water | _**Naturalness of 500-year floodplain**_ 
lat | Latitude of centroid. Added by Metropolitan Transportation Commission's Data & Visualization group | | | | 
long | Longitude of centroid. Added by Metropolitan Transportation Commission's Data & Visualization group | | | | 
wkt | Well known text value for centroid. Added by Metropolitan Transportation Commission's Data & Visualization group for use in map applications | | | | 
