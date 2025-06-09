import sys
import requests # Mantenha esta linha para testar

print(f"Python executable being used: {sys.executable}")

try:
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    print(response.content)
except Exception as e:
    print(f"Erro ao importar ou usar requests: {e}")
