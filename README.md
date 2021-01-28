# SelectorAndMove
A CLI script that select files from a directory based in an input list in txt format and move it to another directory

## Use:
It's simple to use this script, the only fact that you should worry about is the arguments that must be introduce in the command line or edditing the script (this is slower)

### Arguments:
if you use the command below it will sow all the posibles arguments and their description
''' python
python selector.py -h
'''
However here is a list with the same information to make it easier to unsderstand:<br/>

--destination or -d, to set output path<br/>
--file" or -f, set the path of input file list<br/>
--location or -l, set the path of the target directory (default is corrent working directory)<br/>
--extension or -e, adds extension to input file name (write it without .)<br/>

if there is any problem with the script try to enter the entiry path from the root in each argument

## list:
This script needs a list in .txt format, this list must have a certain format to make possible the script to read it, here is an example<br/>

'''txt
file_1<br/>
file_2<br/>
file_3<br/>
.<br/>
.<br/>
.<br/>
'''

Each name must be in a different line and it's not necessary that the name have the extension, because you can add it by the -e argument (the extension must be introduced without ".", for exmanple)
'''python 
-e txt
'''
