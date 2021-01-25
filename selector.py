import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--destination", "-d", help="to set output path")
parser.add_argument("--file", "-f", help="set the path of input file list")
parser.add_argument("--location", "-l", help="set the path of the target directory (default is corrent working directory)")
parser.add_argument("--extension", "-e", help="adds extension to input file name (write it without .)")
args = parser.parse_args()

directory = os.getcwd()
array = []

if args.destination:
    destination = args.destination
if args.file:
    paper = args.file
if args.location:
    directory = args.location
if args.extension:
    extension = args.extension

with open(paper,"r") as names:
    for name in names.read().splitlines():
        array.append(name+"."+extension)
    names.close()

for position in array:
    os.chdir(directory)
    for document in os.listdir(directory):
        if position == document:
            shutil.move(document,destination)
        else:
            pass
