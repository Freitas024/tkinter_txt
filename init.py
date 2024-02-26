import tkinter as tk
from tkinter import filedialog

def salvar_arquivo():
    texto = entrada.get()
    
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'w') as arquivo:
                arquivo.write(texto)
            print(f"Texto salvo com sucesso em: {caminho_arquivo}")
        except Exception as error:
            print(f"Falha ao salvar o arquivo: {error}")


janela = tk.Tk()
janela.title("Salvar texto em arquivo.")
janela.geometry(f"{840}x{420}")
janela.configure(bg="#FFFAE3")


rotulo = tk.Label(janela, text="salvando texto.", bg="#FFFAE3", font=("Arial", 12, "bold"))
rotulo.pack()

entrada = tk.Entry(janela)
entrada.config(width=40)
entrada.pack(pady=12)

button = tk.Button(janela, text="salvar_texto", command=salvar_arquivo)
button.pack()



janela.mainloop()