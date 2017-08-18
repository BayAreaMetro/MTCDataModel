for /F %%x in (filelist.txt) do (


if not exist ".\%%x" (
mkdir %%x
move "usauc1___________%%x."* ".\%%x"
move "usauc2___________%%x."* ".\%%x"
move "usauc3___________%%x."* ".\%%x"
move "usauc4___________%%x."* ".\%%x"
move "usauc5___________%%x."* ".\%%x"
move "usauc6___________%%x."* ".\%%x"))
