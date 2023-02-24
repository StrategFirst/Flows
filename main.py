from tkinter import PhotoImage
import customtkinter
from TabFrames import TabFrames
from PIL import Image

from section.Player import SectionPlayer
from section.Sidebar import SectionSidebar

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("./assets/flows-theme.json")



class App(customtkinter.CTk):

	def __init__(self):
		super().__init__()

		# Configure window
		self.title("Flows")
		self.geometry(f"{1100}x{580}")

		# Configure layout
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure((2, 3), weight=0)
		self.grid_rowconfigure((0, 1, 2), weight=1)

		# Create elements
		self.sidebar_frame = SectionSidebar( 
			master=self,
			
			# Content
			icon=Image.open('./assets/icon.png'),
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
		self.tabview = TabFrames(self, width=250, fg_color=self._fg_color)
		self.tabview.add("Recherche")
		
		self.entry = customtkinter.CTkEntry(self.tabview.tab('Recherche'), placeholder_text="CTkEntry")
		#self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

		self.main_button_1 = customtkinter.CTkButton(master=self.tabview.tab('Recherche'), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
		#self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

		self.tabview.add("Playlist")
		self.tabview.add("Paramètres")
		self.tabview.tab("Paramètres").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
		self.tabview.tab("Playlist").grid_columnconfigure(0, weight=1)

		self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Paramètres"), dynamic_resizing=False,
														values=["Value 1", "Value 2", "Value Long Long Long"])
		self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
		self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Paramètres"),
													values=["Value 1", "Value 2", "Value Long....."])
		self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
		self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Paramètres"), text="Open CTkInputDialog",
														   command=self.open_input_dialog_event)
		self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
		self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Playlist"), text="CTkLabel on Playlist")
		self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

		#self.sidebar_frame.configure( background='#777' )
		#self.tabview.configure( bg='#444' )
		#self.player.configure( background='#999' )
		#self.tabview.tab('Recherche').configure(bg_color='red')
		#self.tabview.tab('Playlist').configure(bg_color='red')
		#self.tabview.tab('Paramètres').configure(bg_color='red')

		# Positioning in layout
		self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
		self.tabview.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
		self.player.grid(row=1,column=1, padx=0, pady=0,  sticky="nsew")

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
	img = PhotoImage(file='assets/icon_sq.png')
	app.tk.call('wm', 'iconphoto', app._w, img)
	app.mainloop()
