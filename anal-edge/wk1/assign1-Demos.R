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

# Problem 2 - Evaluating Missing Values

# determine columns with NAs
summary(CPS)

# determine if patern exists for NAs
table(CPS$Region, is.na(CPS$Married))
table(CPS$Sex, is.na(CPS$Married))
table(CPS$Age, is.na(CPS$Married))
table(CPS$Citizenship, is.na(CPS$Married))

# determine states with all interviewees living in a non-metropolitan area and
# vice versa
table(CPS$State, is.na(CPS$MetroAreaCode))

# determine region which has largest proportion of interviewees living in non-metro areas
prop.table(CPS$Region, is.na(CPS$MetroAreaCode))

# determine state proportions for metro/non-metro interviewees
tapply(c(is.na(CPS$MetroAreaCode)), CPS$State,  mean)

# Problem 3 - Integrating Metropolitan Area Data

# determine number of obs for Metro Area Codes and Country Codes
str(MetroCodes)
str(CountryCodes)

# intergrate metro area data into CPS
CPS = merge(CPS, MetroCodes, by.x="MetroAreaCode", by.y="Code", all.x=TRUE)
summary(CPS)
str(CPS)

# determine the number of interviewees with missing MetroArea data
table(CPS$MetroArea, useNA = "ifany")

# determine which metro area has the largest num of interviewees
# from a particular set of 4 areas
ABBS = CPS[CPS$MetroArea == "Atlanta-Sandy Springs-Marietta, GA" | CPS$MetroArea == "Baltimore-Towson, MD" | CPS$MetroArea == "Boston-Cambridge-Quincy, MA-NH" | CPS$MetroArea == "San Francisco-Oakland-Fremont, CA",]
ABBS$MetroArea = factor(ABBS$MetroArea)
table(ABBS$MetroArea)

# determine metro area with highest proportion of Hispanic ethnicity
sort(tapply(CPS$Hispanic, CPS$MetroArea, mean))

# determine number of metro areas with race Asian > 20%
sort(tapply(CPS$Race == "Asian", CPS$MetroArea, mean))

# determine metro area with smallest proportion with no high school degree
sort(tapply(CPS$Education == "No high school diploma", CPS$MetroArea, mean, na.rm = TRUE))

