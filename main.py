import tkinter as tk
import menuFrame
import settingFrame
import gameFrame
import sqlite3

# データの初期設定　マークは○, 順番は先攻
conn = sqlite3.connect('setting.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS settings(id integer, mark integer, attack integer)')
cur.execute('INSERT INTO settings(id,mark,attack) SELECT 1,0,0 WHERE NOT EXISTS(SELECT 1 FROM settings WHERE id = 1)')
conn.commit()
cur.close()
conn.close()

WIDTH = 0
HEIGHT = 0

root = tk.Tk()
root.title('○×ゲーム')
root.resizable(False, False)

# メニューバーを作成
menubar = tk.Menu(root)
root.config(menu = menubar)

# メニューバーにメニューを作成
menu = tk.Menu(menubar)
menubar.add_cascade(label = 'メニュー', menu = menu)

# メニューに子メニュー作成
menu.add_command(label='メインメニュー', command = lambda: show_frame('メニューフレーム'))
menu.add_command(label='ゲーム開始', command = lambda: show_frame('ゲームフレーム'))
menu.add_command(label='設定画面', command = lambda: show_frame('設定フレーム'))
menu.add_separator()
menu.add_command(label='ゲーム終了', command = root.destroy)

container = tk.Frame(root)
container.pack()

menuframe = settingframe = gameframe = tk.Frame(root)

def show_frame(targetFrame):
	global WIDTH, HEIGHT, menuframe, settingframe, gameframe

	try:
		if gameframe.thread1.is_alive():
			gameframe.stop()
	except AttributeError:
		pass

	for frame in (menuframe, settingframe, gameframe):
		frame.destroy()

	if targetFrame == 'メニューフレーム':
		menuframe = menuFrame.MenuFrame(container, root)
		menuframe.pack()
		WIDTH = menuframe.getWidth()
		HEIGHT = menuframe.getHeight()

	elif targetFrame == '設定フレーム':
		settingframe = settingFrame.SettingFrame(container, root)
		settingframe.pack()
		WIDTH = settingframe.getWidth()
		HEIGHT = settingframe.getHeight()

	elif targetFrame == 'ゲームフレーム':
		gameframe = gameFrame.GameFrame(container, root)
		gameframe.pack()
		WIDTH = gameframe.getWidth()
		HEIGHT = gameframe.getHeight()

	root.update_idletasks()
	x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
	y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
	root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

def launch():
	root.mainloop()

show_frame('メニューフレーム')