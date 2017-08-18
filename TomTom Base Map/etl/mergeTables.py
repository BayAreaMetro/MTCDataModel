import arcgisscripting
import arcpy, string, os, sys
from arcpy import env
gp = arcgisscripting.create(9.3)

# Get the Parameters
inputFolderPath = gp.getparameterastext(0)
outputFolderPath = gp.getparameterastext(1)
global errorTbls
errorTbls = []

for filename in os.listdir(inputFolderPath):
    try:
        fullpath = os.path.join(inputFolderPath, filename)
        arcpy.env.workspace = fullpath
        fcs = arcpy.ListTables()
##        arcpy.AddMessage(fcs)
        
        if len(fcs)>0:
            
            #get new folder name and make tbl
            bname = os.path.basename(fullpath)
            concat1=bname
            
            #to handle old folder naming syntax with hyphens "fe-Ferries"
            concat2=concat1.split("-")
            newtblname=concat2[0]
            arcpy.AddMessage (newtblname)
            
            newtblname1 = outputFolderPath + os.sep + newtblname + ".dbf"

            #create new folder 
            arcpy.CopyRows_management (fcs[0], newtblname1)
##            arcpy.AddMessage("Copied rows to new table")

            if len(fcs)>1:
                #delete all rows in tbl
                arcpy.DeleteRows_management(newtblname1)
##                arcpy.AddMessage("Deleted rows")

                #append all tbls into newtbl
                arcpy.Append_management(fcs, newtblname1)
##                arcpy.AddMessage("Appended tables successfully")

            arcpy.AddMessage("successfully merged")   
    except:
        errorTbls.append(concat1)
        arcpy.AddWarning("Error merging " + concat1)
        
if len(errorTbls)>0:
    arcpy.AddWarning("Error merging: " + ', '.join(map(str,errorTbls)))
        
    

    
    
