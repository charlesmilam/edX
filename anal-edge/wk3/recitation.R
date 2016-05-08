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

# create training and testing data sets
train = subset(polling, Year == 2004 | Year == 2008)
test = subset(polling, Year == 2012)

# view dependent variable Republican from the training set
table(train$Republican)

# create a smart baseline using data from the Rasmussen variable
poll_baseline = sign(train$Rasmussen)

# view this baseline as a table
table(poll_baseline)
# and compare it to the actual
table(train$Republican, poll_baseline)

# determine the corellation between the independent variables and the dependent variable
cor(train[c("Rasmussen", "SurveyUSA", "PropR", "DiffCount", "Republican")])

# create a model based on the highly correlated PropR
mod1 = glm(Republican ~ PropR, data = train, family = binomial)
summary(mod1)
# analyze the model
# create a prediction
pred1 = predict(mod1, type = "response")
table(train$Republican, pred1 >= 0.5)

# create a new model based on two variables
mod2 = glm(Republican ~ SurveyUSA + DiffCount, data = train, family = binomial)
summary(mod2)
# analyze the model
# create a prediction
pred2 = predict(mod2, type = "response")
table(train$Republican, pred2 >= 0.5)

# use second model against testing data
# first view testing data against the test baseline
poll_test_baseline = sign(test$Rasmussen)
table(test$Republican, poll_test_baseline)
# make prediction on test data using the model
test_pred = predict(mod2, newdata = test, type = "response")
table(test$Republican, test_pred >= 0.5)
# find the mistake that the prediction made
subset(test, test_pred >= 0.5 & Republican == 0)

