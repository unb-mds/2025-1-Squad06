# 📋 Requisitos de Host – Aplicativo de Votação Local via UDP

## 🎯 Objetivo do Host

Hospedar uma aplicação de votação local que funcione em redes internas, com comunicação via protocolo **UDP**, sem dependência de internet.

---

## 💻 Requisitos de Software

- **Sistema Operacional**: Linux (Ubuntu Server recomendado) ou Windows (a definir)
- **Ambiente de Execução**: (a definir)
- **Bibliotecas UDP**: *(a definir, dependente da linguagem)*
- **Interface Gráfica**: *(a definir)*
- **Gerenciamento**: Interface de administração local (web ou desktop) *(a definir)*

---

## 📡 Requisitos de Rede

- Comunicação via **protocolo UDP** (ex: portas 5005, 5006)
- Conexão via **Wi-Fi ou cabo Ethernet**
- Rede local (LAN) sem necessidade de internet
- Possibilidade de criar **hotspot ou roteador local** para conectar os dispositivos

---

## 🔐 Requisitos de Segurança (Rede Local)

- Isolamento físico da rede (sem acesso externo)
- Registro de logs local
- Exportação de resultados (PDF/CSV) *(se necessário,  definir a necessidade)*
- Controle de acesso do administrador/master (login local simples) 

---

# 🧰 Funcionalidades Esperadas com Tecnologias Sugeridas

## Funcionalidades principais

---

### 🔹 Início do sistema como HOST (mestre da votação) **(importante)**  
**Tecnologias sugeridas:**  
- Backend: Python (`socket`, `threading`), Node.js (`dgram`)  
- Interface: Tkinter, Electron, PyQt5, React

---

### 🔹 Definição da pergunta a ser votada via interface do HOST **(importante)**  
**Tecnologias sugeridas:**  
- Frontend: React, Tkinter, Flutter  
- Armazenamento opcional: SQLite (registro local)

---

### 🔹 Envio da pergunta para todos os dispositivos via UDP broadcast **(importante)**  
**Tecnologias sugeridas:**  
- Python (`socket.sendto` com `broadcast`)  
- Node.js (`dgram` com `socket.setBroadcast(true)`)

---

### 🔹 Interface de votação com três opções:  
- ✅ A favor  
- ❌ Contra  
- ⚪ Abstenção  
**Tecnologias sugeridas:**  
- UI: React, Flutter, HTML+JS, Tkinter  
- Lógica de envio: Python ou JS para UDP unicast

---

### 🔹 Envio do voto via UDP unicast diretamente ao HOST **(importante)**  
**Tecnologias sugeridas:**  
- Python (`socket.sendto` com IP do HOST)  
- Node.js (`dgram.send` com IP do HOST)

---

### 🔹 Recebimento, validação e contagem de votos no HOST em tempo real **(importante)**  
**Tecnologias sugeridas:**  
- Backend: Python com `threading` para escuta contínua  
- Armazenamento temporário: dicionário em memória, ou SQLite

---

### 🔹 Visualização de resultados parciais conforme os votos chegam **(importante)**  
**Tecnologias sugeridas:**  
- Interface: React + Chart.js, Tkinter com `matplotlib`, Electron

---

### 🔹 Encerramento manual da votação pelo HOST  
**Tecnologias sugeridas:**  
- CLI: `input()` no Python  
- GUI: Botão em interface React, Flutter, Tkinter

---

### 🔹 Exibição do resultado final com contagem por opção **(importante)**  
**Tecnologias sugeridas:**  
- Interface: React, Tkinter, PyQt5  
- Visualização: gráfico ou tabela (Chart.js, `matplotlib`)

---

### 🔹 Possibilidade de iniciar nova rodada de votação  
**Tecnologias sugeridas:**  
- Reset automático das variáveis do sistema  
- Botão "Nova Votação" na interface (React, Tkinter)

---

### 🔹 Armazenamento local das votações realizadas **(importante)**  
**Tecnologias sugeridas:**  
- SQLite, JSON local, ou arquivos `.csv`  
- Backend em Python, Node.js, ou Dart (Flutter)

---

### 🔹 Visualização do status dos dispositivos conectados  
**Tecnologias sugeridas:**  
- Registro de IPs de votos recebidos  
- Ping UDP ou heartbeat periódicos

---

### 🔹 Número de votos recebidos e aguardados  
**Tecnologias sugeridas:**  
- Interface dinâmica que mostra contagem total esperada  
- Estimativa baseada em número de dispositivos detectados

---

### 🔹 Identificação de dispositivos que perderam conexão  
**Tecnologias sugeridas:**  
- Heartbeat UDP periódico dos CLIENTES  
- Timeout para considerar desconexão

---

---

## 🛠️ Requisitos de Testes / Diagnóstico
- Modo de teste da rede: simula envio e recebimento de pacotes via UDP.
- Log de erro com mensagens compreensíveis. **(importante)**
- Feedback visual para o usuário em caso de falha (ex: “Conexão perdida com o master”).
 
 ---

## 🔧 Facilidade de Instalação e Execução
- Aplicação deve rodar com um único comando/script.
- Requisitos de instalação documentados.
- Instalação local simples, sem necessidade de serviços externos.
- Deve ser possível atualizar o sistema sem reiniciar toda a rede.
- As atualizações devem ser simples.
---
