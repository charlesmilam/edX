# exercises for week 3 lecture 1

# load the data and view structure
quality = read.csv("quality.csv")
str(quality)

# create table based on care
table(quality$PoorCare)

# determine baseline (this is for a classification problem)
baseline = length(quality$PoorCare[quality$PoorCare == 0]) / nrow(quality)
baseline

# load caTools
library(caTools)

# randomly split the data using caTools, to create a training and a test set
# first set the seed, so data is the same as that used in the class
set.seed(88)
# now split the data, using 75% for the training set
split = sample.split(quality$PoorCare, SplitRatio = 0.75)
# view the split
split
# create the training set
quality_train = subset(quality, split == TRUE)
# create the test set
quality_test = subset(quality, split == FALSE)

# build the logistical regression model and view it
quality_log = glm(PoorCare ~ OfficeVisits + Narcotics, data = quality_train, family = binomial)
summary(quality_log)

# create prediction against the training set
predict_train = predict(quality_log, type = "response")
summary(predict_train)

# compare prediction against actual
tapply(predict_train, quality_train$PoorCare, mean)
