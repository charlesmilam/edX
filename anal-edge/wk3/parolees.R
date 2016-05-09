# exercises for week 3 homework - parolees

# load the data
parole = read.csv("parole.csv")
str(parole)
summary(parole)

# determine number of parole violators
nrow(subset(parole, parole$violator == 1))

# convert unordered factors with level > 3
parole$state = as.factor(parole$state)
parole$crime = as.factor(parole$crime)
summary(parole)

# split the data into training and testing sets
# set the seed
set.seed(144)
# add the caTools library
library(caTools)
# perform the split
split = sample.split(parole$violator, SplitRatio = 0.7)
# assign the train and test sets
train = subset(parole, split == TRUE)
test = subset(parole, split = FALSE)

# build the model
mod1_log = glm(violator ~ ., data = train, family = binomial)
summary(mod1_log)

# build a specific model ???
example_parolee = c(male = 1, race = 1, age = 50, state2 = 0, state3 = 0, state4 = 0, time.served = 3, max.sentence = 12, multiple.offenses = 0, crime2 = 1, crime3 = 0, crime4 = 0, violator = 0)
example_parolee
data.frame(example_parolee)
# make prediction
examp_pred = predict(mod1_log, newdata = example_parolee, type = "response")

# make prediction on training set
test_parole_pred = predict(mod1_log, newdata = test, type = "response")
summary(test_parole_pred)

# evaluate the model against test data
table(test$violator, test_parole_pred >= 0.5)
# compute the sensitivity
27 / 78
# compute the specificity
578 / (578 + 19)
# compute the accuracy
(578 + 27) / (578 + 19 + 51 + 27)
