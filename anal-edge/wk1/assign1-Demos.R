# Assignment 1 of week 1 - Demographics

# data setup
CPS = read.csv("CPSData.csv")
MetroCodes = read.csv("MetroAreaCodes.csv")
CountryCodes = read.csv("CountryCodes.csv")

# Problem 1 - Loading and Summarizing the Dataset
summary(CPS)
str(CPS)

# table of states sorted
sort(table(CPS$State))

# determine proportion of US citizens
(length(which(CPS$Citizenship == "Citizen, Native")) + length(which(CPS$Citizenship == "Citizen, Naturalized"))) / length(CPS$Citizenship)

# determine races that identify as of Hispanic ethnicity
Hispanics = CPS$Race[CPS$Hispanic == 1]
table(Hispanics)
