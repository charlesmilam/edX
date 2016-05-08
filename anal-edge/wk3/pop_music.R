# exercises for week 3 homework - popular music

# load the data
songs = read.csv("songs.csv")
str(songs)

# determine the number of songs in 2010
nrow(subset(songs, songs$year == 2010))

# determine the number of songs by Michael Jackson
nrow(subset(songs, songs$artistname == "Michael Jackson"))

# determine top 10 Michael Jackson songs
subset(songs$songtitle, songs$artistname == "Michael Jackson" & songs$Top10 == 1)

# determine time signature
table(songs$timesignature)

# determine song with highest tempo
max_tempo = max(songs$tempo)
songs$songtitle[songs$tempo == max_tempo]

# split the songs data frame into a training and testing set
songs_train = subset(songs, songs$year <= 2009)
songs_test = subset(songs, songs$year > 2009)

# build the model
# first, remove un-needed variables from the train and test sets
# create a vector for the variables we are not wanting to use
nonvars = c("year", "songtitle", "artistname", "songID", "artistID")
# use nonvars to remove those variables from our training set
songs_train = songs_train[, !(names(songs_train) %in% nonvars)]
songs_test = songs_test[, !(names(songs_test) %in% nonvars)]
# the model
songs_log1 = glm(Top10 ~ ., data = songs_train, family = binomial)
summary(songs_log1)

# determine the correlation between loudness and energy
cor(songs_train$loudness, songs_train$energy)

# create new model not using loudness
songs_log2 = glm(Top10 ~ . - loudness, data = songs_train, family = binomial)
summary(songs_log2)

# create new model not using energy
songs_log3 = glm(Top10 ~ . - energy, data = songs_train, family = binomial)
summary(songs_log3)

# make a prediction using the test set
predict_songs_test = predict(songs_log3, newdata = songs_test, type = "response")
table(songs_test$Top10, predict_songs_test >= 0.45)
# determine the accuracy
(309 + 19) / (309 + 5 + 40 + 19)

# determine the baseline
songs_baseline = length(songs_test$Top10[songs_test$Top10 == 0]) / nrow(songs_test)
songs_baseline

# determine the sensitivity and specificity
table(songs_test$Top10, predict_songs_test >= 0.45)
# compute sensitivity
19 / 59
# compute specificity
309 / 314

