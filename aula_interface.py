from tkinter import *
import random
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Tente advinhar a vogal")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()


        self.senhaLabel = Label(self.terceiroContainer, text="Vogal", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaNumero
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaNumero(self):
      tentativa = 0
      a = ["a",'e','i',"o",'u']
      j=random.choice(a)
      while tentativa <= 5:


          print("***TENTE ACERTAR O NUMERO***")

          senha = self.senha.get()
          if   j == senha:
            self.mensagem["text"] = "Correto"
            print('ok')
            break

          elif senha != j:
            self.mensagem["text"] = "Não correto"
            print('n ok,uma dica--->')
            print(j)
            break
      tentativa += 1



root = Tk()
Application(root)
root.mainloop()
