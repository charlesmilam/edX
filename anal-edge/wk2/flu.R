# week 2 problem set 3 - flu epidemics

# load the data 
flu_train = read.csv("FluTrain.csv")

# view summary and structure of flu data
str(flu_train)
summary(flu_train)

# get week with max queries and ILI 
flu_train$Week[flu_train$ILI == 7.6189]
flu_train$Week[flu_train$Queries == 1.00]

# generate histogram of ILI values
hist(flu_train$ILI)
# generate histogram of Queries values
hist(flu_train$Queries)

# plot the log of ILI vs Queries
plot(log(flu_train$ILI), flu_train$Queries)

# create model of flu trends
flu_trend1 = lm(log(ILI) ~ Queries, data = flu_train)
summary(flu_trend1)

# determine the correlation between variables
qry_ili_cor = cor(flu_train$Queries, log(flu_train$ILI))
qry_ili_cor

# make some calcs on the correlation
qry_ili_cor^2
log(1/qry_ili_cor)
exp(-0.5 * qry_ili_cor)

# load the test data
flu_test = read.csv("FluTest.csv")

# create prediction on test data
test_pred1 = exp(predict(flu_trend1, newdata = flu_test))

# get the estimate for a specific date
week_est = test_pred1[which(flu_test$Week == "2012-03-11 - 2012-03-17")]
# get the observed week
week_obs = flu_test[which(flu_test$Week == "2012-03-11 - 2012-03-17"),][2]

# determine the relative error between the prediction and the observed
(week_obs - week_est) / week_obs

# calculate the SSE and RMSE of the test set
# calculate SSE
SSE = sum((test_pred1 - flu_test$ILI)^2)
SSE
# calculate SST
SST = sum((mean(flu_train$ILI) - flu_test$ILI)^2)
SST
# calculate r squared for test data, and view it
r2 = 1 - SSE / SST
r2

# calculate the RMSE for test data
RMSE = sqrt(SSE / nrow(flu_test))
RMSE