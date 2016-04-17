# Assignment 1 Stocks Data

# set up data
# create data frames from provided data files
IBM = read.csv("IBMStock.csv")
GE = read.csv("GEStock.csv")
ProcterGamble = read.csv("ProcterGambleStock.csv")
CocaCola = read.csv("CocaColaStock.csv")
Boeing = read.csv("BoeingStock.csv")

# convert dates to Date objects
IBM$Date = as.Date(IBM$Date, "%m/%d/%y")
GE$Date = as.Date(GE$Date, "%m/%d/%y")
CocaCola$Date = as.Date(CocaCola$Date, "%m/%d/%y")
ProcterGamble$Date = as.Date(ProcterGamble$Date, "%m/%d/%y")
Boeing$Date = as.Date(Boeing$Date, "%m/%d/%y")

# Problem 1 - Summary Statistics

# view structure of data frames to determine the number of obs
str(IBM)
str(GE)
str(CocaCola)
str(ProcterGamble)
str(Boeing)

# determine the earlist and latest year listed in the dataets
# as well as mean, min, max, and median of the various stocks
summary(IBM)
summary(GE)
summary(CocaCola)
summary(ProcterGamble)
summary(Boeing)

# determine standard deviaion of Procter & Gamble
sd(ProcterGamble$StockPrice)

# Problem 2 - Visualizing Stock Dynamics

# line plot for Coca-Cola stock price ove time
plot(CocaCola$Date, CocaCola$StockPrice, xlab = "Date", ylab = "Stock Price", main = "Stock Prices Over Time", type = "l", col = "red")

# add lines for Procter & Gamble
lines(ProcterGamble$Date, ProcterGamble$StockPrice, col = "blue")

# add abline to make question answering easier
abline(v = as.Date(c("1983-01-01")), lwd = 2)
