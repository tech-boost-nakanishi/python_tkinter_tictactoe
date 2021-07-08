import tkinter as tk

class GameFrame(tk.Frame):

	WIDTH = 500
	HEIGHT = 600

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		tk.Label(self, text="ゲームフレーム", font=('Helvetica', 18, "bold")).pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT