import arcgisscripting
import arcpy, string, os, sys
from arcpy import env
gp = arcgisscripting.create(9.3)

# Get the Parameters
inputfolderPath = gp.getparameterastext(0)
outputfolderPath = gp.getparameterastext(1)
failMergeList = []
try:
    for filename in os.listdir(inputfolderPath):
        fullpath = os.path.join(inputfolderPath, filename)
        arcpy.env.workspace = fullpath
        fcs = arcpy.ListFeatureClasses()
        merge_dir = arcpy.env.workspace

        bname = os.path.basename(merge_dir)
        foldername = bname.partition("-")
        arcpy.AddMessage(foldername[0])
        merge = outputfolderPath + os.sep + foldername[0]+".shp"
        try:
            if fcs and not os.path.exists(merge):
                arcpy.Merge_management(fcs, merge)
        except:
            failMergeList.append(merge)
            arcpy.AddWarning("Error on: " + merge)
         
except:
    arcpy.AddWarning("Error merging: "+merge)

if len(failMergeList)>0:
    arcpy.AddWarning("Failed to merge: "+ "' ".join(map(str,failMergeList)))   
    
