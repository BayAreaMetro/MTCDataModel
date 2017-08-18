if exist filelist.txt (del filelist.txt)
for %%y in (usauc1*.dbf) do (@echo %%~ny >> filelist.txt)

for %%y in (usauc2*.dbf) do (@echo %%~ny >> filelist.txt)

for %%y in (usauc3*.dbf) do (@echo %%~ny >> filelist.txt)

for %%y in (usauc4*.dbf) do (@echo %%~ny >> filelist.txt)

for %%y in (usauc5*.dbf) do (@echo %%~ny >> filelist.txt)

for %%y in (usauc6*.dbf) do (@echo %%~ny >> filelist.txt)