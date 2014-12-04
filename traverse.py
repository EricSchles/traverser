import os
from sys import argv

def process(file):
    if file.endswith(".py"):
        print os.path.abspath(file)
    else:
        print "not python file :P"

for root,dir,files in os.walk(argv[1]):
    for file in files:
        file = os.path.join(root,file)
        process(file)
