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

