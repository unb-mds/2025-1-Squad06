# Pesquisa Geral:

# 🔐 Sistema de Votação Presencial com Criptografia

## 📌 1. Escolha do tipo de criptografia

### ✅ Simétrica (AES)
- Mais rápida.
- Ideal se todos os dispositivos compartilham uma **chave secreta**.

### ✅ Assimétrica (RSA/ECC)
- Mais segura para **troca de chaves**.
- Mais lenta.
- Ideal para **autenticação inicial**.

### 🎯 Recomendação
Use **RSA para troca de chaves** e **AES para criptografar os votos**.

---

## 📌 2. Fluxo de criptografia sugerido

### 🛠 Etapa de Preparação:
- Cada terminal de votação (cliente) e o servidor geram um **par de chaves RSA** (pública/privada).
- A **chave pública do servidor é distribuída** para os clientes.

### 🔐 Etapa de Comunicação Segura:
1. Cliente gera uma **chave AES aleatória**.
2. Cliente **criptografa essa chave AES** com a **chave pública do servidor (RSA)**.
3. Cliente **envia a chave criptografada** via UDP para o servidor.
4. Servidor **decripta com sua chave privada RSA** e obtém a chave AES.
5. A partir daí, todas as mensagens (votos, confirmações, etc.) são **criptografadas com AES**.

---

## 📌 3. Exemplo em pseudocódigo simplificado

### 🧑‍💻 Cliente:

```python
# Geração da chave AES
aes_key = generate_random_aes_key()

# Criptografa a chave AES com a chave pública do servidor
encrypted_aes_key = rsa_encrypt(server_public_key, aes_key)

# Envia via UDP
udp_send(encrypted_aes_key)

# Depois, envia o voto criptografado
vote = "Candidato A"
encrypted_vote = aes_encrypt(aes_key, vote)
udp_send(encrypted_vote)
```

### 🖥️ Servidor:

```python
# Recebe chave AES criptografada
encrypted_aes_key = udp_receive()

# Decripta com a chave privada
aes_key = rsa_decrypt(server_private_key, encrypted_aes_key)

# Recebe o voto criptografado
encrypted_vote = udp_receive()

# Decripta o voto
vote = aes_decrypt(aes_key, encrypted_vote)
```

---

## 📌 4. Considerações extras

- **Integridade:** Use **HMAC** com a chave AES para garantir integridade das mensagens.
- **Nonce ou IV:** Para AES em modo seguro (ex: CBC ou GCM), use um **vetor de inicialização (IV)** diferente por mensagem.
- **UDP é não confiável:** Evite retransmitir pacotes sensíveis sem verificação.
- **Assinatura Digital:** Pode ser usada para garantir que o voto veio de um cliente autorizado.

---



# Possível Implementação:

# 🗳️ Aplicativo de Votação Presencial com Criptografia e Rede Local (UDP) - Python


## 🔐 Objetivo

Garantir:
- **Confidencialidade:** o voto não pode ser lido por terceiros.
- **Integridade:** o voto não pode ser alterado.
- **Autenticidade:** o voto vem de um terminal confiável.

## ⚙️ Tecnologias utilizadas

- **UDP (sockets)** para comunicação local.
- **RSA (assimétrica)** para troca de chave segura.
- **AES (simétrica)** para criptografia de votos.
- **JSON** para armazenamento dos votos.
- **Python** com a biblioteca `cryptography`.

---

## 🏗️ Estrutura do Sistema

### 1. Cliente
- Gera uma chave AES aleatória.
- Criptografa a chave AES com a chave pública do servidor (RSA).
- Criptografa o voto com AES.
- Envia tudo via UDP para o servidor.

### 2. Servidor
- Recebe a chave AES criptografada e decripta com sua chave privada RSA.
- Recebe o voto criptografado e decripta com a chave AES.
- Salva o voto em um arquivo `votos.json`.

---

## 📦 Instalação

Instale a biblioteca necessária:

```bash
pip install cryptography
```

---

## 🖥️ Código do Servidor (servidor.py)

```python
import socket
import os
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Gerar par de chaves RSA
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Salvar chave pública para os clientes
with open("server_public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# Inicializar servidor UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 9999))
print("Servidor pronto. Aguardando votos...")

# Receber chave AES criptografada
encrypted_key, addr = sock.recvfrom(1024)
aes_key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Receber IV + voto criptografado
data, _ = sock.recvfrom(1024)
iv = data[:16]
encrypted_vote = data[16:]

# Decriptar voto
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
decryptor = cipher.decryptor()
padded_vote = decryptor.update(encrypted_vote) + decryptor.finalize()
vote = padded_vote.rstrip(b"\0").decode()

print(f"Voto recebido: {vote}")

# Salvar voto em votos.json
file_path = "votos.json"

# Carregar ou criar lista de votos
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        votos = json.load(f)
else:
    votos = []

# Adicionar novo voto
votos.append({"voto": vote})

# Salvar em JSON
with open(file_path, "w") as f:
    json.dump(votos, f, indent=4)

print("Voto salvo com sucesso em votos.json.")
```

---

## 🗳️ Código do Cliente (cliente.py)

```python
import socket
from cryptography.hazmat.primitives.asymmetric import padding, serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Carregar chave pública do servidor
with open("server_public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Gerar chave AES
aes_key = os.urandom(32)  # AES-256

# Criptografar chave AES com RSA
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Criptografar voto
vote = "Candidato A"
padded_vote = vote.encode().ljust(128, b"\0")  # padding simples
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
encryptor = cipher.encryptor()
encrypted_vote = encryptor.update(padded_vote) + encryptor.finalize()

# Enviar via UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(encrypted_key, ("127.0.0.1", 9999))          # Enviar chave AES
sock.sendto(iv + encrypted_vote, ("127.0.0.1", 9999))    # Enviar IV + voto

print("Voto enviado com sucesso.")
```

---

## ✅ Exemplo de saída (`votos.json`)

```json
[
    {"voto": "Candidato A"},
    {"voto": "Candidato B"}
]
```

---

## 🔐 Melhorias possíveis

- Assinatura digital dos votos.
- Marcar data/hora e ID do terminal.
- Rejeitar votos duplicados.
- Interface gráfica (GUI) para o terminal.

---

