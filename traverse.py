import os
from sys import argv

def process(file):
    if file.endswith(".py"):
        print os.path.abspath(file)
    else:
        print "not python file :P"

for root,dir,files in os.walk(argv[1]):
    [os.path.join(os.getcwd(),elem) for elem in root]
    [os.path.join(os.getcwd(),elem) for elem in dir]
    for file in files:
        process(file)
