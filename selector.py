import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--destination", "-d", help="set destination path")
parser.add_argument("--file", "-f", help="set the path of the file with names")
parser.add_argument("--location", "-l", help="set the path of the dircectory with the files")
parser.add_argument("--extension", "-e", help="set the extension files name")
args = parser.parse_args()

directory = os.getcwd()

if args.info:
    print("-d or --destination to set output path, --file or -f set the path of input file list, --location or -l set the path of the output directory (default is corrent working directory), --extension or -e adds extension to input file name (write it without .) ")
    exit()
if args.destination:
    destination = args.destination
if args.file:
    paper = args.file
if args.location:
    directory = args.location
if args.extension:
    extension = args.extension


names = open(paper,"r")
array = []

with open("names.txt","r") as names:
    for name in names.read().splitlines():
        array.append(name+"."+extension)
    names.close()

for position in array:
    for document in os.listdir(directory):
        if position == document:
            shutil.move(document,destination)
        else:
            pass
