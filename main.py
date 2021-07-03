import tkinter as tk

class WindowClass(tk.Tk):

	global MenuFrame, SettingFrame, GameFrame
	WIDTH = 0
	HEIGHT = 0

	def __init__(self):
		tk.Tk.__init__(self)
		self.title('○×ゲーム')
		self._frame = None

		# メニューバーを作成
		menubar = tk.Menu(self)
		self.config(menu = menubar)

		# メニューバーにメニューを作成
		menu = tk.Menu(menubar)
		menubar.add_cascade(label = 'メニュー', menu = menu)

		# メニューに子メニュー作成
		menu.add_command(label='メインメニュー', command = lambda: self.show_frame('メニューフレーム'))
		menu.add_command(label='ゲーム開始', command = lambda: self.show_frame('ゲームフレーム'))
		menu.add_command(label='設定画面', command = lambda: self.show_frame('設定フレーム'))
		menu.add_separator()
		menu.add_command(label='ゲーム終了', command = self.destroy)

		self.container = tk.Frame(self)
		self.container.pack()

		# 各フレームのインスタンス生成
		import menuFrame
		import settingFrame
		import gameFrame

		global MenuFrame, SettingFrame, GameFrame
		MenuFrame = menuFrame.MenuFrameClass(self.container, self)
		SettingFrame = settingFrame.SettingFrameClass(self.container, self)
		GameFrame = gameFrame.GameFrameClass(self.container, self)

		self.show_frame('メニューフレーム')

		self.resizable(False, False)

	def iconify(self):
		self.iconify()

	def getContainer(self):
		return self._frame

	def setContainer(self, targetFrame):
		self._frame = targetFrame

	def setWidth(self, width):
		self.WIDTH = width

	def setHeight(self, height):
		self.HEIGHT = height

	def getWidth(self):
		return self.WIDTH

	def getHeight(self):
		return self.HEIGHT

	def show_frame(self, targetFrame):
		global MenuFrame, SettingFrame, GameFrame
		
		for F in (MenuFrame, SettingFrame, GameFrame):
			F.pack_forget()
			
		if targetFrame == 'メニューフレーム':
			self.setContainer(MenuFrame)
			self.setWidth(self.getContainer().getWidth())
			self.setHeight(self.getContainer().getHeight())
			MenuFrame.pack()

		elif targetFrame == '設定フレーム':
			self.setContainer(SettingFrame)
			self.setWidth(self.getContainer().getWidth())
			self.setHeight(self.getContainer().getHeight())
			SettingFrame.pack()

		elif targetFrame == 'ゲームフレーム':
			self.setContainer(GameFrame)
			self.setWidth(self.getContainer().getWidth())
			self.setHeight(self.getContainer().getHeight())
			GameFrame.pack()

		# ウィンドウを中央に表示
		self.update_idletasks()
		x = (self.winfo_screenwidth() // 2) - (self.getWidth() // 2)
		y = (self.winfo_screenheight() // 2) - (self.getHeight() // 2)
		self.geometry('{}x{}+{}+{}'.format(self.getWidth(), self.getHeight(), x, y))

if __name__ == '__main__':
	wc = WindowClass()
	wc.mainloop()