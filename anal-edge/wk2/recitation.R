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

# create regression model for points and view its summary
pts_reg = lm(PTS ~ X2PA + X3PA + FTA + AST + ORB + DRB + TOV + STL + BLK, data = nba)
summary(pts_reg)

# view the points residuals
pts_reg$residuals

# create points SSE and view it
SSE = sum(pts_reg$residuals^2)
SSE

# calculate the RMSE and view it
RMSE = sqrt(SSE / nrow(nba))
RMSE

# determine avg num of pts in a season
mean(nba$PTS)

# revise points model, removing turn overs variable, and view it
pts_reg2 = lm(PTS ~ X2PA + X3PA + FTA + AST + ORB + DRB + STL + BLK, data = nba)
summary(pts_reg2)

# revise points model, removing def rebounds variable, and view it
pts_reg3 = lm(PTS ~ X2PA + X3PA + FTA + AST + ORB + STL + BLK, data = nba)
summary(pts_reg3)

# revise points model, removing blocks variable, and view it
pts_reg4 = lm(PTS ~ X2PA + X3PA + FTA + AST + ORB + STL, data = nba)
summary(pts_reg4)

# create points SSE based on latest mode and view it
SSE4 = sum(pts_reg4$residuals^2)
SSE4

# calculate the RMSE based on latest model's SSE and view it
RMSE4 = sqrt(SSE4 / nrow(nba))
RMSE4