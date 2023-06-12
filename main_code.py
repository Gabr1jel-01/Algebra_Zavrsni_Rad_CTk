import tkinter as tk
import customtkinter as ctk 



def main():
    root = ctk.CTk()
    
    def sign_up_window_f():
        
        sign_up_window = Window(root, "PyFlora Posude", "800x600" )
        
        
        pass
    
    
    sign_up_window_f()
    return None

class Window():
    
    def __init__(self,root,title,geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.mainloop()
        
        pass
    pass

class Button():
    
    def __init__(self,root,message, geometry) -> None:
        self.root = root
        self.root.geometry(geometry)
        ctk.Label(self.root, text=message).pack()
        
    
        pass

main()