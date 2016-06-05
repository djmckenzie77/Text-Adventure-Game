class Rock:
	def __init__(self):
		self.name = "Rock"
		self.description = "A fist-sized rock, suitable for bludgeoning."
		self.damage = 5
		
	def __str__(self):
		return self.name
		
class Dagger:
	def __init__(self):
		self.name = "Dagger"
		self.description = "A small rusty dagger."
		self.damage = 10
		
	def __str__(self):
		return. self.name


class RustySword:
	def __init__(self):
		self.name = "Rusty Sword"
		self.description = "A slightly rusty sword with some fight left in it"
		self.damage = 20
		
	def __str__(self):
		return self.name


def play():
	inventory = [Dagger(), 'Gold(5)', 'Crusty Bread']
	print("Escape from Cave Terror!")
	while True:
		action_input = get_player_command()
		if action_input in ['n', 'N']:
			print("Go North!")
		elif action_input in ['s', 'S']:
			print("Go South!")
		elif action_input in ['e', 'E']:
			print("Go East!")
		elif action_input in ['w', 'W']:
			print("Go West!")
		elif action_input in ['i', 'I']:
			print("Inventory:")
			for item in inventory:
				print('* ' + str(item))
		else:
			print("Invalid action!")
		
		
def get_player_command():
	return input('Action: ')
	
	
play()
