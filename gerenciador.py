import sys
import tkinter as gerenciador
import random
import string
#import pyperclip
## 1) Salvar as senhas em um arquivo

def salvarSenha (apelido, senha):
  file = open ("senhas.txt", "a+")
  file.write (apelido)
  file.write ("\n")
  file.write (senha)
  file.write ("\n")
  file.close()

def contarSenhas ():
  file = open ("senha.txt", "r")
  for line in file:
    count =+ 1
  return count/2

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
"Copiar senha salva para clipboard"
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
#    labelTest.configure(text="The selected item is {}".format(variable.get()))
    
    if (variable.get() == "Gerar Senha Aleatoria"):
      senhaNova = gerarSenhaAleatoria ()
      labelTest.configure(text=senhaNova)
      app.clipboard_clear()
      # text to clipboard
      app.clipboard_append(senhaNova)
      # text from clipboard
      clip_text = app.clipboard_get()

    elif (variable.get() == "Salvar Senha Nova"):
      gerenciador.Label(app, 
         text="Apelido").grid(row=0)
      gerenciador.Label(app, 
         text="Senha").grid(row=1)

      entry1 = gerenciador.Entry (app)     
      entry2 = gerenciador.Entry (app)
      tk.Button(master, text='Enviar', command=show_entry_fields).grid(
        row=3, column=0, sticky=tk.W, pady=4)

    elif (variable.get() == "Copiar senha salva para clipboard"):
      start (4)


def start(number):
  buttons = []
  win = gerenciador.Tk()
  for i in range(number):
    b = gerenciador.Button(win, height=1, width=10, command=lambda i=i: onClick(i))
    b.pack()
    buttons.append(b)   

variable.trace("w", callback)

app.mainloop()



## 5) Encriptar as senhas
