# Intro R Lecture
WHO = read.csv("WHO.csv")
table(WHO$Region)
tapply(WHO$Over60, WHO$Region, mean)
