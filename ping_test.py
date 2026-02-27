import os

host = input("Digite o host para testar: ")

print(f"\nTestando conexão com {host}...\n")

response = os.system(f"ping -n 4 {host}")

if response == 0:
    print("\nConectividade OK ✅")
else:
    print("\nFalha de conexão ❌")