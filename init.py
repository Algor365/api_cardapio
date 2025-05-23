from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def carregar_db():
    with open('db.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def formatar_resposta(lista, titulo):
    resposta = f"{titulo}:\n\n"
    for item in lista:
        nome = item['nome']
        preco = f"R${item['preco']:.2f}".replace('.', ',')
        resposta += f"{nome}: {preco}\n"
    return resposta

@app.route('/')
def esfihas():
    db=carregar_db()
    return jsonify(db)

@app.route('/esfihas/salgada')
def esfihas_salgadas():
    db = carregar_db()
    esfihas = db['esfihas_salgadas']
    nome_param = request.args.get('nome')

    if nome_param:
        nome_param = nome_param.lower()
        filtradas = [e for e in esfihas if nome_param in e['nome'].lower()]
        if not filtradas:
            return "Nenhuma esfiha salgada encontrada.", 404
        return formatar_resposta(filtradas, "Esfihas Salgadas"), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    return jsonify(esfihas)

@app.route('/esfihas/doce')
def esfihas_doces():
    db = carregar_db()
    doces = db['esfihas_doces']
    nome_param = request.args.get('nome')

    if nome_param:
        nome_param = nome_param.lower()
        filtradas = [d for d in doces if nome_param in d['nome'].lower()]
        if not filtradas:
            return "Nenhuma esfiha doce encontrada.", 404
        return formatar_resposta(filtradas, "Esfihas Doces"), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    return jsonify(doces)

@app.route('/salgados')
def salgados():
    db = carregar_db()
    salgados = db['salgados']
    nome_param = request.args.get('nome')

    if nome_param:
        nome_param = nome_param.lower()
        filtradas = [s for s in salgados if nome_param in s['nome'].lower()]
        if not filtradas:
            return "Nenhum salgado encontrado.", 404
        return formatar_resposta(filtradas, "Salgados"), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    return jsonify(salgados)

@app.route('/bebidas')
def bebidas():
    db = carregar_db()
    bebidas = db['bebidas']
    nome_param = request.args.get('nome')

    if nome_param:
        nome_param = nome_param.lower()
        filtradas = [b for b in bebidas if nome_param in b['nome'].lower()]
        if not filtradas:
            return "Nenhuma bebida encontrada.", 404
        return formatar_resposta(filtradas, "Bebidas"), 200, {'Content-Type': 'text/plain; charset=utf-8'}

    return jsonify(bebidas)
