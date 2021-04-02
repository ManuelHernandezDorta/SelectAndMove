# SelectAndMove
A CLI script that select files from a directory based in an input list in txt format and move it to another directory

## Use:
It's simple to use this script. Use either arguments or edit the script (this is slower)

### Arguments:
Type python selector -h to read help

Next there is a list:

--destination or -d, to set output path i.e. -d ./testdir<br/>
--file" or -f, to set the name/path for the input list file i.e.  -f list.txt<br/>
--location or -l, to set the name/ path for the target directory (default is current working directory)<br/>
--extension or -e, to add an extension to the input file name (write it without .) i.e. -e txt<br/>
--action or -a, to select the action you want to do (move or copy)<br/>

if there is any problem with the script try to enter the full path in each argument

## list:
This script needs a list in .txt format, that must have a format to make possible the script to read it. Here is an example<br/>


file_1<br/>
file_2<br/>
file_3<br/>
.<br/>
.<br/>
.<br/>


Each name must be in a different line and it's not necessary that the name have the extension, because you can add it by the -e argument (the extension must be introduced without ".", for exmanple)
```python 
-e txt
```
