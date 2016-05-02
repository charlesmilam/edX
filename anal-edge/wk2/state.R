# week 2 problem set 4 - state data

# load the data
data(state)
state_data = cbind(data.frame(state.x77), state.abb, state.area, state.center, state.division, state.name, state.region )

# view structure of data
str(state_data)

# plot the state's centers
plot(state_data$x, state_data$y)

# determine region with highest avg HS graduation
tapply(state_data$HS.Grad, state_data$state.region, mean)

# create boxplot of murder rate by region
region_murder = tapply(state_data$Murder, state_data$state.region, median)
region_murder
boxplot(region_murder)
boxplot(state_data$Murder, data = state_data)

# determine outlier state for NE region for murder rate
ne_region = state_data[state_data$state.region == "Northeast",]
factor(ne_region$state.name)
factor(ne_region$state.abb)
plot(ne_region$state.abb, ne_region$Murder)
table(ne_region$state.abb, ne_region$Murder)

# build model for life expectancy
life_exp = lm(Life.Exp ~ Population + Income + Illiteracy + Murder + HS.Grad + Frost + Area, data = state_data)
summary(life_exp)

# plot income vs. life expectancy
plot(state_data$Income, state_data$Life.Exp)

# revise model to find simplest but most accurae
life_exp1 = lm(Life.Exp ~ Population + Income + Illiteracy + Murder + HS.Grad + Frost, data = state_data)
summary(life_exp)
summary(life_exp1)

life_exp2 = lm(Life.Exp ~ Population + Income + Murder + HS.Grad + Frost, data = state_data)
summary(life_exp)
summary(life_exp2)

life_exp3 = lm(Life.Exp ~ Population + Murder + HS.Grad + Frost, data = state_data)
summary(life_exp)
summary(life_exp3)

step(life_exp)

# make a prediction, lowest life expectancy
sort(predict(life_exp3))
# the actual
state_data$state.name[which.min(state_data$Life.Exp)]

# make a prediction, highest life expectancy
sort(predict(life_exp3), decreasing = TRUE)
# the actual
state_data$state.name[which.max(state_data$Life.Exp)]

# view the residuals
sort(life_exp3$residuals)
