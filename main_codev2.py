import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3
import bcrypt
from tkinter import ttk


class App(ctk.CTk):
    def __init__(self):
        # Configure window
        self.window = ctk.CTk()
        self.window.geometry("900x600+325+40")
        self.window.title('PyFlora Posude')
        self.window.iconbitmap('pictures/app_flower_picture.ico')
        self.window.config(background="#e6e6fa")
        self.window.resizable(False, False)

        # Canvas for background image
        self.canvas_for_back_image = ctk.CTkCanvas(self.window,
                                                   height=2000,
                                                   width=2000,
                                                   bg='#e6e6fa',
                                                   highlightthickness=0)
        self.canvas_for_back_image.pack(expand=True, fill='both')

        # Load and display background images
        self.person_at_table_img = ImageTk.PhotoImage(Image.open("pictures/vector.png"))
        self.avatar_image = ImageTk.PhotoImage(Image.open("pictures/hyy.png"))
        self.canvas_for_back_image.create_image(150, 600, anchor='w', image=self.person_at_table_img)
        self.canvas_for_back_image.create_image(930, 55, anchor='w', image=self.avatar_image)

        # Configure SQL database
        self.sql_connection = sqlite3.connect('database.db')
        self.cursor = self.sql_connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL )''')
                
        self.sign_up_label_big = ctk.CTkLabel(self.window,
                                              text="PyFlora",
                                              font=('Verdana', 70),
                                              fg_color="#e6e6fa",
                                              text_color="#000000")
        self.sign_up_label_big.place(relx=0.17, rely=0.15)

        """
        self.welcome_label = ctk.CTkLabel(self.window,
                                          text="Dobrodosli",
                                          font=('Verdana Pro', 65),
                                          fg_color="#e6e6fa",
                                          text_color="#000000")
        self.welcome_label.place(relx=0.10, rely=0.13)
        """
        
        self.password_label = ctk.CTkLabel(self.window,
                            text="Sifra:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
        self.password_label.place(relx=0.6,rely=0.60)
        
        self.username_label = ctk.CTkLabel(self.window,
                            text="Korisnicko ime:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
        self.username_label.place(relx=0.6,rely=0.45)
        
        self.first_name_label = ctk.CTkLabel(self.window,
                            text="Ime:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
        self.first_name_label.place(relx=0.6,rely=0.14)
        
        self.last_name_label = ctk.CTkLabel(self.window,
                            text="Prezime:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
        self.last_name_label.place(relx=0.6,rely=0.3)
        
        # Entry boxes
        self.username_entry_box = ctk.CTkEntry(self.window,
                                               width=250,
                                               fg_color='white',
                                               bg_color='#e6e6fa',
                                               corner_radius=30,
                                               text_color='#000000')
        self.username_entry_box.place(relx=0.59, rely=0.53)

        self.password_entry_box = ctk.CTkEntry(self.window,
                                               width=250,
                                               fg_color='white',
                                               bg_color='#e6e6fa',
                                               corner_radius=30,
                                               text_color='#000000',
                                               show="•")
        self.password_entry_box.place(relx=0.59, rely=0.67)
        
        self.first_name_entry_box = ctk.CTkEntry(self.window,
                                               width=250,
                                               fg_color='white',
                                               bg_color='#e6e6fa',
                                               corner_radius=30,
                                               text_color='#000000')
        self.first_name_entry_box.place(relx=0.59, rely=0.22)
        
        self.last_name_entry_box = ctk.CTkEntry(self.window,
                                               width=250,
                                               fg_color='white',
                                               bg_color='#e6e6fa',
                                               corner_radius=30,
                                               text_color='#000000')
        self.last_name_entry_box.place(relx=0.59, rely=0.37)

    
        # Button
        self.sign_me_in_button = ctk.CTkButton(self.window,
                                               text='Stvori racun',
                                               text_color='#000000',
                                               width=200,
                                               height=50,
                                               font=('Verdana', 25),
                                               corner_radius=30,
                                               bg_color='#e6e6fa',
                                               fg_color='#98b4d4',
                                               hover_color='#4c5578',
                                               command=self.sign_me_in_action)
        self.sign_me_in_button.place(relx=0.61, rely=0.87)
        
        def tab_view(self):
            
            # Create the main application window
            window = ctk.CTk()
            window.geometry("900x600+325+40")
            window.title('PyFlora Posude')
            window.iconbitmap('pictures/app_flower_picture.ico')
            window.config(background="#e6e6fa")
            window.resizable(False, False)
            
            
            s = ttk.Style()
            s.theme_use('default')
            s.configure('TNotebook.Tab', background="#38D8FF")
            s.map("TNotebook", background=[("selected", "black")])

            # Create a CustomNotebook widget
            notebook = ttk.Notebook(window)
            
            # Create tabs/pages
            tab1 = ctk.CTkFrame(notebook,fg_color="#e6e6fa")
            tab2 = ctk.CTkFrame(notebook,fg_color="#e6e6fa")
            tab3 = ctk.CTkFrame(notebook,fg_color="#e6e6fa")

            # Add tabs to the notebook
            notebook.add(tab1, text="Moj Profil")
            notebook.add(tab2, text="Posude")
            notebook.add(tab3,text="Postavke")
            

            def tab1_function():
                
                moj_profil_label = ctk.CTkLabel(tab1, text="Moj profil",font=("Verdana",50),text_color="black")
                moj_profil_label.pack(anchor="n")
                
                posude_label = ctk.CTkLabel(tab2, text="Posude",font=("Verdana",50),text_color="black")
                posude_label.pack(anchor="n")
            
                postavke_label = ctk.CTkLabel(tab3, text="Postavke",font=("Verdana",50),text_color="black")
                postavke_label.pack(anchor="n")
                
                # Label za posude po Posude
                
                
                
                
                
                
                
                
                pass
                
            
            
            
            # Add content to the tabs
            tab1_function()
            
            

            # Pack the notebook
            notebook.pack(expand=True, fill='both')

            # Start the main event loop
            window.mainloop()
            
            
            
        
        def kill_first_window(self,tab_view):
            self.window.destroy()
            tab_view(self)
        
        def log_me_in_action():
            
            
            first_name = self.first_name_entry_box.get()
            last_name = self.last_name_entry_box.get()
            username = self.username_entry_box.get()
            password = self.password_entry_box.get()
            
            if username !='' and password !='' and first_name !='' and last_name !='':
                self.cursor.execute('SELECT password FROM users WHERE username=? AND first_name=? AND last_name=?', [username,first_name,last_name])
                result = self.cursor.fetchone()
                if result:
                    if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                        messagebox.showinfo('Uspijeh', 'Uspijesno ste se ulogirali.')
                        #OVDJE UNESI FUNKCIJU KOJA SE IZVRSI KOD SUCESSFULL LOGINA
                        kill_first_window(self,tab_view)
                    else:
                        messagebox.showerror('Greska', 'Pogresna sifra')
                else:
                    messagebox.showerror('Greska', 'Nepostojece korisnicko ime.')
            else:
                messagebox.showerror('Greska', 'Unesite potrebne podatke.')
        
        self.log_me_in_button = ctk.CTkButton(self.window,
                                               text='Ulogiraj me',
                                               text_color='#000000',
                                               width=200,
                                               height=50,
                                               font=('Verdana', 25),
                                               corner_radius=30,
                                               bg_color='#e6e6fa',
                                               fg_color='#98b4d4',
                                               hover_color='#4c5578',
                                               command=log_me_in_action)
        self.log_me_in_button.place(relx=0.61, rely=0.75)

    def sign_me_in_action(self):
        
        username = self.username_entry_box.get()
        password = self.password_entry_box.get()
        first_name = self.first_name_entry_box.get()
        last_name = self.last_name_entry_box.get()

        if username != '' and password != '':
            self.cursor.execute('SELECT username FROM users WHERE username = ?', [username])
            if self.cursor.fetchone() is not None:
                messagebox.showerror('Greska', 'Korisnicko ime vec postoji!')
                result = self.cursor.fetchone()
                print(result)
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                self.cursor.execute('INSERT INTO users VALUES (?,?,?,?)', [username, hashed_password,first_name,last_name])
                self.sql_connection.commit()
                messagebox.showinfo('Uspjeh', 'Korisnicki racun je napravljen!')
        else:
            messagebox.showerror('Greska', 'Unesite potrebne podatke')
        if self.cursor.fetchone() is not None:
            result = self.cursor.fetchone()

    def run(self):
        # Run the main loop
        self.window.mainloop()
        
        
    

    
    
    
    
    
    
        

if __name__ == '__main__':
    app = App()
    app.run()