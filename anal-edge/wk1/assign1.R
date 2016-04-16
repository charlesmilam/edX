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
