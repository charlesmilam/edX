# week 2 problem set 2 - reading test scores

# load the data for the training and test sets
pisa_train = read.csv("pisa2009train.csv")
pisa_test = read.csv("pisa2009test.csv")

# check the structure of both
str(pisa_train)
str(pisa_test)

# determine average reading test score for males
tapply(pisa_train$readingScore, pisa_train$male, mean)

# view summary of training set to aid in determining those with NAs
summary(pisa_train)

# remove obs with missing data from training and test sets
pisa_train = na.omit(pisa_train)
pisa_test = na.omit(pisa_test)

# view structure of cleaned up sets
str(pisa_train)
str(pisa_test)

# set the ref level for the factor race to white
pisa_train$raceeth = relevel(pisa_train$raceeth, "White")
pisa_test$raceeth = relevel(pisa_test$raceeth, "White")

# create model on readingScore using all remaining variables
score_reg = lm(readingScore ~ ., data = pisa_train)
# view the summary of the model
summary(score_reg)

# first calculate the SSE of the model
SSE = sum(score_reg$residuals^2)
SSE
# then calculate the RMSE and view it
RMSE = sqrt(SSE / nrow(pisa_train))
RMSE

# create predictions for students and view summary
score_predict = predict(score_reg, newdata = pisa_test)
summary(score_predict)

# calculate the SSE and RMSE of the test set
# calculate SSE
SSE = sum((score_predict - pisa_test$readingScore)^2)
SSE
# calculate SST
SST = sum((mean(pisa_train$readingScore) - pisa_test$readingScore)^2)
SST
# calculate r squared for test data, and view it
r2 = 1 - SSE / SST
r2

# calculate the RMSE for test data
RMSE = sqrt(SSE / nrow(pisa_test))
RMSE

# calculate baseline mean of training data
mean(pisa_train$readingScore) 
