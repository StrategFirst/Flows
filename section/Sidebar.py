from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton, CTkSwitch, CTkSlider
from customtkinter import get_appearance_mode, set_appearance_mode
from typing import List, Callable, Tuple
from PIL import Image
from utils.SizeHandling import SizeHandler
class Sidebar(CTkFrame):

	def __init__( self,
		
		master	: any,

		icon	: Tuple[any,any],
		menu	: List[str],

		callback: Callable,

		menuIcon : List[any],

		** kwargs
	):
		super().__init__(
			master=master,
			width=SizeHandler.get_sidebarWidth(),
			height=SizeHandler.get_sidebarHeight(),

			**kwargs
		)

		self.callback = callback

		## Creation
		# App's icon
		width = SizeHandler.get_sidebarWidth()
		self.icon = CTkLabel( 
			master = self , 
			text = ' ' ,
			image =	CTkImage(
				light_image=icon[1],
				dark_image=icon[0],
				size=(width,icon[0].height*(width/icon[0].width))
			),
			padx = 0,
		)

		# menu's button's
		self.menu = [ 
				
				CTkButton( 
					master=self , 
					text=content ,
					command= self.factoryChangeTab(content) ,
					image = CTkImage(
						light_image=contentIcon,
						dark_image=contentIcon,
						size=(20,20)
					),
					corner_radius=0,

				) 
			for 
				(content,contentIcon) 
			in 
				zip(menu,menuIcon)
			]

		# fast opt's interface
		x = CTkFrame( master=self , bg_color='transparent' , width=width , fg_color=self._fg_color )
		CTkLabel(
			master=x ,
			text= '' ,
			image= CTkImage(
					light_image=Image.open('./assets/icons/moon_reverse.png'),
					dark_image=Image.open('./assets/icons/moon.png'),
					size=(20,20)),

			width=width/2,
		).grid( row=0 , column=0 , padx=(20,0) , pady=(12,12))
		CTkSwitch(
			master=x ,
			text= '' ,
			command= self.switchDarkLight,
			width=width/2,
		).grid( row=0 , column=1 )
		y = CTkFrame( master=self , bg_color='transparent' , width=width , fg_color=self._fg_color )
		CTkLabel(
			master=y ,
			text= 'Volume :' ,
			width=width/2,
		).grid( row=0 , column=0 , padx=3 , pady=3 )
		CTkSlider(
			master=y,
			width=width,
			#min=0,
			#max=100,
		).grid( row=1 , column=0 , padx=3 , pady=3 )
		

		self.fopt = [ x , y ]

		self.spacing = CTkLabel(
			master=self ,
			text= ' ' ,
			width=width,
		)
		

		## Inserting
		self.icon.grid( row=0 , column=0 , padx=20 , pady=20 )
		for i,m in enumerate(self.menu) : 
			m.grid( row=(i+1) , column=0 , padx=0 , pady=(0,1) )
		k = len(self.menu)
		self.spacing.grid( row=k+1 , column=0 )
		self.grid_rowconfigure(k+1, weight=1)
		for i,m in enumerate(self.fopt) :
			m.grid( row=(i+k+2) , column=0 , padx=0 , pady=0 )

		SizeHandler.subscribe( self.updateSize )

	def updateSize(self):
		self.configure( 
			width=SizeHandler.get_sidebarWidth(),
			height=SizeHandler.get_sidebarHeight(),
		)

	def factoryChangeTab( self , tabName ):
		return lambda : self.callback( tabName )

	def switchDarkLight( self ):
		if get_appearance_mode() == 'Dark':
			set_appearance_mode('Light')
		else:
			set_appearance_mode('Dark')

