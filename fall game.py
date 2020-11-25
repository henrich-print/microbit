from microbit import *

class Player:
	def __init__(self, app_self):
		self.app_self = app_self
		self.pos = {"x":4, "y": 3}
		self.move = True

	def loop(self):
		if button_a.is_pressed() and self.move:
			self.pos["x"] -= 1
			display.scroll(self.pos["x"])
			self.move = False
		elif button_b.is_pressed() and self.move:
			self.pos["x"] += 1
			self.move = False
		else:
		    self.move = True

		lines = self.player_line(self.app_self.bg)
		self.app_self.bg = lines

	def player_line(self, line):
		line[self.pos["x"]*self.pos["y"]] = 9
		return line

class Main:
	def __init__(self):
		self.score = 0
		self.player = Player(self)
		self.bg_update()
		self.loop()

	def loop(self):
		while True:
			self.bg_update()
			self.player.loop()
			display.show(Image(5, 5, bytearray(self.bg)))

	def bg_update(self):
		self.bg = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

main = Main()