from customtkinter import CTkFrame, CTkLabel

class VideoFrame(CTkFrame):
	
	def __init__( self,
		
		master	: any,

		id : str,
		title : str,
		duration : str,

		height : int,

		** kwargs
	):
		super().__init__(
			height=height,
			master=master,
			**kwargs
		)

		self.configure(
			border_width=1,
			border_color='red',
		)

		self.title = CTkLabel(
			master = self,
			text = title[:42],
			width=420,
			justify='left',
		).grid( column=1 , row=0)

		self.duration = CTkLabel(
			master = self,
			text = duration,
			text_color = 'gray50',
			width=50,
			justify='right',
		).grid( column=2 , row=0 )