from tkinter import *
from tkinter import ttk

# cores

cor0 = "#3b3b3b" #preta
cor1 = "#feffff" #branca
cor2 = "#38576b" #azul forte
cor3 = "#ECEFF1" #Cinza
cor4 = "#FFAB40" #Laranja

# Criando a janela, dimensão, titulo e cor de fundo
janela = Tk()
janela.title("Calculadora")
janela.geometry("233x310")
janela.config(bg=cor0)

# Criando os frames
frame_tela = Frame(janela, width=235, height=60, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=300)
frame_corpo.grid(row=1, column=0)

# Variavel que recebe todos valores

data_Value = ''

# Criando função que recebe os dados

def inputData(event):

    global data_Value

    data_Value = data_Value + str(event)

    #Passando o valor para tela
    valorTexto.set(data_Value)

# Função para calcular

def calcular(event):
    
    resultado = eval(event)
    valorTexto.set(resultado)

# Função para limpar os dados

def limparDados():
    global data_Value
    data_Value = ''
    valorTexto.set('')
    
# Criando label
valorTexto = StringVar()

app_label = Label(frame_tela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT,anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor1)
app_label.place(x=0, y=0)

# Criando botões
#linha 0
b_1 = Button(frame_corpo, command=lambda:limparDados(),text="C", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda:inputData('%'), text="%", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda:inputData('/'), text="/", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#linha 1
b_5 = Button(frame_corpo, command=lambda:inputData('7'), text="7", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=52)
b_6 = Button(frame_corpo, command=lambda:inputData('8'), text="8", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=59, y=52)
b_7 = Button(frame_corpo, command=lambda:inputData('9'), text="9", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=52)
b_8 = Button(frame_corpo, command=lambda:inputData('*'), text="*", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=177, y=52)

#linha 2

b_9 = Button(frame_corpo, command=lambda:inputData('4'), text="4", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=104)
b_10 = Button(frame_corpo, command=lambda:inputData('5'), text="5", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=59, y=104)
b_11 = Button(frame_corpo, command=lambda:inputData('6'), text="6", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=118, y=104)
b_12 = Button(frame_corpo, command=lambda:inputData('-'), text="-", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=177, y=104)

#linha 3

b_13 = Button(frame_corpo, command=lambda:inputData('1'), text="1", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=156)
b_14 = Button(frame_corpo, command=lambda:inputData('2'), text="2", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=59, y=156)
b_15 = Button(frame_corpo, command=lambda:inputData('3'), text="3", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=118, y=156)
b_16 = Button(frame_corpo, command=lambda:inputData('+'), text="+", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=177, y=156)

#linha 4

b_1 = Button(frame_corpo, command=lambda:inputData('0'), text="0", width=11, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=204)
b_2 = Button(frame_corpo, command=lambda:inputData('.'), text=".", width=5, height=2, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=204)
b_3 = Button(frame_corpo, command=lambda:calcular(data_Value), text="=", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=204)


janela.mainloop()
