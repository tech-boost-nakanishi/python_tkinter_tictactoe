import tkinter as tk
import main

class SettingFrame(tk.Frame):

	WIDTH = 500
	HEIGHT = 300
	bgcolor = 'lightgray'

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.pack()
		self.pack_propagate(0)

		tk.Label(self, text="設定画面", font=('Helvetica', 26, "bold"), bg = 'lightgray').place(x = 195, y = 20)

		# マーク選択ラベルフレーム
		ox_frame = tk.LabelFrame(self, width=150, height=150, text='マーク', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 5)
		ox_frame.place(x = 95, y = 70)
		ox_frame.pack_propagate(0)
		xorovalue = tk.StringVar()
		oradio = tk.Radiobutton(ox_frame, value=0, variable=xorovalue, text='○', font=('Arial', 50, 'bold'), bg = self.bgcolor)
		oradio.place(x = 40, y = 0)
		xradio = tk.Radiobutton(ox_frame, value=1, variable=xorovalue, text='×', font=('Arial', 50, 'bold'), bg = self.bgcolor)
		xradio.place(x = 40, y = 50)

		# 先攻後攻選択ラベルフレーム
		attack_frame = tk.LabelFrame(self, width=150, height=150, text='先攻 or 後攻', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 5)
		attack_frame.place(x = 255, y = 70)
		attack_frame.pack_propagate(0)
		attackvalue = tk.StringVar()
		fradio = tk.Radiobutton(attack_frame, value=0, variable=attackvalue, text='先攻', font=('Arial', 30, 'bold'), bg = self.bgcolor)
		fradio.place(x = 25, y = 10)
		sradio = tk.Radiobutton(attack_frame, value=1, variable=attackvalue, text='後攻', font=('Arial', 30, 'bold'), bg = self.bgcolor)
		sradio.place(x = 25, y = 60)

		# 変更ボタン
		tk.Button(self, text = '変　更', bg = self.bgcolor, highlightbackground = self.bgcolor).place(x = 215, y = 225)

		# メニュー画面遷移ボタン
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('メニューフレーム')).place(x = 120, y = 255)

		# ゲーム画面遷移ボタン
		tk.Button(self, text = 'ゲーム画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('ゲームフレーム')).place(x = 260, y = 255)

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT