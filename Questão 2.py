# Algoritmos e Programação
# Questão 2: Registro de temperaturas semanais

dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado"]
temperaturas = []

for i in range(7):
    while True:
        try:
            temperatura = float(input(f"Digite a temperatura de {dias[i]} (-10.0 a 50.0 °C): "))
            if -10.0 <= temperatura <= 50.0:
                temperaturas.append(temperatura)
                break
            else:
                print("Temperatura inválida! Digite entre -10.0 e 50.0 °C.")
        except ValueError:
            print("Entrada inválida! Digite um número real válido.")

print("\nTemperaturas registradas:")
for i in range(7):
    print(f"Índice {i} - {dias[i]}: {temperaturas[i]:.1f} °C")

# Análise climática e alertas
maior_temperatura = temperaturas[0]
menor_temperatura = temperaturas[0]
indice_maior = 0
alertas_calor = 0

for i in range(7):
    if temperaturas[i] > maior_temperatura:
        maior_temperatura = temperaturas[i]
        indice_maior = i

    if temperaturas[i] < menor_temperatura:
        menor_temperatura = temperaturas[i]

    if temperaturas[i] > 32.0:
        alertas_calor += 1

print(f"\nMaior temperatura: {maior_temperatura:.1f} °C")
print(f"Menor temperatura: {menor_temperatura:.1f} °C")
print(f"Dias com Alerta de Calor: {alertas_calor}")
print(f"Dia da maior temperatura: índice {indice_maior} - {dias[indice_maior]}")

# Simulação de frente fria e reajuste
for i in range(7):
    if temperaturas[i] > 30.0:
        temperaturas[i] -= 4.5

        if temperaturas[i] < 15.0:
            temperaturas[i] = 15.0

# Resultado final
print("\nVetor temperaturas após a frente fria:", temperaturas)
for i in range(7):
    print(f"Índice {i} - {dias[i]}: {temperaturas[i]:.1f} °C")

nova_media = sum(temperaturas) / 7
print(f"\nNova média de temperatura da semana: {nova_media:.2f} °C")
