from customtkinter import CTkToplevel, CTkButton, CTkLabel

class ErrorPopup(CTkToplevel):

    def __init__(
        self,
        master,
        msg :str, 
        *args, 
        **kwargs):
        super().__init__(master,*args, **kwargs)

        self.geometry("300x100")
        self.title("Flows error")

        self.info_txt = CTkLabel(self, text=msg )
        self.info_txt.pack(anchor="c", padx=2,pady=2)
        self.ok_btn = CTkButton(self, text="Ok", command=self.destroy)
        self.ok_btn.pack(anchor="c", padx=2, pady=2)

        self.toplevel_window = None
        self.after( 100 , self.focus )

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
