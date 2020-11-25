from microbit import *
from time import sleep
import random

class Player:
	def __init__(self, app_self):
		self.app_self = app_self
		self.pos = {"x":4, "y": 3}
		self.skin = 9
		self.score = 0

	def loop(self):
		if button_a.is_pressed():
			self.pos["x"] -= 1
			sleep(.25)

		elif button_b.is_pressed():
			self.pos["x"] += 1
			sleep(.25)

		if self.pos["x"]-2*self.pos["y"] == self.app_self.coin.pos["x"]-2*self.app_self.coin.pos["y"]:
			self.score += 1
			self.app_self.coin.get_pos()
			self.app_self.timer.pos["time"] = 5

		self.build()
	
	def build(self):
		self.app_self.display[self.pos["x"]-2*self.pos["y"]] = self.skin

class Timer:
	def __init__(self, app_self):
		self.app_self = app_self
		self.pos = {"x": 1, "time": 5, "clock": 200}
		self.skin = 1

	def loop(self):
		if self.pos["time"] == 0:
			self.app_self.quit()
		else:
			self.build()

			if self.pos["clock"] == 0:
				self.pos["time"] -= 1
				self.pos["clock"] = 200

			self.pos["clock"] -= 1

	def build(self):
		for i in range(self.pos["time"]):
			self.app_self.display[i] = self.skin

class Coin:
	def __init__(self, app_self):
		self.app_self = app_self
		self.get_pos()
		self.skin = 5

	def get_pos(self):
		self.pos = {"x": random.randint(1, 5), "y": random.randint(1, 5)}

	def loop(self):
		self.build()

	def build(self):
		self.app_self.display[self.pos["x"]-2*self.pos["y"]] = self.skin

class Main:
	def __init__(self):
		self.player = Player(self)
		self.timer = Timer(self)
		self.coin = Coin(self)

		self.display = [i-i for i in range(25)]
		self.run = True
		
		self.main()

	def main(self):
		while self.run:
			self.player.loop()
			self.timer.loop()
			self.coin.loop()
			
			self.display_update()

	def display_update(self):
		display.show(Image(5, 5, bytearray(self.display)))
		self.display = [i-i for i in range(25)]

	def quit(self):
		self.run = False
		display.scroll(self.player.score)
		display.clear()

while True:
	main = Main()
