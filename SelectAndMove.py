import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--action', '-a', help= 'select the action you want to do (move or copy)')
parser.add_argument('--interactive', '-i', help="to start the interactive mode", action = 'store_true')
parser.add_argument("--destination", "-d", help="to set output path")
parser.add_argument("--file", "-f", help="set the path of input file list")
parser.add_argument("--location", "-l", help="set the path of the target directory (default is corrent working directory)")
parser.add_argument("--extension", "-e", help="adds extension to input file name (write it without .)")
args = parser.parse_args()

directory = os.getcwd()
array = []
extension = ""

if args.action:
    action = args.action
if args.destination:
    destination = args.destination
if args.file:
    ls = args.file
if args.location:
    directory = args.location
if args.extension:
    extension = "."+args.extension
if args.interactive:
    action = input("select the action you want to do (move or copy):\n")
    ls = input("set the path of input file list:\n")
    destination = input("to set output path:\n")
    extension = input("adds extension to input file name (write it without .):\n")
    directory = input("et the path of the target directory (default is corrent working directory):\n")



with open(ls,"r") as names:
    for name in names.read().splitlines():
        array.append(name + extension)
    names.close()

if os.path.isdir(destination):
    pass
else:
    os.mkdir(destination)
            
if action == "copy":
    for position in array:
        for document in os.listdir(directory):
            if position == document:
                shutil.copy(document,destination)
            else:
                pass
elif action == "move":
    for position in array:
        for document in os.listdir(directory):
            if position == document:
                shutil.move(document,destination)
            else:
                pass
