from customtkinter import CTkComboBox, CTkFrame, CTkLabel, CTkButton
from customtkinter import set_widget_scaling

from utils.SizeHandling import SizeHandler
from utils.Configuration import Config

class SettingsTab(CTkFrame):
	
	def __init__( self , master_tab : CTkFrame ):
		super().__init__(
			master=master_tab,
			fg_color=master_tab._fg_color,
		)
		initialSizeSetting = CTkFrame( master=self )
		CTkLabel(
			master=initialSizeSetting,
			text='Taille de fenêtre',
			font=('',18)
		).grid(
			padx=5 , pady=5 ,
			row=0 , column=0 , 
			columnspan=2 ,)
		CTkLabel(
			master=initialSizeSetting,
			text='Largeur'
		).grid( 
			padx=5 , pady=5 ,
			row=1 , column=0 ,)
		self.w = CTkComboBox(
			master=initialSizeSetting,
			values=[str(SizeHandler.get_totalWidth()),'750','800','1000','1500','1920']
		)
		self.w.grid( row=1 , column=1 )
		CTkLabel(
			master=initialSizeSetting,
			text='Hauteur'
		).grid( 
			padx=5 , pady=5 ,
			row=2 , column=0 ,)
		self.h = CTkComboBox(
			master=initialSizeSetting,
			values=[str(SizeHandler.get_totalHeight()),'400','500','700','850','1080']
		)
		self.h.grid( row=2 , column=1 )
		CTkButton(
			master=initialSizeSetting,
			text='Enregistrer',
			command=self.setSize,
		).grid( 
			padx=5 , pady=5 ,
			row=3 , column=0 ,
			columnspan=2)

		initialSizeSetting.configure( fg_color = master_tab.master._fg_color )
		initialSizeSetting.grid( row=1 , column=1 )
		self.pack(
			padx=0,
			pady=0,)
		
		##########
		##########
		##########
	
	def setSize(self):
		W = int(self.w.get())
		H = int(self.h.get())
		T = self
		while T.master != None : T = T.master;
		SizeHandler.setSize( 
			app = T,
			width = W,
			height = H, 
		)
		Config.set( ['initial_size','width'] , value=W , save=False)
		Config.set( ['initial_size','height'] , value=H , save=True)


