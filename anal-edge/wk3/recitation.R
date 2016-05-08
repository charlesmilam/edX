# exercises for week 3 recitation

# load the data
polling = read.csv("PollingData.csv")
str(polling)

# analyze the year variable in a table
table(polling$Year)

# view summary of polling data
summary(polling)

# multiple imputation
# add the mice library
library(mice)
# create a simplified data frame for use with the multiple imputation
simple = polling[c("Rasmussen", "SurveyUSA", "PropR", "DiffCount")]
summary(simple)
# set the seed
set.seed(144)
# create the new data frame based on multiple imputation
imputed = complete(mice(simple))
summary(imputed)
# use the provided imputed polling data frame, because of randomness in the multiple imputation
polling_imputed = read.csv("PollingData_Imputed.csv")
# add in the imputed variables to the base polling data frame.
polling$Rasmussen = polling_imputed$Rasmussen
polling$SurveyUSA = polling_imputed$SurveyUSA
