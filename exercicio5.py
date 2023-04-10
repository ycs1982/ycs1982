print("""O pagamento semanal total de um funcionário é igual ao salário por hora multiplicado
pelo número total de horas regulares mais qualquer pagamento de horas extras.
O pagamento de horas extras é igual ao total de horas extras multiplicado por 1,5 vez o salário por hora.
Escreva um programa que receba como entradas o salário por hora, o total de horas regulares e o total de
horas extras e exiba o pagamento semanal total de um funcionário.""")

print()


salario_hora = float(input("Salario por hora: "))
total_hora = float(input("Horas trabalhadas: "))
total_extra = float(input("Horas extras: "))

hora_extra = total_extra * ( 1.5 * salario_hora)

pagamento_semanal = (salario_hora*total_hora) + (hora_extra)

print(f"pagamento semanal: {pagamento_semanal}")




