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

# build model for Temp
temp_reg = lm(Temp ~ MEI + CO2 + CH4 + N2O + CFC.11 + CFC.12 + TSI + Aerosols, data = climate_train)
# view summary of model
summary(temp_reg)

# determination of the correlation of N2O with other variables
cor(climate_train, climate_train$N2O)

# determine the correlation of CFC.11 to other variables
cor(climate_train, climate_train$CFC.11)

# create model based around N2O and non-correlated variables
n2o_reg = lm(Temp ~ MEI + TSI + Aerosols + N2O, data = climate_train)
# and view its summary
summary(n2o_reg)

# use step function to create a new model
temp_step_reg = step(temp_reg)
# and view the summary
summary(temp_step_reg)

# get prediction on test data based on step model
temp_predict = predict(temp_step_reg, newdata = climate_test)
summary(temp_predict)

# calculate the r squared for the test data
# calculate new SSE
SSE = sum((temp_predict - climate_test$Temp)^2)
# calculate SST
SST = sum((mean(climate_train$Temp) - climate_test$Temp)^2)
# calculate r squared for test data, and view it
r2 = 1 - SSE / SST
r2

