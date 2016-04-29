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

# create model for use in quick questions
price_rain_model = lm(Price ~ HarvestRain + WinterRain, data = wine)

# view summary of price rain model
summary(price_rain_model)

# create model not making use of FrancePop
model4 = lm(Price ~ WinterRain + AGST + HarvestRain + Age, data = wine)

# view summary of model4
summary(model4)

# view summary of price_rain_model again for use in quick question
summary(price_rain_model)

# view correlation between winter rain and price
cor(wine$WinterRain, wine$Price)

# view correlation between age and france pop
cor(wine$Age, wine$FrancePop)

# view all correlations
cor(wine)

# create new model not making use of age and france pop
model5 = lm(Price ~ AGST + WinterRain + HarvestRain, data = wine)

# view summary of model5
summary(model5)

# determine correlation between winter rain and harvest rain for use with 
# quick question
cor(wine$WinterRain, wine$HarvestRain)
