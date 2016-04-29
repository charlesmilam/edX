# exercises for lecture 1

# load the wine data
wine = read.csv("wine.csv")

# check the structure of the wine data frame
str(wine)

# check the summary info
summary(wine)

# create linear regression model for AGST
model1 = lm(Price ~ AGST, data = wine)

# check summary of model1
summary(model1)

# view residuals of model1
model1$residuals

# compute the SSE and view it
SSE = sum(model1$residuals^2)
SSE

# create new model with additional ind variables
model2 = lm(Price ~ AGST + HarvestRain, data = wine)

# view summary of model2
summary(model2)

# recompute the SSE and view it
SSE = sum(model2$residuals^2)
SSE

# create new model using all available ind variables
model3 = lm(Price ~ WinterRain + AGST + HarvestRain + Age + FrancePop, data = wine)

# view sumary of model3
summary(model3)

# and recompute SSE one more time and view it
SSE = sum(model3$residuals^2)
SSE