import csv 
import glob
import os

os.chdir("Lab5")
print("Current active directory " + os.getcwd())

file1 = "first_group.txt"
file2 = "second_group.txt"

def isFileExisting(filename):
    return os.path.isfile(filename)

def outputFileByName(filename):
    print('File ' + filename)
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()

def readFiles():
    fd1=open(file1, 'r')
    reader = csv.reader(fd1, delimiter="\t")
    print('\nfirst group:')
    for row in reader:
        print(row)

    fd2=open(file2, 'r')
    reader = csv.reader(fd2, delimiter="\t")
    print('\second group:')
    for row in reader:
        print(row)

    fd1.close()
    fd2.close()