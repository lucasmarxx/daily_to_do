import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# criando a janela

janela = ctk.CTk()
ctk.set_appearance_mode('dark')

janela.title('Lista de Tarefas')
janela.geometry('650x550')

tarefas = []
lista_de_labels = []

def adicionar_tarefas():
    tarefa = tarefas_a_fazer.get()

    if tarefa not in tarefas:
        tarefas.append(tarefa)
        texto_tarefa.configure(text='Tarefa adicionada.', text_color='#005c69')
        print(tarefas)
        tarefa_adicionada = ctk.CTkLabel(master=frame_tarefas, text=tarefa.capitalize())
        lista_de_labels.append(tarefa_adicionada)
        tarefa_adicionada.pack(pady=5, padx=5, side='left')
        tarefas_a_fazer.delete(0, 'end')
    else:
        texto_tarefa.configure(text='Tarefa existente.', text_color='red')

def remover_tarefas():
    tarefa = tarefas_a_remover.get()

    if tarefa in tarefas:
        tarefas.remove(tarefa)
        

        for label in lista_de_labels:
            if label.cget('text') == tarefa.capitalize():
                label.destroy()
                lista_de_labels.remove(label)
                break

    
        texto_tarefa.configure(text='Tarefa removida!', text_color='green')
        print(tarefas)
        tarefas_a_remover.delete(0, 'end')
    else:
        texto_tarefa.configure(text='tarefa não encontrada!', text_color='red')

titulo = ctk.CTkLabel(janela, text='Tarefas:', font=('Arial', 20, 'bold'))
titulo.pack(pady=15)

tarefas_a_fazer = ctk.CTkEntry(janela, placeholder_text='Tarefas a Fazer',width=190, font=('Arial', 20),text_color='white')
tarefas_a_fazer.pack(pady=10)

tarefas_a_remover = ctk.CTkEntry(janela, placeholder_text='Tarefas a Remover', width=190, font=('Arial', 20,), text_color='red')
tarefas_a_remover.pack(padx=20)

frame_tarefas = ctk.CTkScrollableFrame(janela)
frame_tarefas.pack(pady=20, padx=20, fill = 'x', expand=True)

botao_add_tarefas = ctk.CTkButton(janela, text = 'Adicionar Tarefa', command=adicionar_tarefas)
botao_add_tarefas.pack(padx=15, pady=15, side='left')

botao_remocao_tarefas = ctk.CTkButton(janela, text='Remover Tarefa', command=remover_tarefas)
botao_remocao_tarefas.pack(padx=25, pady=25, side='right')

texto_tarefa = ctk.CTkLabel(janela, text='', font=('Times', 12))
texto_tarefa.pack(pady=5)

janela.mainloop()