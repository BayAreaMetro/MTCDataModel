FOR /F %%x IN (filelist.txt) DO (if not exist ".\tables\%%x" (if not exist ".\%%x\*.shp" (mkdir ".\tables\%%x" 
move ".\%%x\*" ".\tables\%%x\")))
