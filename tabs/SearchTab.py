from customtkinter import CTkEntry, CTkFrame, CTkScrollableFrame
from utils.VideoFrame import VideoFrame
from utils.ytbSearchScrapper import ytbSearchScrapper
from utils.SizeHandling import SizeHandler
from utils.ErrorPopup import ErrorPopup

class SearchTab(CTkFrame):
	
	def __init__( self , master_tab : CTkFrame ):
		super().__init__(
			master=master_tab,
			fg_color=master_tab._fg_color,
		)
		self.searchbar = CTkEntry(
			master=self,
			width=(SizeHandler.get_mainWidth()*80/100),
		)
		self.searchbar.grid(
			row=0 , column=0,
			padx=0, 
		)
		self.searchbar.bind(
			sequence='<Return>',
			command=self.search,
		)
		self.results = CTkScrollableFrame( master=self , fg_color=self._fg_color , width=800 , height=350)
		self.results.grid( row=1 , column=0 )
		self.list = []
		self.pack(
			padx=0,
			pady=0,)
		SizeHandler.subscribe( self.updateSize )

	def updateSize(self):
		self.configure(
			width=SizeHandler.get_mainWidth(),
			height=SizeHandler.get_mainHeight(),
		)
		self.searchbar.configure( 
			width= int(SizeHandler.get_mainWidth()*80/100),
		)
		self.results.configure( 
			width= int(SizeHandler.get_mainWidth()*80/100),
		)

	def search( self , event ):
		try:
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
		except BaseException as e:
			print( 'Catched error : ' , e )
			T = self
			while T.master != None: 
				T = T.master
			ErrorPopup( T , 'Une erreur est survenu pendant la recherche' )

