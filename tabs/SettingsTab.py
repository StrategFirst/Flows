from customtkinter import CTkComboBox, CTkFrame, CTkLabel, CTkSlider

def settingsTab( tab : CTkFrame ) -> None :
    initialSizeSetting = CTkFrame( master=tab )
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
    CTkComboBox(
        master=initialSizeSetting,
        values=['1100','750','800','1000','1500','1920']
    ).grid( row=1 , column=1 )
    CTkLabel(
        master=initialSizeSetting,
        text='Hauteur'
    ).grid( 
        padx=5 , pady=5 ,
        row=2 , column=0 ,)
    CTkComboBox(
        master=initialSizeSetting,
        values=['580','400','500','700','850','1080']
    ).grid( row=2 , column=1 )
    CTkLabel(
        master=initialSizeSetting,
        text='Échelle'
    ).grid( 
        padx=5 , pady=5 ,
        row=3 , column=0 ,)
    CTkSlider(
        master=initialSizeSetting,
        from_=50,
        to=200,
        number_of_steps=16
    ).grid( row=3 , column=1 )

    initialSizeSetting.configure( fg_color = tab._fg_color )
    initialSizeSetting.grid( row=1 , column=1 )
    
    ##########
    ##########
    ##########

