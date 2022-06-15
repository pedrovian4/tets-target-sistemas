from json import loads
from functools import reduce


with open('data\dados.json', 'r') as d:
    dados = loads(d.read())





def menor_valor():
    menor_valor=1000000000000
    valores_dia_zero=[]
    dia = None
    #desconsiderando valores zerados
    for dado in dados: 
        if dado["valor"]!=0:
            if dado["valor"]<menor_valor:
                menor_valor= dado["valor"]
                dia= dado["dia"]
        else:
            valores_dia_zero.append("dia: {dia} ,valor:{valor}\n".format(dia=dado["dia"], valor=dado["valor"]))
    print(f'\n\n!Desconsiderando os valores zerados!\n\n\no menor valor é: {menor_valor}\naconteceu no dia: {dia}\n')
    valores_dia_zero= ''.join(valores_dia_zero)
    print(f'Os dias que deram os valores zerados (consequente os menores valores) são:\n\n{valores_dia_zero } ')


def d_media(): 
    filtrar_zeros = [dado["valor"] for index,dado in enumerate(dados) if dados[index]["valor"]!=0]
    media = sum(filtrar_zeros)/len(filtrar_zeros)
    c= 0
    dados_dias_maior =[]
    for dado in dados: 
        if dado["valor"]>media:
            dados_dias_maior.append("dia: {dia}, valor: {valor}\n".format(dia=dado["dia"],valor=dado["valor"]))
            c+=1
    dados_dias_maior=''.join(dados_dias_maior)
    print(f'\n\nA média é de lucro é {media}\n')
    print(f" O número de dias que os valores de faturamento foram maiores que a média mensal é um total de: {c}\n\n")
    print(f"Esses dias foram {dados_dias_maior}\n")


mv = reduce(lambda a, b: a if a["valor"] > b["valor"] else b,dados )


if __name__ == "__main__": 
    menor_valor()
    print("\n\no maior valor é: {valor}\naconteceu no dia: {dia}".format(valor=mv["valor"], dia=mv["dia"]))
    d_media()