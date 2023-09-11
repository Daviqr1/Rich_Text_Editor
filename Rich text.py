import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import filedialog



#rich text editor

root = Tk()
root.title('Rich Text Editor')
def aplicar_formatacao(formatacao):
    selecao = text_widget.tag_ranges(tk.SEL)
    if selecao:
        text_widget.tag_add(formatacao, selecao[0], selecao[1])
    else:
        cursor_pos = text_widget.index(tk.INSERT)
        text_widget.tag_add(formatacao, cursor_pos)

        import tkinter as tk
from tkinter import filedialog

def aplicar_formatacao(formatacao, text_widget):
    selecao = text_widget.tag_ranges(tk.SEL)
    if selecao:
        text_widget.tag_add(formatacao, selecao[0], selecao[1])
    else:
        cursor_pos = text_widget.index(tk.INSERT)
        text_widget.tag_add(formatacao, cursor_pos)

def abrir_arquivo():
    try:
        arquivo = filedialog.askopenfilename(title='Abrir arquivo', filetypes=(('Arquivos de texto', '*.txt'),))
        
        if arquivo:
            with open(arquivo, 'r') as f:
                conteudo = f.read()
            text_widget.delete('1.0', tk.END)  # Limpa o texto atual
            text_widget.insert('1.0', conteudo)  # Insere o conteúdo do arquivo
        else:
            print("Nenhum arquivo selecionado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {str(e)}")


def escolher_cor():
    cor = colorchooser.askcolor(title='Escolha uma cor')
    if cor:
        cor_hex, cor_rgb = cor
        text_widget.tag_config('cor', foreground=cor_hex)
        aplicar_formatacao('cor')

#definindo a janela da aplicacao e criando a área de texto
root = tk.Tk()
root.title('Rich Text Editor')
root.geometry('800x600')

text_widget = tk.Text(root)
text_widget.pack(fill=tk.BOTH, expand=True)

#criacao dos botoes
negrito_button = tk.Button(root, text='Negrito', command=lambda: aplicar_formatacao('negrito'))
italico_button = tk.Button(root, text='Itálico', command=lambda: aplicar_formatacao('italico'))
sublinhado_button = tk.Button(root, text='Sublinhado', command=lambda: aplicar_formatacao('sublinhado'))
cor_button = tk.Button(root, text='Cor', command=escolher_cor)


#posicionamento dos botões
negrito_button.pack(side=tk.LEFT, padx=5, pady=5)
italico_button.pack(side=tk.LEFT, padx=5, pady=5)
sublinhado_button.pack(side=tk.LEFT, padx=5, pady=5)
cor_button.pack(side=tk.LEFT, padx=5, pady=5)

#funcoes para abrir e salvar arquivos
def abrir_arquivo():
    arquivo = filedialog.askopenfilename(title='Abrir arquivo', filetypes=(('Arquivos de texto', '*.txt'),))
    if arquivo:
        text_widget.delete(1.0, tk.END)
        with open(arquivo, 'r') as f:
            text_widget.insert(1.0, f.read())
    else:
        return None


#criando o menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#criando o menu arquivo
arquivo_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Arquivo', menu=arquivo_menu)
arquivo_menu.add_command(label='Novo')
arquivo_menu.add_command(label='Abrir')
arquivo_menu.add_command(label='Salvar')
arquivo_menu.add_command(label='Salvar como')
arquivo_menu.add_separator()
arquivo_menu.add_command(label='Sair', command=root.quit)



#criando tags para formatacao
negrito_button = tk.Button(root, text='Negrito', command=lambda: aplicar_formatacao('negrito', text_widget))
italico_button = tk.Button(root, text='Itálico', command=lambda: aplicar_formatacao('italico', text_widget))
sublinhado_button = tk.Button(root, text='Sublinhado', command=lambda: aplicar_formatacao('sublinhado', text_widget))


root.mainloop()



