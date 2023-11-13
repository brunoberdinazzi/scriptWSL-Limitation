import tkinter as tk
from tkinter import messagebox
import subprocess

def configurar_wsl(memoria):
    try:
        # Configura o limite de memória no sysctl.conf
        resultado = subprocess.run(["wsl", "--", "sudo", "sysctl", "-w", f'vm.max_map_count={memoria}'], check=True, capture_output=True, text=True)

        messagebox.showinfo("Configuração Concluída", "As configurações do WSL2 foram ajustadas com sucesso.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao configurar o WSL2:\n\n{e.stdout}\n\n{e.stderr}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao configurar o WSL2: {str(e)}")

def obter_memoria():
    valor = entry.get()
    try:
        memoria = int(valor)
        return memoria
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor inteiro para a memória.")
        return None

def configurar():
    memoria = obter_memoria()
    if memoria is not None:
        configurar_wsl(memoria)

# Criar a janela principal
root = tk.Tk()
root.title("Configuração WSL2")

# Criar e posicionar os elementos na janela
label = tk.Label(root, text="Insira a quantidade máxima de memória RAM para o WSL2 (em GB):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Configurar WSL2", command=configurar)
button.pack(pady=20)

# Iniciar o loop principal da interface gráfica
root.mainloop()
