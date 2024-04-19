# CSV handling option 1 - basic python readline()

# This is a not on your reference guide, but "with open()"
# is a handier way to open a file, as it is
# automatically closed after (no need for file.close()

#Initialise our totals
sumAwards = sumNoms= 0
with open("oscar.csv","r") as file:
    movieDetails = file.readline()
    headers = movieDetails.split(",")
    print(headers)
    for movieDetails in file.readlines():
        movie = movieDetails.split(",")
        # Work out the chances of winning if you are nominated
        # P(Winning) = #awards/#nomination ie col3/col4
        
        sumAwards += int(movie[2])
        sumNoms += int(movie[3])

print(sumAwards,sumNoms)
# Overall average chance is
probWin = sumAwards/sumNoms
print("Chance of winning",probWin)

