import tkinter as tk
import main

class MenuFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 500
		self.HEIGHT = 300
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		self.setController(controller)

		global canvas
		canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT)
		canvas.pack()

		self.paint()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getController(self):
		return self.controller

	def setController(self, con):
		self.controller = con

	def mouseEnter(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['gamestart', 'gamestarttext', 'setting', 'settingtext', 'gamefinish', 'gamefinishtext']:
			event.widget.itemconfig(str(tag).replace('text', ''), fill = 'cyan')

	def repaint(self, event):
		canvas.delete('all')
		self.paint()

	def mousePressed(self, event):
		tag = event.widget.gettags('current')[0]

		if tag in ['gamestart', 'gamestarttext']:
			main.show_frame('ゲームフレーム')

		elif tag in ['setting', 'settingtext']:
			main.show_frame('設定フレーム')

		elif tag in ['gamefinish', 'gamefinishtext']:
			self.getController().quit()

	def paint(self):
		# 背景を設定
		canvas.create_rectangle(0, 0, self.WIDTH, self.HEIGHT, fill = 'black')

		canvas.create_text(250, 50, fill = 'white', text = 'メインメニュー', font = ('Arial', 30))

		# ゲーム開始メニュー
		canvas.create_oval(self.WIDTH / 2 - 90, 90, self.WIDTH / 2 - 60 + 150, 135, fill = 'white', tags = 'gamestart')
		canvas.create_text(250, 112, fill = 'black', text = 'ゲーム開始', font = ('Arial', 20), tags = 'gamestarttext')

		# 設定画面メニュー
		canvas.create_oval(self.WIDTH / 2 - 90, 150, self.WIDTH / 2 - 60 + 150, 195, fill = 'white', tags = 'setting')
		canvas.create_text(250, 172, fill = 'black', text = '設定画面', font = ('Arial', 20), tags = 'settingtext')

		# ゲーム終了メニュー
		canvas.create_oval(self.WIDTH / 2 - 90, 210, self.WIDTH / 2 - 60 + 150, 255, fill = 'white', tags = 'gamefinish')
		canvas.create_text(250, 232, fill = 'black', text = 'ゲーム終了', font = ('Arial', 20), tags = 'gamefinishtext')

		# マウスイベントを設定
		canvas.tag_bind('current', '<Enter>', self.mouseEnter)
		canvas.tag_bind('current', '<Leave>', self.repaint)
		canvas.tag_bind('current', '<ButtonPress-1>', self.mousePressed)