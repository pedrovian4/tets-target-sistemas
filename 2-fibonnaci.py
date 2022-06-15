#from functools import reduce

# fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0,1])

"""
 
    value = int(input("Insira um valor para verificar se ele esta na sequência de fibonnaci"))
    values = []
    for i in range (1, value):
        values.append(i)
    sequence = list(map(fibonacci,values))
    print(sequence)

"""



# SOLUÇÃO COM MENOS GASTO COMPUTACIONAL ENCONTRADA

def fibonacci(n): 
       return n if n<=1 else (fibonacci(n-1)) +(fibonacci(n-2))


if __name__ =="__main__":
    value = int(input("Insira um valor para verificar se ele esta na sequência de fibonnaci: "))
    for i in range(1,value):
        if (fibonacci(i)) == value:
            print(f'O número {value} está na sequência')
            break
        elif (fibonacci(i)) > value:
            print(f'O número {value} não esta na sequência')
            break
       