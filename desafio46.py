
def selecao (seletor):
    if(seletor == 1):
        lista("Placa Mãe", "CPU", "VGA", "Memoria RAM")
        
        r = int(input("Quais itens deseja ver ? \nSelecione o operador correspondente: "))
        listapecas (r)
    elif(seletor == 2):
         calculo()
    else:
        ("Operador errado!")

def listapecas (r):
     
      if(r == 1):
         lista1("\n1- B550M; \n2- A520M; \n3- H610M;")
      elif(r == 2):
          lista2("\n1- Ryzen 5 9600X; \n2- i5-12400F; \n3- Ryzen 7 5700X; \n4- i7-14700K; ")
      elif(r == 3):
          lista3("\n1- RX 6600; \n2- RX 7900 XT; \n3- RTX 4060 ; \n4- RTX 4090; ")
      elif(r == 4):
          lista4("\n1- 8GB 3200MHZ; \n2- 16GB 3200MHZ;")
      else:
          print("Erro no operador!")


def lista1 (*mae):
     print ("------------------------")
     for x in range(len(mae)): 
         print(f"Item: {mae[x]}")
         print ("------------------------")
         

def lista2 (*cpu):
     print ("------------------------")
     for x in range(len(cpu)): 
         print(f"Item: {cpu[x]}")
         print ("------------------------")

def lista3 (*vga):
     print ("------------------------")
     for x in range(len(vga)): 
         print(f"Item: {vga[x]}")
         print ("------------------------")

def lista4 (*ram):
     print ("------------------------")
     for x in range(len(ram)): 
         print(f"Item: {ram[x]}")
         print ("------------------------")



def lista (*itens):
     print ("------------------------")
     for x in range(len(itens)): 
         print(f"{x+1} - Item: {itens[x]}")
         print ("------------------------")


def calculo ():
    n1 = int(input("Digite a quantidade de quadros: "))
    n2 = int(input("Digite a quantidade de segundos: "))
    print ("------------------------")
    print(f"Seu FPS é de: {n1/n2:.2f}")
    print ("------------------------")


def entrada (): 
     seletor = int(input("Oque deseja ver/fazer ? \n1- Lista de itens \n2- Calcular taxa de FPS \nDigite o operador correspondente: "))
     selecao(seletor)
entrada()

def main ():
     rep = 1

     while(rep == 1):
          rep = int(input(f"Deseja voltar ao menu ? \n1-Sim; \n2-Não; "))
          print ("------------------------")
          if rep == 2:
              break
              
     
          entrada()
main()







