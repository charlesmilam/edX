# Assignment 1 optional problem set

# data setup
poll = read.csv("AnonymityPoll.csv")
str(poll)

# determine smartphone usage, include non-answers
table(poll$Smartphone, useNA = "ifany")

# determine regional information
table(poll$State, poll$Region)

# determine smartphone and internet usage
table(poll$Smartphone, poll$Internet.Use, useNA = "ifany")

# create a dataframe users who used either the internet or a smartphone
limited = subset(poll, poll$Internet.Use == 1 | poll$Smartphone == 1)
# limited = poll[complete.cases(poll[, 1:2]),]
str(limited)

# determine variables with NA values
summary(limited)
