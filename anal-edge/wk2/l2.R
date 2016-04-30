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