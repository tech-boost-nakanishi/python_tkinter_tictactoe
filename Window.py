import tkinter

class WindowClass:
	def __init__(self):
		self.root = tkinter.Tk()
		self.root.title('○×ゲーム')
		self.root.geometry('250x160')

		# メニューバーを作成
		menubar = tkinter.Menu(self.root)
		self.root.config(menu = menubar)

		# メニューバーにメニューを作成
		menu = tkinter.Menu(menubar)
		menubar.add_cascade(label = 'メニュー', menu = menu)

		menu.add_command(label='メインメニュー')
		menu.add_command(label='ゲーム開始')
		menu.add_command(label='設定画面')
		menu.add_command(label='ゲーム終了', command = self.root.destroy)

		self.root.mainloop()

if __name__ == '__main__':
	wc = WindowClass()