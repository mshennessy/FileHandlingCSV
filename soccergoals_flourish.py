# G Hennessy 2024
# This file takes a soccer goals dataset which has a row for every match player goal
# And changes it to a dataset that looks like this
# Player URL                  1916  1901 1902 ... 2024
# messi  argentinaURL.html      0     0    0       56
# etc

# The original data set contained country names only. Flourish looks better with flags
# so countries.csv is opened and processed to match country names with the URL of the flags
# This is a pain to do as some flags were missing (defunct countries like yugoslavia or
# other smaller countries like Wales had to be added manually)

# For data analysis
import pandas as pd
# for creating a new csv file
import csv

# function to sort players into decades which will be shown in
# different colours on the flourish bar-chart
def decadeFinder(yearIn):
    if yearIn < 1920:
        return "1910s"
    elif yearIn < 1930:
        return "1920s"
    elif yearIn < 1940:
        return "1930s"
    elif yearIn < 1950:
        return "1940s"
    elif yearIn < 1960:
        return "1950s"
    elif yearIn < 1970:
        return "1960s"
    elif yearIn < 1980:
        return "1970s"
    elif yearIn < 1990:
        return "1980s"
    elif yearIn < 2000:
        return "1990s"
    elif yearIn < 2010:
        return "2000s"
    elif yearIn < 2020:
        return "2010s"
    else:
        return "2020s"
    
# For testing purposes only - so I can test a smaller data-set more quickly
endYear=int(input("Year to finish?"))
# If the enter 2024, we need to set up a for year in range(2025)
endYear +=1

# read csv file of countries and flag URLS into two lists
# then zip these into a single dictionary object
df3 = pd.read_csv('countries.csv')
countryList= list(df3["country"])
urlList= list(df3["image_url"])
flagsDict=dict(zip(countryList,urlList))

#Test to show how to find an entry in a dictionary of key:value pairs
#print(flagsDict["Ireland"])

# initialise a list of years covered by the data
years=[]
for i in range(1916,endYear):
    years.append(i)

# df1 is the raw data read from the CSV file of players and goals
# Note this is not the original file taken from kaggle.com
# It has been pre-processed so that dates are turned into years only
df1 = pd.read_csv('goals_tidied_utf8.csv')

# Read all players from the players column and convert
# to a set to remove duplicates
playersSet = set(df1["Player"])

# df2 is the new dataframe I am creating formatted for flourish
# These are the column headings for my flourish.csv file
header=[]
header.append("Player")
header.append("Decade")
header.append("URL")
for year in years:
    header.append(year)

# Now I want to populate the csv file with the player, their decade,
# their country flag URL and a load of zeroes
allPlayerData=[]
playerRow=[]
for player in playersSet:
    playerRow.append(player)
    playerIndex=df1.loc[df1["Player"]==player].index[0]
    playerRow.append(decadeFinder(df1.loc[playerIndex,"Year"]))
    # Look up our dictionary of flag URLs to add the flag
    playerRow.append(flagsDict[df1.loc[playerIndex,"Country"]])
    for i in range(len(years)):
        playerRow.append(0)
    # Add my player row list to the allPlayerData list
    # [[player1,decade,URL,0...0],[player1,decade,URL,0...0], ... ]
    allPlayerData.append(playerRow)
    # Reinitialise playerRow for the next player
    playerRow=[]

# Now we have gone through the full CSV file, we want to create a
# dataframe for our newly reformatted data
df2 = pd.DataFrame(allPlayerData, columns=header)

# Now we have a new dataframe with player name, a URL and all zeroes

# Next we go through the original dataframe df1 again
# We read a sub-dataframe for each year and complete the column of the
# new dataframe for that year.
# As we are accumulating goals year-on-year we need to make sure that
# we only add on to the previous years tally from year 2 onwards
# Boolean to detect first pass through the data
firstColumn=True

# For each year in the datafame 
for year in years:
    if firstColumn:
        pass
    else:
        # Copy the value from the previous year
        # so we can add to it if necessary
        df2[year] = df2[year-1]
    
    # Read the block of data for current year from raw data
    subdf=df1.loc[df1["Year"]==year]
    
    # Some output so we can observe progress
    print("*"*10, year, "*"*10)

    # We need to go through the subdataframe row by row so we use .iloc[] with an index
    for i in range(len(subdf)):
        #playerRow=subdf.iloc[i]
        # Get the current player
        player=subdf.iloc[i]["Player"]
        # Now locate the player in my output dataframe (the one for flourish)
        playerIndex=df2.loc[df2["Player"]==player].index[0]
        # Under the current year, I increment the players tally 
        df2.loc[playerIndex,year] += 1

    #We want this true so that all players start at zero in 1916
    # Once we have iterated through the dataframe, set it back to false
    # so that previous goals will be added year by year
    firstColumn=False

# before writing to file, sort the data by decade so that the decades
# labels appear in order in flourish
finalDf = df2.sort_values(by=['Decade'], ascending=True)
# Write the dataframe to a csv file. Note that index=false, stops the extra
# index being added to the file
finalDf.to_csv('flourish.csv', index=False)

