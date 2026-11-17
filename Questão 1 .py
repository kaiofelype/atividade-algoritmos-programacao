# Algoritmos e Programação
# Questão 1: Leitura de notas

notas = []
for i in range(6): 
    while True: 
        try: 
            nota = float(input(f"Digite a nota do aluno {i+1} (0.0 a 10.0): "))
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
                break
            else:
                print("Nota inválida! A nota deve ser entre 0.0 e 10.0")
        except ValueError:
            print("Entrada inválida! Digite um número real válido.")

print("Notas armazenadas:", notas)
for i in range(6):
    print(f"Aluno {i + 1}: {notas[i]:.1f}")

# Cálculo da média
media = sum(notas) / 6
acima_media = 0

print(f"\nMédia geral da turma: {media:.2f}")
print("\nNotas abaixo da média:")

for nota in notas:
    if nota >= media:
        acima_media += 1
    else:
        print(f"{nota:.1f}")

print(f"Alunos acima ou na média: {acima_media}")

# Recuperação dos alunos
for i in range(6):
    if notas[i] < media:
        print(f"\nAluno {i + 1} ficou abaixo da média.")

        while True:
            try:
                nota_recuperacao = float(
                    input("Digite a nota da recuperação: ")
                )

                if 0 <= nota_recuperacao <= 10:
                    break
                else:
                    print("Nota inválida! Digite entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")

        if nota_recuperacao > notas[i]:
            notas[i] = nota_recuperacao

# Resultado final
print("\nNotas após a recuperação:")
print("Vetor notas atualizado:", notas)
for i in range(6):
    print(f"Aluno {i + 1}: {notas[i]:.1f}")

nova_media = sum(notas) / 6
print(f"\nNova média geral: {nova_media:.2f}")
