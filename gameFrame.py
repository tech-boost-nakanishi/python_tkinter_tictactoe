import tkinter as tk
import main
from decimal import Decimal, ROUND_HALF_UP
from tkinter import messagebox
import time
import random
import threading

class GameFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 500
		self.HEIGHT = 600
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT)
		self.pack_propagate(0)

		self.bgcolor = 'lightgray'
		self.BLANK = 0
		self.USER = 1
		self.COMPUTER = 2
		self.DRAW = 3
		self.turnnum = self.BLANK
		self.board = []
		global mx, my
		self.mx = self.my = -1
		self.isPut = False
		self.combination = [
			[[0, 0], [1, 0], [2, 0]],
			[[0, 1], [1, 1], [2, 1]],
			[[0, 2], [1, 2], [2, 2]],
			[[0, 0], [0, 1], [0, 2]],
			[[1, 0], [1, 1], [1, 2]],
			[[2, 0], [2, 1], [2, 2]],
			[[0, 0], [1, 1], [2, 2]],
			[[0, 2], [1, 1], [2, 0]],
		]
		
		global canvas
		canvas = tk.Canvas(self, width = self.WIDTH, height = self.HEIGHT)
		canvas.pack()

		tk.Button(self, text = '最初から', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('ゲームフレーム')).place(x = 20, y = 505)
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('メニューフレーム')).place(x = 20, y = 535)
		tk.Button(self, text = '設定画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, width = 10, command = lambda: main.show_frame('設定フレーム')).place(x = 20, y = 565)

		# ボードリストの初期化
		self.board = [[self.BLANK]*3 for i in range(3)]

		self.masuwidth = self.masuheight = int(Decimal(str(self.WIDTH / len(self.board))).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

		import settingFrame
		settingframe = settingFrame.SettingFrame(main.container, main.root)
		self.attackvalue = settingframe.getATTACKVALUE()
		self.xorovalue = settingframe.getXOROVALUE()
		if self.attackvalue == 0:
			self.turnnum = self.USER
		else:
			self.turnnum = self.COMPUTER

		self.paint()

		self.thread1 = threading.Thread(target=self.start)
		self.thread1.setDaemon(True)
		self.thread1.start()

	def start(self):
		while True:
			# ユーザーのターン
			if self.turnnum == self.USER:
				print('ユーザー')
				while True:
					if self.isPut == True:
						break
				self.isPut = False

			# コンピューターのターン
			elif self.turnnum == self.COMPUTER:
				time.sleep(0.5)
				print('コンピューター')
				self.computerAI()
				self.turnnum = self.USER

			# 再描画
			self.repaint()

			# 勝敗のチェック
			winner = self.checkWinner()
			# ユーザーが勝ちなら
			if winner == self.USER:
				messagebox.showinfo('メッセージ', 'あなたの勝ちです。')
				break

			# コンピューターが勝ちなら
			elif winner == self.COMPUTER:
				messagebox.showinfo('メッセージ', 'あなたの負けです。')
				break

			# 引き分けなら
			elif winner == self.DRAW:
				messagebox.showinfo('メッセージ', '引き分けです。')
				break

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getX(self, mx):
		for i in range(len(self.board)):
			if mx >= i * self.masuwidth and mx <= i * self.masuwidth + self.masuwidth:
				return i

	def getY(self, my):
		for i in range(len(self.board)):
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
		for i in range(len(self.board)):
			canvas.create_line(0, (i + 1) * self.masuheight, self.WIDTH, (i + 1) * self.masuheight, fill = linecolor)

		# 縦線
		for i in range(len(self.board)):
			canvas.create_line((i + 1) * self.masuwidth, 0, (i + 1) * self.masuwidth, self.WIDTH, fill = linecolor)

		# マウスイベント
		canvas.bind('<Button-1>', self.mousePressed)

		self.repaint()

	def computerAI(self):
		# どちらかがリーチの場合
		userlist = []
		for i in range(len(self.combination)):
			usercount = computercount = blankcount = 0
			blankindex = []
			for j in range(len(self.combination[i])):
				x, y = self.combination[i][j][0], self.combination[i][j][1]
				if self.board[x][y] == self.USER:
					usercount += 1
				elif self.board[x][y] == self.COMPUTER:
					computercount += 1
				elif self.board[x][y] == self.BLANK:
					blankcount += 1
					blankindex.append([x, y])

			# コンピューターがリーチなら
			if computercount == 2 and blankcount == 1:
				self.board[blankindex[0][0]][blankindex[0][1]] = self.COMPUTER
				return

			# ユーザーがリーチならuserlistに追加
			if usercount == 2 and blankcount == 1:
				userlist.append([blankindex[0][0], blankindex[0][1]])

		# ユーザーがリーチのパターンがあれば
		if len(userlist) > 0:
			rand = random.randint(0, len(userlist) - 1)
			self.board[userlist[rand][0]][userlist[rand][1]] = self.COMPUTER
			return

		# それ以外はランダム
		while True:
			rx = random.randint(0, len(self.board) - 1)
			ry = random.randint(0, len(self.board) - 1)
			if self.board[rx][ry] == self.BLANK:
				self.board[rx][ry] = self.COMPUTER
				break

	def checkWinner(self):
		blankcount = 0
		for i in range(len(self.combination)):
			usercount = computercount = 0
			for j in range(len(self.combination[i])):
				x, y = self.combination[i][j][0], self.combination[i][j][1]
				if self.board[x][y] == self.USER:
					usercount += 1
				elif self.board[x][y] == self.COMPUTER:
					computercount += 1
				elif self.board[x][y] == self.BLANK:
					blankcount += 1

			# ユーザーが勝ちなら
			if usercount == len(self.board):
				return self.USER

			# コンピューターが勝ちなら
			elif computercount == len(self.board):
				return self.COMPUTER

		# 引き分けなら
		if blankcount == 0:
			return self.DRAW

		return self.BLANK