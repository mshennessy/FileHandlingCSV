# This library saves us all the trouble of having
# to split the input into comma separated values
# and new lines
# A python list is automatically added as a row
# to the CSV file.

import csv

# This is a not on your reference guide, but "with open()"
# is a handier way to open a file, as it is
# automatically closed after (no need for file.close()

with open("student.csv","r") as file:
    allRecords = list(csv.reader(file))
    print(allRecords)

print(" Can you print the details of the CSV file more nicely?")
print("Note that it is a list of lists [[ at the start and end ]]")
print("Like this [[1,2,3],[4,5,6],[7,8,9]]")
