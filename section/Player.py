from customtkinter import CTkFrame, CTkProgressBar, CTkLabel, CTkImage
from PIL import Image

class SectionPlayer(CTkFrame):


	def __init__( self,
		
		master	: any,

		height	: int,

		** kwargs
	):
		super().__init__(
			master=master,
			height=height,

			**kwargs
		)

		self.topline = CTkLabel(self,text='',font=('Roboto',1),image=CTkImage(Image.open('assets/line.png'),size=(master._current_width,1)))
		self.topline.configure(	pady=10)
		self.topline.pack()

		self.a = CTkLabel(self,text='Lorem Ipsum',font=('Roboto',20,'bold') )
		self.a.pack()

		self.b = CTkLabel(self,text='Lorem Ipsum',font=('Roboto',12,'normal') )
		self.b.pack()

		self.progressbar = CTkProgressBar(self,width=(master._current_width/2))
		self.progressbar.configure(mode="indeterminnate")
		self.progressbar.start()
		self.progressbar.pack()


