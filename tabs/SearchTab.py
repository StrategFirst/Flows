from customtkinter import CTkEntry, CTkFrame, CTkScrollableFrame
from utils.VideoFrame import VideoFrame
from utils.ytbSearchScrapper import ytbSearchScrapper

#from tkinter import KeyEvent

class searchTab(CTkFrame):
	
	def __init__( self , master_tab : CTkFrame ):
		super().__init__(
			master=master_tab,
			fg_color=master_tab._fg_color,
		)
		self.searchbar = CTkEntry(
			master=self,
			width=(master_tab.master.master._current_width*80/100),
			#
		)
		self.searchbar.grid(
			row=0 , column=0,
			padx=20
		)
		self.searchbar.bind(
			sequence='<Return>',
			command=self.search,
		)
		self.results = CTkScrollableFrame( master=self , fg_color=self._fg_color , width=800 , height=350)
		self.results.grid( row=1 , column=0 )
		self.list = []
		self.pack()

	def search( self , event ):
		query = event.widget.get()
		if query == '':
			return

		for i in list(range(len(self.list)))[::-1]:
			self.list[i].destroy()
			del self.list[i]
		
		self.list = [
				VideoFrame(
					master	= self.results,

					id = result.get('id'),
					title = result.get('title'),
					duration = result.get('length'),

					height = 15,
					fg_color = self._fg_color,

				)
			for 
				result
			in 
				ytbSearchScrapper( query ).results
		]

		for i in range(len(self.list)):
			self.list[i].grid( row=i , column=1 )
