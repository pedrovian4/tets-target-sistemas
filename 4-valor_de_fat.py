from functools import reduce


faturamentos=[{"estado":"SP", "faturamento":67836.43},{"estado":"RJ", "faturamento":36678.66},{"estado":"MG", "faturamento":29229.88},
{"estado":"ES", "faturamento":27165.48}, {"estado":"outros", "faturamento":19849.53}]


soma = 0
for faturamento in faturamentos: 
    soma+=faturamento["faturamento"]

print(f"A soma total dos faturamentos é {soma}\n que corresponde a 100% do faturamento")

for faturamento in faturamentos: 
    print("\n{estado} em relação a esse percentual teve um faturamento de {fat:.2f}%".format(estado=(faturamento["estado"]),fat=(faturamento["faturamento"]*100/soma)))
