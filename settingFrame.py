import tkinter as tk
from tkinter import messagebox
import main
import sqlite3

class SettingFrame(tk.Frame):

	def __init__(self, parent, controller):
		self.WIDTH = 500
		self.HEIGHT = 300
		self.bgcolor = 'lightgray'
		tk.Frame.__init__(self, parent, width = self.WIDTH, height = self.HEIGHT, bg = self.bgcolor)
		self.pack_propagate(0)

		tk.Label(self, text="設定画面", font=('Helvetica', 26, "bold"), bg = 'lightgray').place(x = 195, y = 20)

		# マーク選択ラベルフレーム
		self.ox_frame = tk.LabelFrame(self, width=150, height=150, text='マーク', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 5)
		self.ox_frame.place(x = 95, y = 70)
		self.ox_frame.pack_propagate(0)
		self.xorovalue = tk.IntVar()
		self.xorovalue.set(self.getXOROVALUE())
		self.oradio = tk.Radiobutton(self.ox_frame, value=0, variable=self.xorovalue, text='○', font=('Arial', 50, 'bold'), bg = self.bgcolor)
		self.oradio.place(x = 40, y = 0)
		self.xradio = tk.Radiobutton(self.ox_frame, value=1, variable=self.xorovalue, text='×', font=('Arial', 50, 'bold'), bg = self.bgcolor)
		self.xradio.place(x = 40, y = 50)

		# 先攻後攻選択ラベルフレーム
		self.attack_frame = tk.LabelFrame(self, width=150, height=150, text='先攻 or 後攻', font=('Arial', 20, 'bold'), bg = self.bgcolor, bd = 5)
		self.attack_frame.place(x = 255, y = 70)
		self.attack_frame.pack_propagate(0)
		self.attackvalue = tk.IntVar()
		self.attackvalue.set(self.getATTACKVALUE())
		self.fradio = tk.Radiobutton(self.attack_frame, value=0, variable=self.attackvalue, text='先攻', font=('Arial', 30, 'bold'), bg = self.bgcolor)
		self.fradio.place(x = 25, y = 10)
		self.sradio = tk.Radiobutton(self.attack_frame, value=1, variable=self.attackvalue, text='後攻', font=('Arial', 30, 'bold'), bg = self.bgcolor)
		self.sradio.place(x = 25, y = 60)

		# 変更ボタン
		tk.Button(self, text = '変　更', bg = self.bgcolor, highlightbackground = self.bgcolor, command = self.changeSettings).place(x = 215, y = 225)

		# メニュー画面遷移ボタン
		tk.Button(self, text = 'メニュー画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('メニューフレーム')).place(x = 120, y = 255)

		# ゲーム画面遷移ボタン
		tk.Button(self, text = 'ゲーム画面へ', bg = self.bgcolor, highlightbackground = self.bgcolor, command = lambda: main.show_frame('ゲームフレーム')).place(x = 260, y = 255)

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def getXOROVALUE(self):
		conn = sqlite3.connect('setting.db')
		cur = conn.cursor()
		result = cur.execute('SELECT mark FROM settings WHERE id = 1').fetchone()
		cur.close()
		conn.close()
		return result[0]

	def getATTACKVALUE(self):
		conn = sqlite3.connect('setting.db')
		cur = conn.cursor()
		result = cur.execute('SELECT attack FROM settings WHERE id = 1').fetchone()
		cur.close()
		conn.close()
		return result[0]

	def changeSettings(self):
		if messagebox.askyesno('確認', '設定を変更してもよろしいですか？') == True:
			conn = sqlite3.connect('setting.db')
			cur = conn.cursor()
			cur.execute('UPDATE settings SET mark = {}, attack = {} WHERE id = 1'.format(self.xorovalue.get(), self.attackvalue.get()))
			conn.commit()
			cur.close()
			conn.close()

			if messagebox.showinfo('メッセージ', '設定を変更しました。') == 'ok':
				self.xorovalue.set(self.getXOROVALUE())
				self.attackvalue.set(self.getATTACKVALUE())