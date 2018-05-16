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
