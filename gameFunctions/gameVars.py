from random import randint

# set up some variables for player and AI Lives
player_lives=5
computer_lives=5
total_lives=5

# choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

#set the computer variable to one of these choices (0,1or2)
computer=choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False