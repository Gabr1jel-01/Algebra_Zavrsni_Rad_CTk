
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