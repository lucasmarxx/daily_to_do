import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# criando a janela

janela = ctk.CTk()

janela.title('Lista de Tarefas')
janela.geometry('400x350')

tarefas = []


titulo = ctk.CTkLabel(janela, text='Tarefas:', font=('Times', 15, 'bold'))
titulo.pack(pady=15)

# CTkMessagebox(title = 'Teste da message box', message= 'testee')


def abrir_dialogo():
    texto = ctk.CTkInputDialog(text='Digite uma tarefa: ', title='Tarefas')
    user = texto.get_input()
    if user:
        print('entrou!', user)

botao = ctk.CTkButton(janela, text = 'abrir dialogo', command=abrir_dialogo)
botao.pack(padx=15, pady=50)

janela.mainloop()