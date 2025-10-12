
# Linux:
    # pip install pyinstaller
    # sudo apt install python3-tk -y
    # pip install --upgrade customtkinter
    # pyinstaller --onefile --noconsole --hidden-import=tkinter --hidden-import=customtkinter index.py




import customtkinter as tk
from tkinter import *

hello = """
Bem-vindo! 
Criptografe palavras ou frases utilizando criptografia simétrica.
"""

def Criptografia_cifra_cesar():
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    palavra = valorVar.get().lower()
    pulos = pulosVar.get()

    if not pulos.isdigit():
        resultado.configure(text="Erro: informe apenas números no campo de pulos.")
        return
    
    pulos1 = int(pulos)
    oq_obteve = []

    for letra in palavra:
        if letra in alfabeto:
            aux0 = alfabeto.index(letra)
            aux1 = (aux0 + pulos1) % len(alfabeto)
            aux2 = alfabeto[aux1]
            oq_obteve.append(aux2)
        else:
            oq_obteve.append(letra)  # mantém espaços e pontuação

    entradaUser = "Resultado: " + "".join(oq_obteve)
    resultado.configure(text=entradaUser)

# Configuração da janela principal
root = tk.CTk()
valorVar = tk.StringVar()
pulosVar = tk.StringVar()

root.geometry('600x350')
root.resizable(width=False, height=False)
tk.set_appearance_mode("system") 

# Frame principal
frm = tk.CTkFrame(root)
frm.pack(padx=20, pady=20, fill="both", expand=True)

# Widgets
tk.CTkLabel(frm, text=hello, font=("", 13), justify="center").grid(row=0, column=0, columnspan=2, pady=10)

tk.CTkLabel(frm, text="Digite uma palavra ou frase:").grid(row=1, column=0, sticky="e", pady=5)
tk.CTkEntry(frm, textvariable=valorVar, width=300).grid(row=1, column=1, pady=5)

tk.CTkLabel(frm, text="Quantidade de pulos:").grid(row=2, column=0, sticky="e", pady=5)
tk.CTkEntry(frm, textvariable=pulosVar, width=100).grid(row=2, column=1, sticky="w", pady=5)

tk.CTkButton(frm, text="Criptografar", command=Criptografia_cifra_cesar).grid(row=3, column=0, columnspan=2, pady=10)
resultado = tk.CTkLabel(frm, text="", font=("", 12))
resultado.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
