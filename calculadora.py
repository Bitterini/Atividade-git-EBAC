# calculadora.py
import tkinter as tk

def clicar(botao):
    if botao == "=":
        try:
            resultado = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, resultado)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Erro")
    elif botao == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, botao)

janela = tk.Tk()
janela.title("Calculadora")

display = tk.Entry(janela, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

linha = 1
coluna = 0
for botao in botoes:
    tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 14),
              command=lambda b=botao: clicar(b)).grid(row=linha, column=coluna, padx=2, pady=2)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

tk.Button(janela, text="C", width=22, height=2, font=("Arial", 14),
          command=lambda: clicar("C")).grid(row=linha, column=0, columnspan=4, padx=2, pady=2)

janela.mainloop()
