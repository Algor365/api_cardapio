
# API Cardápio - Casa de Esfiha

API para consulta de itens do cardápio de uma casa de esfiha, incluindo esfihas salgadas, doces, salgados e bebidas.

---

## Base URL

```
https://api-cardapio-f44e.onrender.com
```

---

## Endpoints

### GET `/`
Retorna **todos os itens** do cardápio.

### GET `/esfihas`
Retorna **todas as esfihas**, doces e salgadas.

### GET `/esfihas/salgadas`
Retorna **somente esfihas salgadas**.

### GET `/esfihas/doce`
Retorna **somente esfihas doces**.

### GET `/salgados`
Retorna a lista de **salgados tradicionais**, que não são esfihas.

### GET `/bebidas`
Retorna a lista de **bebidas disponíveis**.

---

## Filtro por nome

Todos os endpoints aceitam busca por nome com o parâmetro `?nome=`.

### Exemplo:
```
https://api-cardapio-f44e.onrender.com/bebidas?nome=coca-cola lata
```

> Observação: Use **underscore (`_`)** no lugar de espaços.

---

## Exemplo de resposta (JSON)

```json
[
  {
    "nome": "Esfiha de Carne",
    "valor": 4.00
  },
  {
    "nome": "Coca-Cola Lata",
    "valor": 6.00
  }
]
```

---

## Códigos de status

- `200 OK`: Requisição bem-sucedida.
- `404 Not Found`: Item não encontrado.
- `500 Internal Server Error`: Erro interno do servidor.

---

## Tecnologias utilizadas

- Python
- Flask (ou Django)
- Render (para deploy)
- JSON como formato de resposta
