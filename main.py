from tkinter import PhotoImage
import customtkinter
from TabFrames import TabFrames
from PIL import Image

from section.Player import SectionPlayer
from section.Sidebar import SectionSidebar

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("./assets/flows-theme.json")

from tabs.SettingsTab import settingsTab
from tabs.SearchTab import searchTab

class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()

		# Configure window
		self.title("Flows")
		self.geometry(f"{1100}x{580}")

		# Configure layout
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure((2, 3), weight=0)
		self.grid_rowconfigure((0, 1), weight=1)

		# Create elements
		self.sidebar_frame = SectionSidebar( 
			master=self,
			
			# Content
			icon=(
				Image.open('./assets/icon.png'),
				Image.open('./assets/icon_reverse.png'),
			),
			menu=['Recherche','Playlist','Paramètres'],
			callback=self.sidebarMenu,

			# Style
			width=100,
			corner_radius=0,
			menuIcon=[
				Image.open('./assets/icons/lence.png'),
				Image.open('./assets/icons/playlist.png'),
				Image.open('./assets/icons/gear.png'),
			]
		)

		self.player = SectionPlayer (
			master=self,
			height=200,
			fg_color=self._fg_color,
		)



		# create tabview
		self.tabview = TabFrames(self, width=250, fg_color=self._fg_color, height=450)
		self.tabview.add("Recherche")
		
		self.entry = customtkinter.CTkEntry(self.tabview.tab('Recherche'), placeholder_text="CTkEntry")

		self.main_button_1 = customtkinter.CTkButton(master=self.tabview.tab('Recherche'), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))

		self.tabview.add("Playlist")
		self.tabview.add("Paramètres")

		settingsTab( self.tabview.tab('Paramètres') )
		searchTab( self.tabview.tab('Recherche') )
		
		self.tabview.tab("Paramètres").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
		self.tabview.tab("Playlist").grid_columnconfigure(0, weight=1)
		

		self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Playlist"), text="CTkLabel on Playlist")
		self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

		# Positioning in layout
		self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
		self.tabview.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
		self.player.grid(row=1,column=1, padx=0, pady=0,  sticky="nsew")

		# temp
		self.player.setCurrentTrack( artist='John newman' , track='Love me again' )

	def open_input_dialog_event(self):
		dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
		print("CTkInputDialog:", dialog.get_input())

	def change_appearance_mode_event(self, new_appearance_mode: str):
		customtkinter.set_appearance_mode(new_appearance_mode)

	def change_scaling_event(self, new_scaling: str):
		new_scaling_float = int(new_scaling.replace("%", "")) / 100
		customtkinter.set_widget_scaling(new_scaling_float)

	def sidebarMenu(self,tab):
		self.tabview.set(tab)


if __name__ == "__main__":
	app = App()
	app.title("Flows")
	img = PhotoImage(file='assets/icon.ico')
	app.after(100, lambda: app.wm_iconphoto(False, img))
	
	app.mainloop()
