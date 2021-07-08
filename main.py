import tkinter as tk
import menuFrame
import settingFrame
import gameFrame

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

menuframe = menuFrame.MenuFrame(container, root)
settingframe = settingFrame.SettingFrame(container, root)
gameframe = gameFrame.GameFrame(container, root)

def show_frame(targetFrame):
	global WIDTH, HEIGHT, menuframe, settingframe, gameframe

	for frame in (menuframe, settingframe, gameframe):
		frame.pack_forget()

	if targetFrame == 'メニューフレーム':
		WIDTH = menuframe.getWidth()
		HEIGHT = menuframe.getHeight()
		menuframe.pack()

	elif targetFrame == '設定フレーム':
		WIDTH = settingframe.getWidth()
		HEIGHT = settingframe.getHeight()
		settingframe.pack()

	elif targetFrame == 'ゲームフレーム':
		WIDTH = gameframe.getWidth()
		HEIGHT = gameframe.getHeight()
		gameframe.pack()

	root.update_idletasks()
	x = (root.winfo_screenwidth() // 2) - (WIDTH // 2)
	y = (root.winfo_screenheight() // 2) - (HEIGHT // 2)
	root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

def launch():
	root.mainloop()

show_frame('メニューフレーム')