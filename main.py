import customtkinter as ctk

# criando a janela
janela = ctk.CTk()

janela.title('Lista de Tarefas')
janela.geometry('400x350')

titulo = ctk.CTkLabel(janela, text='Tarefas:', font=('Times', 15))
titulo.pack(pady=15)

janela.mainloop()