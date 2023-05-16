import tkinter as tk


# Função da escolha de opção
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

    if opcao_selecionada is None:  # nao consegui fazer, mas, era para deixar o input de valores desativado.
        num.config(state=tk.DISABLED)
        num2.config(state=tk.DISABLED)


# Função do botão CONVERTER
def converter():
    i = 0
    soma = 0

    if var_opcao.get() == "Binário p/ decimal":
        valor = num.get()
        if not valor.isdigit() or any(
                int(digito) not in [0, 1] for digito in valor):  # Verifica se o número inserido é composto por 0 ou 1.
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

    else:  # Opção 2 selecionada
        valor = num2.get()
        if not valor.isdigit():  # Verifica se o valor inserido é um número inteiro
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
var_opcao.set(None)  # Nenhuma seleção por padrão

# CONTAINER 1
containertitle = tk.Frame(janela)
containertitle.grid(row=0, column=0)

titulo = tk.Label(containertitle, text="CONVERSOR")
titulo.pack(padx=5, pady=3)

# CONTAINER 2
containeropcoes = tk.Frame(janela)
containeropcoes.grid(row=1, column=0)

# RadioButton para escolha das opções
for i, opcao in enumerate(opcoes):
    botao_opcao = tk.Radiobutton(containeropcoes, text=opcao, variable=var_opcao, value=opcao, command=definir_opcao)
    botao_opcao.grid(row=0, column=i, padx=2, pady=0)

# CONTAINER 3
container = tk.Frame(janela)
container.grid(row=3, column=0, padx=5, pady=0)

# label e entry do número em binário
rotulobin = tk.Label(container, text="BINÁRIO: ")
rotulobin.grid(row=0, column=0, pady=5)
num = tk.Entry(container)
num.grid(row=0, column=1, padx=6, pady=5, sticky="ew")

# label e entry do número em decimal
rotulodec = tk.Label(container, text="DECIMAL: ")
rotulodec.grid(row=1, column=0, pady=5)
num2 = tk.Entry(container)
num2.grid(row=1, column=1, padx=6, pady=5, sticky="ew")

# Cria o botão para exibir os dados
botao = tk.Button(container, text="CONVERTER", command=converter)
botao.grid(row=2, column=0, columnspan=2, pady=0, sticky="nsew")

# Cria o rótulo para exibir o resultado
rotulo_resultado = tk.Label(container, text="")
rotulo_resultado.grid(row=3, column=0, columnspan=2)

# Configuração das colunas e linhas para se ajustarem automaticamente
janela.grid_columnconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=1)

janela.mainloop()
