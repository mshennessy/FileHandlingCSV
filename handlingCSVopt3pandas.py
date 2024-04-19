# CSV handling option 3 - using pandas

# For data analysis
import pandas as pd

# This is a not on your reference guide, but "with open()"
# is a handier way to open a file, as it is
# automatically closed after (no need for file.close()

# Read from the csv file using pandas. Pandas returns a data structure
# called a dataframe df
df = pd.read_csv('oscar.csv')
#Total up the values in each column - no need for a for loop!
sumAwards = df["NumberOfAwards"].sum()
sumNoms = df["NumberOfNominations"].sum()

print(sumAwards,sumNoms)
# Overall average chance is
probWin = sumAwards/sumNoms
print("Chance of winning",probWin)

# For your analysis, you may need to isolate some specific data
# When there are multiple values you are isolating you
# must use & between them (not "and") Its a pandas thing
# Look for films that got more than 1 nomination in 2022
subdf=df.loc[(df["Year"]==2022) & (df["NumberOfNominations"]>1)]
print("subdf:\n", subdf)
#Total up the values in each column - no need for a for loop!
sumAwards = subdf["NumberOfAwards"].sum()
sumNoms = subdf["NumberOfNominations"].sum()

print(sumAwards,sumNoms)
# Overall average chance is
probWin = sumAwards/sumNoms
print("Chance of winning if you got more than 1 nomination in 2022",probWin)



