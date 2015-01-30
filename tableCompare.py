# Name: Anand Patel (23anandpatel23@gmail.com)
# Purpose: This script will compare sets for updating, adding, and deletes. It's meant for set theory practice rather than application
import csv
import sys
import os
import string

def insert(original, new, pos):
   """Inserts new inside original at pos."""
   return original[:pos] + new + original[pos:]

def main():

    record1 = 'record1|100|102014'
    insert(str(record1),'record5',4)

    print record1



    # Create tables with columns for name|size|date_modified
    recA = {"record1|100|102014", "record2|200|103014", "record4|400|102514"}
    recB = {"record3|300|102514", "record1|100|102014", "record2|200|103014"}
    recTot = {}
    # Remove the records from A that are also in B
    # recA - recB

    # Remove the records from B that are also in A
    # recB - recA

    userUpdate = raw_input("Select field to update (name, size, date_modified, or none")
    recToBeUpdated = raw_input("Which record name do you want to update")

    if ( userUpdate == "none"):
        pass

    elif (userUpdate == "name"):
        nameUpdate = raw_input("Enter name: ")
        if recToBeUpdated in recA:
                recA.remove(str(recToBeUpdated))
                recA.add(str(nameUpdate) + str())

    elif (userUpdate == "size"):
        sizeUpdate = raw_input("Enter size: ")

    elif ( userUpdate == "date_modified"):
        modUpdate == raw_input("Enter date_modified: ")

    else:
        print "Invalid answer"




    print recA
    print recB
    print recTot




if __name__ == '__main__':
    main()
