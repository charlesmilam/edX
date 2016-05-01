# exercises for week 2 homework, problem set 1

# load the provided climate change data
climate = read.csv("climate_change.csv")

# create a trainging set of the data
climate_train = climate[climate$Year < 2007, ]
# and a test set of the remaining years
climate_test = climate[climate$Year >= 2007, ]

# view structure and summary of climate train and test
str(climate_train)
summary(climate_train)
str(climate_test)
summary(climate_test)
