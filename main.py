import subprocess
from threading import Thread
import csv
import time
import os

def subproc(i,file):
	subprocess.call("python parser.py " + str(file), shell=True)

if __name__ == "__main__":
	files = ["typeids1.csv", "typeids2.csv", "typeids3.csv", "typeids4.csv"]
	Thread(target=subproc, args= (1,files[0])).start()
	Thread(target=subproc, args= (1,files[1])).start()
	Thread(target=subproc, args= (1,files[2])).start()
	Thread(target=subproc, args= (1,files[3])).start()
	