import tkinter as tk
import main
from decimal import Decimal, ROUND_HALF_UP
import time
import random
import threading

class GameFrame(tk.Frame):

	WIDTH = 500
	HEIGHT = 600
	masucount = 3
	masuwidth = masuheight = int(Decimal(str(WIDTH / masucount)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
	bgcolor = 'lightgray'
	BLANK = 0
	USER = 1
	COMPUTER = 2
	turnnum = BLANK
	board = []
	global mx, my
	mx = my = -1
	isPut = False

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)
		
		global canvas
		canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT)
		canvas.pack()

		self.paint()

		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('メニューフレーム')).place(x = 20, y = 505)
		tk.Button(self, text = '最初から', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('ゲームフレーム')).place(x = 20, y = 535)
		tk.Button(self, text = '設定画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('設定フレーム')).place(x = 20, y = 565)

		# ボードリストの初期化
		self.board = [[self.BLANK]*self.masucount for i in range(self.masucount)]

		import settingFrame
		settingframe = settingFrame.SettingFrame(main.container, main.root)
		self.attackvalue = settingframe.getATTACKVALUE()
		self.xorovalue = settingframe.getXOROVALUE()
		if self.attackvalue == 0:
			self.turnnum = self.USER
		else:
			self.turnnum = self.COMPUTER

		thread1 = threading.Thread(target=self.start)
		thread1.setDaemon(True)
		thread1.start()

	def start(self):
		while True:
			# ユーザーのターン
			if self.turnnum == self.USER:
				print('ユーザー')
				while self.isPut == False:
					pass
				self.isPut = False

			# コンピューターのターン
			elif self.turnnum == self.COMPUTER:
				time.sleep(0.5)
				print('コンピューター')
				while True:
					rx = random.randint(0, self.masucount - 1)
					ry = random.randint(0, self.masucount - 1)
					if self.board[rx][ry] == self.BLANK:
						self.board[rx][ry] = self.COMPUTER
						break
				self.turnnum = self.USER

			# 再描画
			self.repaint()

			# 勝敗のチェック

		thread1.join()

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getX(self, mx):
		for i in range(self.masucount):
			if mx >= i * self.masuwidth and mx <= i * self.masuwidth + self.masuwidth:
				return i

	def getY(self, my):
		for i in range(self.masucount):
			if my >= i * self.masuheight and my <= i * self.masuheight + self.masuheight:
				return i

	def repaint(self, event = None):
		global mx, my
		self.mx = self.my = -1
		canvas.delete('turntext')
		# どちらのターンか表示
		turnstr = ''
		if self.turnnum == self.USER:
			turnstr = 'あなたの番です'
		else:
			turnstr = 'コンピューターの番です'
		canvas.create_text(300, 550, fill = 'black', text = turnstr, font = ('Arial', 20), tags = 'turntext')

		# マークの表示
		for cy in range(len(self.board)):
			for cx in range(len(self.board[cy])):
				if self.board[cx][cy] == self.USER:
					if self.xorovalue == 0:
						self.drawO(cx, cy)
					else:
						self.drawX(cx, cy)
				elif self.board[cx][cy] == self.COMPUTER:
					if self.xorovalue == 0:
						self.drawX(cx, cy)
					else:
						self.drawO(cx, cy)

	def drawX(self, x, y):
		diff = 10
		xPos = x * self.masuwidth
		yPos = y * self.masuheight

		canvas.create_line(xPos + diff, yPos + diff, xPos + self.masuwidth - diff, yPos + self.masuheight - diff, fill = 'blue')
		canvas.create_line(xPos + self.masuwidth - diff, yPos + diff, xPos + diff, yPos + self.masuheight - diff, fill = 'blue')

	def drawO(self, x, y):
		diff = 10
		xPos = x * self.masuwidth
		yPos = y * self.masuheight

		canvas.create_oval(xPos + diff, yPos + diff, xPos + self.masuwidth - diff, yPos + self.masuheight - diff, outline = 'red')

	def mousePressed(self, event):
		global mx, my, isPut
		self.mx = event.x
		self.my = event.y

		if self.turnnum == self.USER:
			if self.board[self.getX(self.mx)][self.getY(self.my)] == self.BLANK:
				self.board[self.getX(self.mx)][self.getY(self.my)] = self.USER
				self.isPut = True
				self.turnnum = self.COMPUTER

	def paint(self):
		# ゲームボード背景
		canvas.create_rectangle(0, 0, self.WIDTH, self.WIDTH, fill = 'yellow')

		# ゲームボード下部背景
		canvas.create_rectangle(0, self.WIDTH, self.WIDTH, self.HEIGHT, fill = self.bgcolor)

		# 境界線
		linecolor = 'black'
		# 横線
		for i in range(self.masucount - 1):
			canvas.create_line(0, (i + 1) * self.masuheight, self.WIDTH, (i + 1) * self.masuheight, fill = linecolor)

		# 縦線
		for i in range(self.masucount - 1):
			canvas.create_line((i + 1) * self.masuwidth, 0, (i + 1) * self.masuwidth, self.WIDTH, fill = linecolor)

		self.repaint()

		# マウスイベント
		canvas.bind('<Button-1>', self.mousePressed)
		canvas.bind('<ButtonRelease-1>', self.repaint)