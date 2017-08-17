for /F %%x in (filelist.txt) do (
if not exist ".\%%x" (mkdir %%x)
)