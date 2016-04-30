# exercises for lecture 2

# load the baseball data
baseball = read.csv("baseball.csv")

# view the structure of baseball
str(baseball)

# create subset of baseball, include only years before 2002
moneyball = subset(baseball, baseball$Year < 2002)

# view structure of moneyball
str(moneyball)

# create new variable for moneyball to hold run difference
moneyball$RD = moneyball$RS - moneyball$RA

# view structure of moneyball to see new variable
str(moneyball)

# create plot of run difference vs. wins
plot(moneyball$RD, moneyball$W)

# create model based on ind variable RD
wins_reg = lm(W ~ RD, data = moneyball)

# view summary of wins_reg
summary(wins_reg)

# view structure of moneyball
str(moneyball)

# create model for runs, and view its summary
runs_reg = lm(RS ~ OBP + SLG + BA, data = moneyball)
summary(runs_reg)

# revise model, removing the batting average, and view model summary
runs_reg = lm(RS ~ OBP + SLG, data = moneyball)
summary(runs_reg)

# create model for runs allowed, and view its summary
runs_allow_reg = lm(RA ~ OOBP + OSLG, data = moneyball)
summary(runs_allow_reg)

# determine runs scored and runs allowed for qq based on provided values
qq_rs = -804.63 + (2737.77 * 0.311) + (1584.91 * 0.405)
qq_ra = -837.38 + (2913.60 * 0.297) + (1514.29 * 0.370)
qq_rs
qq_ra
