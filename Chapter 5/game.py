def play():
	print("Escape from Cave Terror!")
	action_input = get_player_command()
	if action_input == 'n' or action_input == 'N':
		print("Go North!")
	elif action_input == 's':
		print("Go South!")
	elif action_input == 'e':
		print("Go East!")
	elif action_input == 'w':
		print("Go West!")
	else:
		print("Invalid action!")
		
		
def get_player_command():
	return input('Action: ')
	
	
play()
