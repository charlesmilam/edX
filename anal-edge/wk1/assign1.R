# assignment 1 for week 1

# Problem 1 - Loading the Data
# load the motor vehicle theft data
mvt = read.csv("mvtWeek1.csv")

# check the structure and summary of data frame
str(mvt)
summary(mvt)

# get the max of the ID variable
max(mvt$ID)

# get the min of the Beat variable
min(mvt$Beat)

# get num of obs where Arrest is true
length(which(mvt$Arrest == TRUE))

# get num of obs where LocationDescripton is Alley
length(which(mvt$LocationDescription == "ALLEY"))

# Problem 2 - Understanding Date in R

# exaxmine first entry of Date
mvt$Date[1]

# convert Date to date object
DateConvert = as.Date(strptime(mvt$Date, "%m/%d/%y %H:%M"))
# examine summary of DateConvert
summary(DateConvert)

# add month and weekday to mvt data frame
mvt$Month = months(DateConvert)
mvt$Weekday = weekdays(DateConvert)
# replace the default Date with DateConvert variable
mvt$Date = DateConvert
# display as table to determine month with fewest thefts
table(c(mvt$Month, length(mvt$ID)))

# distplay as table to determine weekday with most thefts
table(c(mvt$Weekday, length(mvt$ID)))

# display as table to determine month with most arrests
table(mvt$Month, mvt$Arrest)

# Problem 3 - Visualiizing Crime Trends

# create histogram of Date
hist(mvt$Date, breaks = 100)

# create boxplot of Date sorted by Arrest
boxplot(mvt$Date ~ mvt$Arrest)

# create tables based on arrests
# year 2001
MVT2001 = mvt[mvt$Year == 2001,]
ArrestsMade2001 = mvt[mvt$Year == 2001 & mvt$Arrest == TRUE,]
table(ArrestsMade2001$Month)

# year 2007
MVT2007 = mvt[mvt$Year == 2007,]
ArrestsMade2007 = mvt[mvt$Year == 2007 & mvt$Arrest == TRUE,]
table(ArrestsMade2007$Month)

# year 2012
MVT2012 = mvt[mvt$Year == 2012,]
ArrestsMade2012 = mvt[mvt$Year == 2012 & mvt$Arrest == TRUE,]
table(ArrestsMade2012$Month)

# Problem 4 - Popular Locations

# sorted locations table
sort(table(mvt$LocationDescription))

# create top 5 theft locations variable
Top5 = mvt[mvt$LocationDescription == "STREET" | mvt$LocationDescription == "PARKING LOT/GARAGE(NON.RESID.)" | mvt$LocationDescription == "ALLEY" | mvt$LocationDescription == "GAS STATION" | mvt$LocationDescription == "DRIVEWAY - RESIDENTIAL",]
# check structure to determine number of obs
str(Top5)

# factor Top5 location description
Top5$LocationDescription = factor(Top5$LocationDescription)
str(Top5)
# determine location with highest arrest rate
tapply(Top5$Arrest, Top5$LocationDescription, mean)

# determine day of week with most thefts at gas stations
table(Top5$Weekday[Top5$LocationDescription == "GAS STATION"])

# determine day of the week with least thefts from residential driveways
table(Top5$Weekday[Top5$LocationDescription == "DRIVEWAY - RESIDENTIAL"])
