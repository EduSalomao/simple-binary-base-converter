import tkinter as tk

def definir_opcao():
    opcao_selecionada = var_opcao.get()

    if opcao_selecionada == "Binário p/ decimal":
        num2.config(state=tk.DISABLED)
        num.config(state=tk.NORMAL)
        num.delete(0, tk.END)
        num2.delete(0, tk.END)

    if opcao_selecionada == "Decimal p/ binário":
        num.config(state=tk.DISABLED)
        num2.config(state=tk.NORMAL)
        num.delete(0, tk.END)
        num2.delete(0, tk.END)

    if opcao_selecionada is None:
        num.config(state=tk.DISABLED)
        num2.config(state=tk.DISABLED)
        
def converter():
    i = 0
    soma = 0

    if var_opcao.get() == "Binário p/ decimal":
        valor = num.get()
        if not valor.isdigit() or any(
                int(digito) not in [0, 1] for digito in valor):
            errorwindow = tk.Toplevel(janela)
            errorwindow.grab_set()
            errorwindow.title("Erro")
            errormessage = tk.Label(errorwindow, text="O VALOR INSERIDO É INVÁLIDO")
            errormessage.pack(padx=10, pady=10)
            botao_ok = tk.Button(errorwindow, text="OK", command=errorwindow.destroy)
            botao_ok.pack(pady=0)
            return
        reversenum = str(valor)[::-1]
        numberlist = list(reversenum)

        for x in numberlist:
            soma += (int(x) * (2 ** i))
            i += 1

    else: 
        valor = num2.get()
        if not valor.isdigit():
            errorwindow = tk.Toplevel(janela)
            errorwindow.grab_set()
            errorwindow.title("Erro")
            errormessage = tk.Label(errorwindow, text="O VALOR INSERIDO É INVÁLIDO")
            errormessage.pack(padx=10, pady=10)
            botao_ok = tk.Button(errorwindow, text="OK", command=errorwindow.destroy)
            botao_ok.pack(pady=0)
            return
        valor = int(valor)
        valor = bin(valor)[2:]

    if var_opcao.get() == "Binário p/ decimal":
        num2.config(state=tk.NORMAL)
        num2.delete(0, tk.END)
        num2.insert(0, str(soma))
        num2.config(state=tk.DISABLED)

    if var_opcao.get() == "Decimal p/ binário":
        num.config(state=tk.NORMAL)
        num.delete(0, tk.END)
        num.insert(0, str(valor))
        num.config(state=tk.DISABLED)


janela = tk.Tk()
janela.title("Conversor")

opcoes = ["Binário p/ decimal", "Decimal p/ binário"]

var_opcao = tk.StringVar()
var_opcao.set(None)

containertitle = tk.Frame(janela)
containertitle.grid(row=0, column=0)

titulo = tk.Label(containertitle, text="CONVERSOR")
titulo.pack(padx=5, pady=3)

containeropcoes = tk.Frame(janela)
containeropcoes.grid(row=1, column=0)

for i, opcao in enumerate(opcoes):
    botao_opcao = tk.Radiobutton(containeropcoes, text=opcao, variable=var_opcao, value=opcao, command=definir_opcao)
    botao_opcao.grid(row=0, column=i, padx=2, pady=0)

container = tk.Frame(janela)
container.grid(row=3, column=0, padx=5, pady=0)

rotulobin = tk.Label(container, text="BINÁRIO: ")
rotulobin.grid(row=0, column=0, pady=5)
num = tk.Entry(container)
num.grid(row=0, column=1, padx=6, pady=5, sticky="ew")

rotulodec = tk.Label(container, text="DECIMAL: ")
rotulodec.grid(row=1, column=0, pady=5)
num2 = tk.Entry(container)
num2.grid(row=1, column=1, padx=6, pady=5, sticky="ew")

botao = tk.Button(container, text="CONVERTER", command=converter)
botao.grid(row=2, column=0, columnspan=2, pady=0, sticky="nsew")

rotulo_resultado = tk.Label(container, text="")
rotulo_resultado.grid(row=3, column=0, columnspan=2)

janela.grid_columnconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=1)

janela.mainloop()
