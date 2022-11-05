from tkinter import *
from tkinter import messagebox


def valores():
    endereco.delete(0, 'fim')
    nome.delete(0, 'fim')
    altura.delete(0, 'fim')
    peso.delete(0, 'fim')


def calcula_imc():
    kg = int(peso.get())
    m = int(altura.get()) / 100
    imc = kg / (m * m)
    imc = round(imc, 1)
    imc_taxa(imc)


def imc_taxa(imc):
    if imc < 18.5:
        messagebox.showinfo('IMC', f'imc= {imc}  Abaixo do peso')
    elif (imc > 18.5) and (imc < 24.9):
        messagebox.showinfo('IMC', f'imc = {imc} Normal')
    elif (imc > 24.9) and (imc < 29.9):
        messagebox.showinfo('IMC', f'imc = {imc} Acima do peso')
    elif imc > 29.9:
        messagebox.showinfo('IMC', f'imc = {imc}  Obesidade')
    else:
        messagebox.showerror('IMC', 'ERRO')


ws = Tk()
ws.title('Calculadora de IMC')
ws.geometry('800x700')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=200,
    pady=100
)
frame.pack(expand=True)

Nome_lb = Label(
    frame,
    text="Seu Nome"
)
Nome_lb.grid(row=1, column=1)

nome = Entry(
    frame,
)
nome.grid(row=1, column=2, pady=5)

frame.pack(expand=True)

Endere_lb = Label(
    frame,
    text="Seu Endereco"
)
Endere_lb.grid(row=2, column=1)

endereco = Entry(
    frame,
)
endereco.grid(row=2, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Qual o seu sexo ?'
)
gen_lb.grid(row=3, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=3, column=2, pady=5)

masc = Radiobutton(
    frame2,
    text='Masculino',
    variable=var,
    value=1
)
masc.pack(side=LEFT)

femi = Radiobutton(
    frame2,
    text='Feminino',
    variable=var,
    value=2
)
femi.pack(side=RIGHT)

altura_lb = Label(
    frame,
    text="Sua altura em (cm)  "
)
altura_lb.grid(row=4, column=1)

peso_lb = Label(
    frame,
    text="Seu peso em (kg)  ",

)
peso_lb.grid(row=5, column=1)

altura = Entry(
    frame,
)
altura.grid(row=4, column=2, pady=5)

peso = Entry(
    frame,
)
peso.grid(row=5, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=6, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculo',
    command=calcula_imc
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Refazer',
    command=valores
)
reset_btn.pack(side=LEFT)

sair_btn = Button(
    frame3,
    text='Saida',
    command=lambda: ws.destroy()
)
sair_btn.pack(side=RIGHT)

ws.mainloop()
