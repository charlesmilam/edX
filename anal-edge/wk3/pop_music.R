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
