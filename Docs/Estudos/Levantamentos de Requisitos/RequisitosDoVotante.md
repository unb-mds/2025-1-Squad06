# 🗳️ Funcionalidades Essenciais para Votantes

## ✅ Experiência do Usuário CLIENTE

---

### 🔹 Receber automaticamente a pergunta enviada pelo HOST **(importante)**  
**Descrição:**  
Ao iniciar o aplicativo, o dispositivo do votante deve escutar automaticamente a rede local e exibir a pergunta assim que ela for enviada.  

**Tecnologias sugeridas:**  
- Backend: Python (`socket.recvfrom`), Node.js (`dgram`)  
- Interface: React Native, Flutter, Electron, Tkinter

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
O voto deve ser transmitido sem expor o conteúdo ou identidade do votante a outros participantes.  

**Tecnologias sugeridas:**  
- Transmissão sem metadados pessoais  
- Possível uso de anonimização local

---

### 🔹 Feedback visual sobre status do voto  
**Descrição:**  
Após o envio, o sistema deve informar o usuário que o voto foi recebido ou está aguardando confirmação.  

**Tecnologias sugeridas:**  
- Mensagem de status na interface  
- Sistema simples de feedback via ícone ou cor

---

### 🔹 Reconexão automática caso perca a pergunta  
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

### 🔹 Histórico local básico
**Descrição:**  
O usuário pode ver um pequeno histórico local que mostra as perguntas já votadas e qual foi o seu voto correspondente em cada pergunta.

---
