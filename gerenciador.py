import sys
import random
import string
import pyperclip
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

def menu ():
  print ("Selecione uma opcao:")
  print ()
  
  escolha = input (""" 
                      a) arquivar senha;
                      b) gerar senha aleatoria
                      c) copiar senha para o clipboard
                      d) sair do programa
                    """)
  if (escolha == "a" or escolha == "A"):
    menuSalvarSenha ()

  elif (escolha == "b" or escolha == "B"):
    menuGerarSenhaAleatoria ()

  elif (escolha == "c" or escolha == "C"):
    menuCopiarSenhaClipboard()

  elif (escolha == "d" or escolha == "D"):
    sys.exit

  else:
    print ("Selecione a, b, c ou d")
    print ("Por favor, tente novamente")
    menu ()




## 5) Encriptar as senhas
