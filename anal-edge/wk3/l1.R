# exercises for week 3 lecture 1

# load the data and view structure
quality = read.csv("quality.csv")
str(quality)

# create table based on care
table(quality$PoorCare)

# determine baseline (this is for a classification problem)
baseline = length(quality$PoorCare[quality$PoorCare == 0]) / nrow(quality)
baseline

# load caTools
library(caTools)

# randomly split the data using caTools, to create a training and a test set
# first set the seed, so data is the same as that used in the class
set.seed(88)
# now split the data, using 75% for the training set
split = sample.split(quality$PoorCare, SplitRatio = 0.75)
# view the split
split
# create the training set
quality_train = subset(quality, split == TRUE)
# create the test set
quality_test = subset(quality, split == FALSE)

# build the logistical regression model and view it
quality_log = glm(PoorCare ~ OfficeVisits + Narcotics, data = quality_train, family = binomial)
summary(quality_log)

# create prediction against the training set
predict_train = predict(quality_log, type = "response")
summary(predict_train)

# compare prediction against actual
tapply(predict_train, quality_train$PoorCare, mean)

# create model for poor care based on combo and provider count
combi_prov_log = glm(PoorCare ~ StartedOnCombination + ProviderCount, data = quality_train, family = binomial)
summary(combi_prov_log)

# create prediction for combi_prov_log
predict_combi = predict(combi_prov_log, type = "response")
summary(predict_combi)

# create some classification tables
# 0.5 threshold
table(quality_train$PoorCare, predict_train > 0.5)
# compute sensitivity
10 / 25
# compute specificity
70 / 74
# 0.7 threshold
table(quality_train$PoorCare, predict_train > 0.7)
# compute sensitivity
8 / 25
# compute specificity
73 / 74
# 0.7 threshold
table(quality_train$PoorCare, predict_train > 0.2)
# compute sensitivity
16 / 25
# compute specificity
54 / 74

# generate ROC curves
# add library ROCR
library(ROCR)
# add a prediction
rocr_pred = prediction(predict_train, quality_train$PoorCare)
# add a performance
rocr_perf = performance(rocr_pred, "tpr", "fpr")
#plot the perf
plot(rocr_perf)
# now with colors
plot(rocr_perf, colorize = TRUE)
# and with threshold labels
plot(rocr_perf, colorize = TRUE, print.cutoffs.at = seq(0, 1, 0.1), text.adj = c(-0.2, 1.7))

# check accuracy of original model (quality_log)
# make prediction based on test data
predict_test = predict(quality_log, type = "response", newdata = quality_test)
# compute the AUC of the test set
roc_pred_test = prediction(predict_test, quality_test$PoorCare)
auc = as.numeric(performance(roc_pred_test, "auc")@y.values)
auc
