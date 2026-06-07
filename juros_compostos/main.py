import math

inicial = 0
taxa = 0
tempo = 0
aporte_mensal = 0

while inicial <= 0:
    inicial = int(input("Digite o valor inicial: "))
    if inicial <= 0:
        print("O valor inicial não pode ser menor ou igual a zero.")

while aporte_mensal <= 0:
    aporte_mensal = int(input("Digite o aporte mensal: "))
    if aporte_mensal <= 0:
        print("O aporte mensal não pode ser menor ou igual a zero.")

while taxa <= 0:
    taxa = float(input("Digite a taxa de juros anual: "))
    if taxa <= 0:
        print("A taxa de juros não pode ser menor ou igual a zero.")

while tempo <= 0:
    tempo = int(input("Digite o tempo(em anos): "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual à zero.")

tempo_meses = tempo * 12
taxa_mensal = (taxa / 100) / 12

saldo_atual = inicial

for mes in range(1, tempo_meses +1):

    saldo_atual = saldo_atual * (1 + taxa_mensal)
    saldo_atual = saldo_atual + aporte_mensal

total_investido = inicial + (aporte_mensal * tempo_meses)
total_juros = saldo_atual - total_investido

print("\n" + "="*30)
print(f"RESULTADO APÓS {tempo} ANOS:")
print(f"Total acumulado: R$ {saldo_atual:.2f}")
print(f"Total investido por você: R$ {total_investido:.2f}")
print(f"Total ganho em juros: R$ {total_juros:.2f}")
print("="*30)