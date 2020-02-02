import sys
import tkinter as gerenciador
import random
import string
#import pyperclip
## 1) Salvar as senhas em um arquivo

def salvarSenha (senha):
  file = open ("senhas.txt", "a+")
  file.write (senha)
  file.write ("\n")
  file.close()

#TESTE: 
#senha1 = "mari"
#senha2 = "kay"
#salvarSenha (senha1)
#salvarSenha (senha2)


## 2) Gerar senhas

def gerarSenhaAleatoria (stringLength=10):
#Generate a random string of letters, digits and special characters
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

#print ("First Random String ", gerarSenhaAleatoria() )
#print (" Random String ", gerarSenhaAleatoria(5) )
##print (" Random String ", gerarSenhaAleatoria(14) )

## 3) Copiar senhas para o clipboard

senha = gerarSenhaAleatoria()

def copiarClipboard (senha):
  pyperclip.copy(senha)
  pyperclip.paste()

#copiarClipboard (senha)

## 4) Menu para selecionar opcoes

OptionList = [
"Selecione um opcao",
"Salvar senha nova",
"Gerar Senha Aleatoria",
"Copiar senha para clipboard"
] 

app = gerenciador.Tk()

app.geometry('300x200')

variable = gerenciador.StringVar(app)
variable.set(OptionList[0])

opt = gerenciador.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")

labelTest = gerenciador.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))

variable.trace("w", callback)

app.mainloop()



## 5) Encriptar as senhas
