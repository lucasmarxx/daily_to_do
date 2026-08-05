import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# criando a janela

janela = ctk.CTk()
ctk.set_appearance_mode('dark')

janela.title('Lista de Tarefas')
janela.geometry('650x450')

tarefas = []

def adicionar_tarefas():
    tarefa = tarefas_a_fazer.get()

    if tarefa not in tarefas:
        tarefas.append(tarefa)
        texto_tarefa_add.configure(text='Tarefa adicionada.', text_color='#005c69')
        print(tarefas)
        tarefa_adicionada = ctk.CTkLabel(master=frame_tarefas, text=tarefa)
        tarefa_adicionada.pack(pady=5, padx=5, side='left')
    else:
        texto_tarefa_add.configure(text='Tarefa existente.', text_color='red')

def remover_tarefas():
    ...

titulo = ctk.CTkLabel(janela, text='Tarefas:', font=('Times', 15, 'bold'))
titulo.pack(pady=15)

tarefas_a_fazer = ctk.CTkEntry(janela, placeholder_text='Tarefas a Fazer', font=('Times', 12))
tarefas_a_fazer.pack(pady=10)

frame_tarefas = ctk.CTkScrollableFrame(janela)
frame_tarefas.pack(pady=20, padx=20, fill = 'x', expand=True)

botao_add_tarefas = ctk.CTkButton(janela, text = 'Adicionar Tarefa', command=adicionar_tarefas)
botao_add_tarefas.pack(padx=15, pady=15, side='left')

botao_remocao_tarefas = ctk.CTkButton(janela, text='Remover Tarefa', command=remover_tarefas)
botao_remocao_tarefas.pack(padx=25, pady=25, side='right')

texto_tarefa_add = ctk.CTkLabel(janela, text='', font=('Times', 12))
texto_tarefa_add.pack(pady=5)

janela.mainloop()