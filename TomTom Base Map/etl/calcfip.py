import arcpy

fc = "E:/1sfoo/tana/New File Geodatabase.gdb/a8"
field = "COUNTYFIP"
cursor = arcpy.SearchCursor(fc)

for row in cursor:
    arcpy.AddMessage(row.getValue(field))
   
