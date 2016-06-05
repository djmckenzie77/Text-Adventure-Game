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
		

