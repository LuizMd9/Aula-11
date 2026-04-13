numero = int(input("Digite o numero da tabuada"))

print("--- Tabuada do numero: {numero} ---")

for i in range(1, 10):
    print(f"{numero} x {i} = { numero * i}")
print("-- Fim da tabuada --")
