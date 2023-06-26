import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk
import pictures
import sqlite3
import bcrypt


#class App(ctk.CTk):
    #def __init__(self):
        #super().__init__()
        
        #configure window
window = ctk.CTk()
window.geometry("900x600+325+40")
window.title('PyFlora Posude')
window.iconbitmap('pictures/app_flower_picture.ico')
window.config(background="#e6e6fa")



canvas_for_back_image = ctk.CTkCanvas(window,
                                      height=2000,
                                      width=2000,
                                      bg='#e6e6fa',
                                      highlightthickness=0
                                      )


canvas_for_back_image.pack(expand=True, fill='both')



person_at_table_img = ImageTk.PhotoImage(Image.open("pictures/vector.png"))
avatar_image = ImageTk.PhotoImage(Image.open("pictures/hyy.png"))
canvas_for_back_image.create_image(150,600,anchor='w',image=person_at_table_img)
canvas_for_back_image.create_image(905,120,anchor='w',image=avatar_image)


"""
canvas_over_back_image = ctk.CTkFrame(window,
                                       height=500,
                                       width=400,
                                       corner_radius=40,
                                       bg_color='#e6e6fa',
                                       #fg_color='#e6e6fa'
                                       )
canvas_over_back_image.place(relx=0.5,rely=0.05)

"""


#configure sql
global sql_connection, cursor    
sql_connection = sqlite3.connect('database.db')
cursor = sql_connection.cursor()
        
cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')
                
#label
sign_up_label_big = ctk.CTkLabel(window,
                            text="Your app",
                            font=('Verdana', 50),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
#sign_up_label.configure(background="#4c5578")
sign_up_label_big.place(relx=0.64,rely=0.25)

welcome_label = ctk.CTkLabel(window,
                            text="Welcome",
                            font=('Verdana Pro', 65),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
welcome_label.place(relx=0.10,rely=0.13)


#region FUNKCIJE
def sign_me_in_action():
    username = username_entry_box.get()
    password = password_entry_box.get()
    
    if username !='' and password != '':
        cursor.execute('SELECT username FROM users WHERE username = ?', [username])
        if cursor.fetchone() is not None:
                messagebox.showerror('Greska', 'Korisnicko ime vec postoji!')
                result = cursor.fetchone()
                print(result)           
            
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            #print(hashed_password)
            cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
            sql_connection.commit()
            messagebox.showinfo('Uspjeh', 'Korisnicki racun je napravljen!')
    else:
        messagebox.showerror('Greska', 'Unesite potrebne podatke')
    if cursor.fetchone() is not None:
        result = cursor.fetchone()

#endregion

username_label = ctk.CTkLabel(window,
                            text="Username:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
username_label.place(relx=0.6,rely=0.4)


username_entry_box = ctk.CTkEntry(window,
                                width=250,
                                fg_color='white',
                                bg_color='#e6e6fa',
                                corner_radius=30,
                                text_color='#000000'
                                )
username_entry_box.place(relx=0.59, rely=0.48)

username_label = ctk.CTkLabel(window,
                            text="Password:",
                            font=('Verdana', 25),
                            fg_color="#e6e6fa",
                            text_color="#000000"
                            )
username_label.place(relx=0.6,rely=0.55)



password_entry_box = ctk.CTkEntry(window,
                                width=250,
                                fg_color='white',
                                bg_color='#e6e6fa',
                                corner_radius=30,
                                text_color='#000000',
                                show="•"
                                )
password_entry_box.place(relx=0.59, rely=0.62)


sign_me_in_button = ctk.CTkButton(window,
                                text='Sign up',
                                text_color='#000000',
                                width=200,
                                height=50,
                                font=('Verdana',25),
                                corner_radius=30,
                                bg_color='#e6e6fa',
                                fg_color='#98b4d4',
                                hover_color='#4c5578',
                                command=sign_me_in_action)


sign_me_in_button.place(relx=0.61, rely=0.8)





window.mainloop()