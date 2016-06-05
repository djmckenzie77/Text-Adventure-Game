class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects")
	
	def  __str__(self):
		return self.name


class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.description = "A fist-sized rock, suitable for bludgeoning."
		self.damage = 5
		
class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.description = "A small rusty dagger."
		self.damage = 10
		

class RustySword(Weapon):
	def __init__(self):
		self.name = "Rusty Sword"
		self.description = "A slightly rusty sword with some fight left in it"
		self.damage = 20
		

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
	


def most_powerful_weapon(inventory):
	max_damage = 0
	best_weapon = None
	for item in inventory:
		try:
			if item.damage > max_damage:
				best_weapon = item
				max_damage = item.damage
		except AttributeError:
			pass
				
				
	return best_weapon
				
	
play()
