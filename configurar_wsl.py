import os
import tkinter as tk
from tkinter import messagebox

def configurar_wsl(diretorio, memoria, processadores):
    try:
        caminho_wslconfig = os.path.join(diretorio, ".wslconfig")
        conteudo = f"[wsl2]\nmemory={memoria}\nprocessors={processadores}"
        with open(caminho_wslconfig, "w") as arquivo:
            arquivo.write(conteudo)
        messagebox.showinfo("Configuração Concluída", "As configurações do WSL2 foram ajustadas com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao configurar o WSL2: {str(e)}")

def obter_diretorio():
    diretorio = entry_diretorio.get()
    return diretorio

def obter_memoria():
    valor = entry_memoria.get()
    try:
        memoria = int(valor)
        return memoria
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor inteiro para a memória.")
        return None

def obter_processadores():
    valor = entry_processadores.get()
    try:
        processadores = int(valor)
        return processadores
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor inteiro para o número de processadores.")
        return None

def configurar():
    diretorio = obter_diretorio()
    memoria = obter_memoria()
    processadores = obter_processadores()

    if diretorio and memoria is not None and processadores is not None:
        configurar_wsl(diretorio, memoria, processadores)

root = tk.Tk()
root.title("Configuração WSL2")

label_diretorio = tk.Label(root, text="Insira o diretório onde deseja criar o arquivo .wslconfig:")
label_diretorio.pack(pady=10)

entry_diretorio = tk.Entry(root)
entry_diretorio.pack(pady=10)

label_memoria = tk.Label(root, text="Insira a quantidade máxima de memória RAM para o WSL2:")
label_memoria.pack(pady=10)

entry_memoria = tk.Entry(root)
entry_memoria.pack(pady=10)

label_processadores = tk.Label(root, text="Insira o número de processadores para o WSL2:")
label_processadores.pack(pady=10)

entry_processadores = tk.Entry(root)
entry_processadores.pack(pady=10)

button = tk.Button(root, text="Configurar WSL2", command=configurar)
button.pack(pady=20)

root.mainloop()
