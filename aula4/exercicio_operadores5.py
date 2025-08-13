salario_bruto = 2500

TAXA_IMPOSTO = 0.10
TAXA_BONUS = 0.05

salario_liquido = (salario_bruto - (salario_bruto * TAXA_IMPOSTO)) + (salario_bruto * TAXA_BONUS)
print(f"O salário líquido calculado é de R$ {salario_liquido:.2f}")

#Prova retirando os parenteses
salario_bruto = 2500

TAXA_IMPOSTO = 0.10
TAXA_BONUS = 0.05

salario_liquido = salario_bruto - salario_bruto * TAXA_IMPOSTO + salario_bruto * TAXA_BONUS
print(f"O salário líquido calculado é de R$ {salario_liquido:.2f}")