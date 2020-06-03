# War
War Card Game - number of turns per game analysis

Plays the card game war x number of times and outputs the number of turns it takes for a win. 

In the .xls spreadsheet I plotted the number of turns for a win for 1000 games. The histogram seems to take a Poisson distribution.

The major assumption here is that the cards that are won on each turn are randomly assigned to the back of the deck. (Whenever I play with my spouse I usually lay down a card first, but assuming we did that all the time led to some infinite looping behaviour here)
