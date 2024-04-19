# CSV handling option 2 - import csv
# This library saves us all the trouble of having
# to split the input into comma separated values
# and new lines
# A python list is automatically added as a row
# to the CSV file.

import csv

# This is a not on your reference guide, but "with open()"
# is a handier way to open a file, as it is
# automatically closed after (no need for file.close()

#Initialise our totals
sumAwards = sumNoms= 0
with open("oscar.csv","r") as file:
    allRecords = csv.reader(file)
    print(allRecords)
    allRecords = list(csv.reader(file))
    # We have to ignore the header row (or delete from .csv)
    # but the .csv file is more useful with the header
    processedHeader= False
    for movie in allRecords:
        # Work out the chances of winning if you are nominated
        # P(Winning) = #awards/#nomination ie col3/col4
        if processedHeader == True:
            sumAwards += int(movie[2])
            sumNoms += int(movie[3])
        processedHeader = True
print(sumAwards,sumNoms)
# Overall average chance is
probWin = sumAwards/sumNoms
print("Chance of winning",probWin)

