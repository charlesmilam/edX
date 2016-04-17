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

# Problem 3 - Visualizing Stock Dynamics 1995-2005

# create line plot for Coca-Cola for given time period
plot(CocaCola$Date[301:432], CocaCola$StockPrice[301:432], type="l", col="red", ylim=c(0,210))

# add lines for the rest of the stocks
lines(ProcterGamble$Date[301:432], ProcterGamble$StockPrice[301:432], type="l", col="purple", ylim=c(0,210))
lines(IBM$Date[301:432], IBM$StockPrice[301:432], type="l", col="blue", ylim=c(0,210))
lines(GE$Date[301:432], GE$StockPrice[301:432], type="l", col="lightblue", ylim=c(0,210))
lines(Boeing$Date[301:432], Boeing$StockPrice[301:432], type="l", col="green", ylim=c(0,210))

# add ablines to aid in isolating a subset of dates
abline(v = as.Date(c("1997-09-01")), lwd = 2)
abline(v = as.Date(c("1997-11-30")), lwd = 2)

# Problem 4 - Monthly Trends

# determine the mean stock price of IBM sorted by months, and use to compare
# against the overall average stock price
tapply(IBM$StockPrice, months(IBM$Date), mean)
summary(IBM)

# determine the mean stock price for the other stocks
tapply(CocaCola$StockPrice, months(CocaCola$Date), mean)
tapply(GE$StockPrice, months(GE$Date), mean)
tapply(ProcterGamble$StockPrice, months(ProcterGamble$Date), mean)
tapply(Boeing$StockPrice, months(Boeing$Date), mean)


