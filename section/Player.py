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
		self.configure( height= 100 , bg_color='blue')

		self.topline = CTkLabel(
			master=self,
			text='',
			font=('',1),
			image=CTkImage(
				Image.open('assets/line.png'),
				size=(master._current_width,1)
			)
		)
		self.topline.configure(	pady=10 )
		self.topline.pack()

		self.title = CTkLabel( self, text='Lorem Ipsum', font=('',20,'bold'), padx=8, pady=4 )
		self.title.pack( anchor='nw')

		self.progressbar = CTkProgressBar(self,width=(master._current_width/2))
		self.progressbar.configure(mode="indeterminnate")
		self.progressbar.start()
		self.progressbar.pack( anchor='nw', padx=(20,0) )

	def setCurrentTrack( self, artist :str, track:str ) -> None :
		self.title.configure( text=f"{track} • {artist} ")
