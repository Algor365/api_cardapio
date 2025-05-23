import requests

# URL da API que você quer testar
url = 'https://api-cardapio-f44e.onrender.com'  # substitua pela rota correta

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print("Resposta JSON:")
    print(response.json())
except Exception as e:
    print(f"Erro ao consumir a API: {e}")
