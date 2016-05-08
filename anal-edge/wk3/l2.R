# exercises for lecture 2 of week 3

# load the data
framingham = read.csv("framingham.csv")
str(framingham)

# create training and test data sets
# load the caTools library
library(caTools)
# set the seed, so data is consistent with lecture
set.seed(1000)
# create the split
split = sample.split(framingham$TenYearCHD, SplitRatio = 0.65)
# and create the data sets
train = subset(framingham, split == TRUE)
test = subset(framingham, split == FALSE)

# create the model
framingham_log = glm(TenYearCHD ~ ., data = train, family = binomial)
summary(framingham_log)

# make prediction against test data
predict_fram_test = predict(framingham_log, type = "response", newdata = test)
# make confusion matrix
table(test$TenYearCHD, predict_fram_test > 0.5)
# and compute the accuracy
(1069 + 11) / (1069 + 6 + 187 + 11)

# create baseline
fram_baseline = (1069 + 6) / (1069 + 6 + 187 + 11)
fram_baseline

# compute the ROC and AU
# load the ROCR library
library(ROCR)
# make the ROC prediction
roc_pred_fram = prediction(predict_fram_test, test$TenYearCHD)
# compute the AUC
fram_auc = as.numeric(performance(roc_pred_fram, "auc")@y.values)
fram_auc

# compute sensitivity and specificity of confusion matrix at a threshold of 0.5
# 0.5 threshold
table(test$TenYearCHD, predict_fram_test > 0.5)
# compute sensitivity
11 / 198
# compute specificity
1069 / 1075
