# 🗳️ Funcionalidades Essenciais para Votantes

## ✅ Experiência do Usuário CLIENTE

---

### 🔹 Receber a pergunta e cronômetro enviados pelo HOST **(importante)**  
**Descrição:**  
Ao iniciar o aplicativo, o dispositivo do votante deve escutar automaticamente a rede local e exibir a pergunta e cronômetro assim que forem enviados pelo host.  

**Tecnologias sugeridas:**  
- Backend: Python (`socket.recvfrom`), Node.js (`dgram`)  
- Interface: React Native, Flutter, Electron, Tkinter

---

### 🔹 Receber aviso quanto ao tempo, antes da votação **(importante)**  
**Descrição:**  
Ao entrar como vontante, antes da votação efetivamente começar, o votante deve receber um aviso sobre o cronômetro, para evitar que os usuários percam o prazo da votação. 

---

### 🔹 Interface intuitiva para seleção de voto **(importante)**  
**Descrição:**  
O usuário deve visualizar três opções claras e fáceis de tocar/clicar:  
- ✅ A favor  
- ❌ Contra  
- ⚪ Abstenção  

**Tecnologias sugeridas:**  
- UI/Frontend: React, Flutter, HTML+JS, Tkinter

---

### 🔹 Enviar o voto diretamente ao HOST via UDP **(importante)**  
**Descrição:**  
O voto deve ser transmitido ao IP do HOST usando UDP unicast com confirmação visual de que foi enviado.  

**Tecnologias sugeridas:**  
- Python (`socket.sendto`)  
- Node.js (`dgram.send`)  
- Visual feedback na interface (ex: "voto enviado com sucesso")

---

### 🔹 Garantia de privacidade do voto  
**Descrição:**  
O voto deve ser transmitido sem expor a identidade do votante a outros participantes.  

**Tecnologias sugeridas:**  
- Transmissão sem metadados pessoais  
- Possível uso de anonimização local

---

### 🔹 Feedback visual sobre status do voto  
**Descrição:**  
Após o envio, o sistema deve informar o usuário se o voto foi recebido com sucesso ou não, após confirmação do votante.
Caso não tenha sucesso ao votar, pode tentar novamente

**Tecnologias sugeridas:**  
- Mensagem de status na interface  
- Sistema simples de feedback via ícone ou cor

---

### 🔹 Reconexão automática caso a votação tenha começado  
**Descrição:**  
Se o dispositivo entrar na rede após o início da votação, ele deve tentar solicitar a pergunta ao HOST automaticamente.  

**Tecnologias sugeridas:**  
- Detecção de ausência de pergunta após X segundos  
- Requisição UDP de sincronização (`request_question`)

---

### 🔹 Interface leve e responsiva **(importante)**  
**Descrição:**  
Deve funcionar em celulares antigos, com pouco processamento, sem travamentos.  

**Tecnologias sugeridas:**  
- Flutter (otimizado)  
- React Native com otimização  
- Aplicativo desktop leve (Electron ou Tkinter)

---

### 🔹 Participar sem necessidade de internet **(importante)**  
**Descrição:**  
Tudo deve funcionar via rede local, sem precisar de internet externa.  

**Tecnologias sugeridas:**  
- Comunicação exclusiva via UDP na LAN  
- Sem dependências de APIs externas

---

### 🔹 Prevenção de múltiplos votos

**Descrição:**  
O sistema deve garantir que cada dispositivo possa votar apenas uma vez por pergunta.

**Tecnologias sugeridas:**  
- Geração de um ID único por dispositivo na sessão

---
