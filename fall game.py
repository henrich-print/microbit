from microbit import *
from time import sleep

class Player:
	def __init__(self, app_self):
		self.app_self = app_self
		self.pos = {"x":4, "y": 3, "width": 1, "height": 1}
		self.skin = 9

	def loop(self):
		if button_a.is_pressed():
			self.pos["x"] -= 1
			sleep(.5)

		elif button_b.is_pressed():
			self.pos["x"] += 1
			sleep(.5)
		self.build()
	
	def build(self):
       		self.app_self.display[self.pos["x"]*self.pos["y"]] = self.skin

class Wall:
    def __init__(self, app_self):
        self.app_self = app_self
        self.app_self.walls.append(self)
        self.pos = {"x": 2, "y": 3, "width": 2, "height": 2}
        
    def loop(self):
        self.build()
        
    def build(self):
        self.app_self.display[self.pos["x"]*self.pos["y"]] = self.skin
        

class Main:
	def __init__(self):
		self.player = Player(self)
		self.walls = []
		self.run = True
		
		self.main()

	def main(self):
		while self.run:
			self.player.loop()
			
			for wall in self.walls:
			    wall.loop()
			
			self.display_update()

	def display_update(self):
		self.display = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		display.show(Image(5, 5, bytearray(self.display)))

main = Main()
