import subprocess
from threading import Thread
import csv
import time
import os

# def subproc(i,file):
# 	subprocess.call("python parser.py " + str(file), shell=True)

if __name__ == "__main__":
	subprocess.call("python parser.py typeids.csv", shell=True0)