import math
# nome='Marcelo'

# print(type(nome))

# print(nome.split("r")) # O que vem antes e o que vem depois

# numero1 = int(input("Digite o primeiro numero: "))
# numero2 = int(input("Digite o segundo numero: "))

# divisao = numero1 // numero2

# print (f"O resultado é: {divisao}")

# raio = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio ** 2
# print(f"{area_do_circulo:.2f}")

try:
    numero_01 = int(input("Digite o primeiro numero: "))
    numero_02 = int(input("Digite o segundo numero: "))
    resultado = numero_01/numero_02
    print("resultado")
except TypeError as e:
    print(e)
else:
    print("deu certo")
finally:
    print("independente do que acontecer sempre vou aparecer, esse é o finally")

#