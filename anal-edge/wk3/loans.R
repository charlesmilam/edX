# exercises for week 3 homework - loan repayment

# load the data
loans = read.csv("loans.csv")
str(loans)
summary(loans)

# what propotion of loans were not paid in full
not_paid = subset(loans, loans$not.fully.paid == 1)
nrow(not_paid) / nrow(loans)

# load provided multiple imputation data so that it matches lecture exerciese
loans_imputed = read.csv("loans_imputed.csv")

# split the data into training and test sets
# set the seed
set.seed(144)
# do the split
split = sample.split(loans_imputed$not.fully.paid, SplitRatio = 0.7)
# and assign the data sets
loans_train = subset(loans_imputed, split == TRUE)
loans_test = subset(loans_imputed, split == FALSE)

# create the model
mod1_loans_log = glm(not.fully.paid ~ ., data = loans_train, family = binomial)
summary(mod1_loans_log)
