import glob
import os
import csv

os.chdir("Lab5")  # Change active directory to Lab5
print("Current active directory " + os.getcwd())
file_names = []

first_group = "first_group.txt"
second_group = "second_group.txt"

def isFileExists(filename):
    return os.path.isfile(filename)


def printAvailableFiles(filename):
    print("File does not exist " + filename)
    print("Available files:")

    # Print all txt files in the current directory
    for filename in glob.glob("*.txt"):
        file_names.append(filename)
        print(filename)


# Read all file in the active directory
def readFiles():

    print("All txt files in current directory:")

    # Print all txt files in the current directory
    for filename in glob.glob("*.txt"):
        file_names.append(filename)
        print(filename)

    print("\n")

    for filename in file_names:
        output_file_by_name(filename)


def output_file_by_name(filename):

    if not isFileExists(filename):
        printAvailableFiles(filename)
        return

    print("Reading the file with name: " + filename)

    # Open a file
    fd = open(filename, "r")

    # Read data from file
    reader = csv.reader(fd, delimiter="\t")

    # Print all data from file
    for row in reader:
        print(row)

    # Close the file
    fd.close()

    print("\n")


# Write to file
def write_to_file(filename):

    if not isFileExists(filename):
        printAvailableFiles(filename)

    fd = open(filename, "w")

    new_text = str(input("Enter a new text to write it to " +
                         filename + " \nSplit values by ';' \n"))

    new_text_array = new_text.split(";")
    write_string = ""

    for new_text_item in new_text_array:
        write_string = write_string + new_text_item.strip() + "\n"

    fd.write(write_string)

    fd.close()


# Append to file
def append_to_file(filename):
    if not isFileExists(filename):
        printAvailableFiles(filename)
        return

    fd = open(filename, "a")

    print("Enter stopWriting to stop the writing process")

    while True:
        new_line = input("Enter a new line \n")

        if new_line != "stopWriting":
            fd.write("\n"+new_line)
        else:
            return

    fd.close()


# Seek the file in the current dir
def search_file_in_dir(query):

    if(not isFileExists(query)):
        print("No file with name: " + query)
    else:
        output_file_by_name(query)


def search_text_in_file(filename, query):

    if(not isFileExists(filename)):
        printAvailableFiles(filename)
        return

    fd = open(filename, "r")
    # Read data from file
    reader = fd.readlines()

    # Print all data from file
    for row in reader:
        if query.lower() in row.lower():
            print(f"Found: {row}")

    # Close the file
    fd.close()

    print("\n")

def sort_marks_in_file(filename):
    dict = {}

    fd = open(filename, "r+")

    reader = fd.readlines()

    # Create dictionary key = mark, value = name
    for row in reader:
        split_row_by_coma = row.split(',')

        # first element is mark, zero element is name
        # strip to remove whitespaces
        dict[int(split_row_by_coma[1].strip())] = split_row_by_coma[0].strip()


    sorted_keys = list(dict.keys())

    #Bubble sort of keys
    for key in range(0, len(sorted_keys)):

        for j in range(0, len(sorted_keys) - key - 1):

            if sorted_keys[j] > sorted_keys[j+1]:
                sorted_keys[j], sorted_keys[j+1] = sorted_keys[j+1], sorted_keys[j]

    sorted_dict_by_key = {}
    for sorted_key in sorted_keys:
        sorted_dict_by_key[sorted_key] = dict[sorted_key]

    # Alternative of bubble sort. I want to use bubble sort just for fun
    # sorted_dict_by_int_key = sorted(dict.items())
    # print(sorted_dict_by_int_key)

    print(sorted_keys)
    print(sorted_dict_by_key)

    write_to_file_sorted_dict(filename, sorted_dict_by_key)

    fd.close()

def write_to_file_sorted_dict(filename, dict):

    fd = open(filename, "w")

    student_mark_strings_list = []

    for key in dict:
        student_mark_strings_list.append(f'{dict[key]}, {key}')

    write_string = ""

    for new_text_item in student_mark_strings_list:
        write_string = write_string + new_text_item.strip() + "\n"

    fd.write(write_string)

    fd.close()


#readFiles()
#write_to_file(first_group)
#append_to_file("second_group.txt")
#search_file_in_dir(second_group)
#search_text_in_file(second_group, "Willson")
sort_marks_in_file(second_group)
