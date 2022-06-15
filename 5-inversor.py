

def inversor(palavra):
    invertida= ''

    for i in reversed(range(len(palavra))):
        invertida += palavra[i]
    return invertida

if __name__ =="__main__":
    palavra = input("Insira a palavra a ser invertida: ")

    print("Palavra invertida: ",inversor(palavra))