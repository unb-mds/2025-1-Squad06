#Foi adicionado criptografia e correção de contagem de votação
'''Como Funciona?
Agora, quando um usuário envia um voto, o sistema cria um hash do seu user_id e o armazena. 
Isso impede que o mesmo usuário vote mais de uma vez, mas sem armazenar o ID real, garantindo anonimato.
Como o hash é irreversível, mesmo que você tenha acesso ao banco de dados, não será possível determinar qual usuário votou.
'''

import json
import socket
import os
import hashlib  # Importação para funções de hash, usada para anonimizar IDs de usuários (criptografia)
from flask import Flask, render_template, request, jsonify

# Configurações do servidor
HOST = '127.0.0.1'
UDP_PORT = 5005
HTTP_PORT = 8000
resultados_file = 'resultados.json'

# Estruturas de dados
votos = {'a_favor': 0, 'contra': 0, 'abstencao': 0}
perguntas = []
votantes = set()  # Para armazenar os hashes dos IDs dos votantes

# Função para salvar os resultados no arquivo JSON
def salvar_resultados():
    with open(resultados_file, 'w') as f:
        json.dump({'perguntas': perguntas}, f, indent=4)

# Carregar resultados do arquivo
def carregar_resultados():
    if os.path.exists(resultados_file):
        with open(resultados_file, 'r') as f:
            data = json.load(f)
            return data.get('perguntas', [])
    return []

# Carregar perguntas
perguntas = carregar_resultados()

# Função para gerar um hash do ID do usuário (para garantir anonimato)
def gerar_hash_id(user_id):
    return hashlib.sha256(user_id.encode()).hexdigest()

# Criando o app Flask
app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template('interface.html')

# Rota para obter os resultados
@app.route('/results', methods=['GET'])
def get_results():
    return jsonify({'perguntas': perguntas})

# Rota para definir uma nova questão
@app.route('/question', methods=['POST'])
def set_question():
    data = request.json
    question = data.get('question')
    if question:
        nova_pergunta = {
            'question': question,
            'results': votos.copy()
        }
        perguntas.append(nova_pergunta)
        salvar_resultados()
        return jsonify({'message': 'Nova questão definida com sucesso!'})
    return jsonify({'error': 'Questão inválida.'}), 400

# Rota para registrar um voto
@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    user_id = data.get('user_id')
    vote = data.get('vote')

    # Gerar hash do ID do usuário para anonimizar
    user_hash = gerar_hash_id(user_id) #criptografia SHA-256

    if user_hash in votantes:
        return jsonify({'error': 'Você já votou.'}), 400

    if vote in votos:
        votos[vote] += 1
        votantes.add(user_hash)  # Registrar que o usuário votou

        # Atualiza os resultados da última pergunta
        if perguntas:
            pergunta_atual = perguntas[-1]
            pergunta_atual['results'] = votos.copy()
            salvar_resultados()

        return jsonify({'message': 'Voto registrado com sucesso!'})
    return jsonify({'error': 'Opção de voto inválida.'}), 400

# Iniciar o servidor HTTP
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=HTTP_PORT)
