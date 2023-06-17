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
window.config(background="#00bcd4")



canvas_for_back_image = ctk.CTkCanvas(window,
                                      height=2000,
                                      width=2000,
                                      bg='#00bcd4',
                                      highlightthickness=0
                                      )

img= ImageTk.PhotoImage(Image.open("pictures/rsz_11modern.jpg"))

canvas_for_back_image.create_image(0,0,anchor='nw',image=img)

canvas_for_back_image.pack(expand=True, fill='both')


canvas_over_back_image = ctk.CTkCanvas(window,
                                       height=800,
                                       width=600,
                                       bg='#eeeeee',
                                       highlightthickness=0)
canvas_over_back_image.place(relx=0.5,rely=0.05)



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
                            text="Prijava",
                            font=('Calisto MT', 40),
                            fg_color="#00bcd4",
                            text_color="#000000"
                            )
#sign_up_label.configure(background="#4c5578")
sign_up_label_big.place(relx=0.7,rely=0.25)

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
                            text="User name:",
                            font=('Calisto MT', 25),
                            fg_color="#00bcd4",
                            text_color="#000000"
                            )
username_label.place(relx=0.65,rely=0.4)


username_entry_box = ctk.CTkEntry(window,
                                width=250,
                                fg_color='white',
                                bg_color='#00bcd4',
                                corner_radius=30,
                                text_color='#000000'
                                )
username_entry_box.place(relx=0.64, rely=0.48)

username_label = ctk.CTkLabel(window,
                            text="Password:",
                            font=('Calisto MT', 25),
                            fg_color="#00bcd4",
                            text_color="#000000"
                            )
username_label.place(relx=0.65,rely=0.55)



password_entry_box = ctk.CTkEntry(window,
                                width=250,
                                fg_color='white',
                                bg_color='#00bcd4',
                                corner_radius=30,
                                text_color='#000000'
                                )
password_entry_box.place(relx=0.64, rely=0.62)


sign_me_in_button = ctk.CTkButton(canvas_for_back_image,
                                text='Prijavi me',
                                text_color='#000000',
                                width=200,
                                height=50,
                                font=('Calisto MT',25),
                                corner_radius=30,
                                bg_color='#00bcd4',
                                fg_color='#98b4d4',
                                hover_color='#4c5578',
                                command=sign_me_in_action)


sign_me_in_button.place(relx=0.67, rely=0.8)





window.mainloop()