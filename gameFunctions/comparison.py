from gameFunctions import gameVars


def compareweapons(gameVarscomputer,gameVarsplayer):
	if gameVars.computer == gameVars.player:
		print("------------------------------")
		print("Result:")
		print ("tie! no one wins, play again")
		print("------------------------------")
	elif gameVars.player.lower() =="quit":
		exit()
	elif gameVars.player.lower() == "rock":
		if gameVars.computer == "paper":
			print("-----------------------------------")
			print("Reason of win/lose:")
			print(gameVars.computer, "covers", gameVars.player,"\n")
			print("Result:")
			print("You LOSE!!!")
			print("-----------------------------------")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("-----------------------------------")
			print("Reason of win/lose:")
			print(gameVars.player, "smashes through", gameVars.computer, "\n")
			print("Result:")
			print("You WIN!!!!!!!!!!!!!")
			print("-----------------------------------")
			gameVars.computer_lives = gameVars.computer_lives - 1
	elif gameVars.player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("-----------------------------------")
			print("Reason of win/lose:")
			print(gameVars.computer, "cuts", gameVars.player,"\n")
			print("Result:")
			print("You LOSE!!")
			print("-----------------------------------")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("-----------------------------------")
			print("Reason of win/lose:")
			print(gameVars.player, "covers", gameVars.computer, "\n")
			print("Result:")
			print("You WIN!!!")
			print("-----------------------------------")
			gameVars.computer_lives = gameVars.computer_lives - 1
	elif gameVars.player.lower() == "scissors":
		if gameVars.computer == "rock":
			print("-----------------------------------")
			print("Reason of win/lose:")
			print(gameVars.computer, "smashes", gameVars.player,"\n")
			print("Result")
			print("You LOSE !!")
			print("-----------------------------------")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("-----------------------------------")
			print("Reason of win/lose")
			print(gameVars.player, "cuts", gameVars.computer, "\n")
			print("Result:")
			print("You WIN!!!!!!!")
			print("-----------------------------------")
			gameVars.computer_lives = gameVars.computer_lives - 1
			
	else:
		print("ERROR -Could not decide winner/loser")
		print("That's not a valid choice, try again")