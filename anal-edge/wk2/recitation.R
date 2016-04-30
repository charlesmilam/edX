# exercises for recitation

# import the training data, view its structure and summary
nba = read.csv("NBA_train.csv")
str(nba)
summary(nba)

# view table to determine number of wins needed to make playoffs
table(nba$W, nba$Playoffs)

# create variable to hold points difference
nba$pts_diff = nba$PTS - nba$oppPTS

# create scatter plot of pts diff vs. wins
plot(nba$pts_diff, nba$W)

# create regression model for wins and view its summary
wins_model = lm(W ~ pts_diff, data = nba)
summary(wins_model)
