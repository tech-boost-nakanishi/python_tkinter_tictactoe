import tkinter as tk

class SettingFrameClass(tk.Frame):

	WIDTH = 500
	HEIGHT = 300

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		tk.Label(self, text="設定フレーム", font=('Helvetica', 18, "bold")).pack()
		# self.pack()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

# if __name__ == '__main__':
# 	sfc = SettingFrameClass()