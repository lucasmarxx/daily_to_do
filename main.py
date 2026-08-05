import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# criando a janela

janela = ctk.CTk()

janela.title('Lista de Tarefas')
janela.geometry('400x350')

tarefas = []

def adicionar_tarefas():
    tarefa = tarefas_a_fazer.get()

    if tarefa:
        tarefas.append(tarefa)
        texto_tarefa_add.configure(text='Tarefa adicionada.')
        print(tarefas)

titulo = ctk.CTkLabel(janela, text='Tarefas:', font=('Times', 15, 'bold'))
titulo.pack(pady=15)

tarefas_a_fazer = ctk.CTkEntry(janela, placeholder_text='Tarefas a Fazer', font=('Times', 12))
tarefas_a_fazer.pack(pady=10)

# CTkMessagebox(title = 'Teste da message box', message= 'testee')


# def abrir_dialogo():
#     texto = ctk.CTkInputDialog(text='Digite uma tarefa: ', title='Tarefas')
#     user = texto.get_input()
#     if user:
#         print('entrou!', user)

botao = ctk.CTkButton(janela, text = 'Adicionar Tarefa', command=adicionar_tarefas)
botao.pack(padx=15, pady=15)

texto_tarefa_add = ctk.CTkLabel(janela, text='', font=('Times', 12))
texto_tarefa_add.pack(pady=5)

janela.mainloop()