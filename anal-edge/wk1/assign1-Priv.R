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

# determine variables with NA values and average number of personal information
summary(limited)

# determine number of interviewees with 0 for Info.On.Internet
# and number of interviewees with 11
table(limited$Info.On.Internet)

# determine proportion of Worry.About.Info
table(limited$Worry.About.Info == 1, limited$Worry.About.Info)

# determine proportion of Anonymity
table(limited$Anonymity.Possible == 1, limited$Anonymity.Possible)

# determine proportion of Tried.Masking
table(limited$Tried.Masking.Identity == 1, limited$Tried.Masking.Identity)

# determine proportion of Privacy.Law
table(limited$Privacy.Laws.Effective)

# build histogram for ages
hist(limited$Age)

# determine overlapping points of age and info.on.internet
max(table(limited$Age, limited$Info.On.Internet))

# experiment with the jitter command
jitter(c(1, 2, 3))
jitter(c(1, 2, 3))

# determine relationship between age and info.on via plot with jiter
plot(jitter(limited$Age), jitter(limited$Info.On.Internet))

# determine average of info.on for smartphone and non smartphone users
tapply(limited$Info.On.Internet, limited$Smartphone == 1, mean)

# determine avergae of tried.masking for smartphone or non smartphone users
tapply(limited$Tried.Masking.Identity, limited$Smartphone, mean, na.rm = TRUE)
