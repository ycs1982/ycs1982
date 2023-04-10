salario_atual = float(input("Entre com seu salario: "))

if salario_atual <= 500:
    x = salario_atual + (salario_atual * 0.15)
    print("Seu novo salario é",x)

if salario_atual > 500 and salario_atual <= 1000:
    y = salario_atual + (salario_atual * 0.10)
    print("Seu novo salario é",y)

if salario_atual > 1000:
    z = salario_atual + (salario_atual * 0.05)
    print("Seu novo salario é",z)


