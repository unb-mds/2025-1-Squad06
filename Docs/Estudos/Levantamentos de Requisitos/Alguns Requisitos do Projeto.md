# 🗳️ Requisitos do Projeto

## Sistema de Votação Presencial com Rede Local (UDP)

---

## 1. Requisitos Funcionais (RF)

- RF01. O sistema deve permitir que um HOST defina e envie perguntas de votação.
- RF02. Os CLIENTES devem receber as perguntas automaticamente via rede local (UDP Broadcast).
- RF03. Os CLIENTES devem exibir a pergunta para o usuário escolher uma das opções: A Favor, Contra, Abstenção.
- RF04. O CLIENTE deve enviar o voto ao HOST via UDP unicast.
- RF05. O HOST deve contabilizar votos recebidos por tipo.
- RF06. O HOST deve exibir os resultados em tempo real.
- RF07. O HOST deve encerrar a votação manualmente (por comando ou tecla).
- RF08. O sistema deve exibir os resultados finais com total por opção.
- RF09. O sistema deve permitir múltiplas rodadas de votação.

---

## 2. Requisitos Não Funcionais (RNF)

- RNF01. O sistema deve funcionar em rede local sem necessidade de acesso à internet.
- RNF02. A comunicação entre dispositivos deve utilizar o protocolo UDP.
- RNF03. O tempo de resposta entre envio e recebimento de voto deve ser inferior a 1 segundo.
- RNF04. A interface deve ser simples e acessível, podendo rodar via terminal.
- RNF05. O sistema deve ser compatível com Python 3.x.
- RNF06. O sistema deve rodar em ambientes com recursos limitados (ex: Pydroid no Android).
- RNF07. O código-fonte deve ser open source, com comentários e documentação básica.

---

## 3. Requisitos de Teste (RT)

- RT01. Testar envio de pergunta e recepção em múltiplos clientes conectados.
- RT02. Testar envio de votos simultâneos e verificação de contagem correta.
- RT03. Testar falha de cliente (desligar um cliente) e estabilidade do sistema.
- RT04. Testar latência de comunicação em diferentes distâncias da rede Wi-Fi.
- RT05. Testar compatibilidade com terminal, Windows, Linux e Android (via Pydroid).
- RT06. Testar bloqueio de votação após finalização pelo HOST.

---

## 4. Requisitos Técnicos (RTec)

- Linguagem: Python 3.x
- Protocolos: UDP (Broadcast e Unicast)
- Bibliotecas sugeridas: socket, threading, tkinter (se GUI), Flask (para futura versão web)
- Ambiente mínimo: Dispositivos conectados à mesma rede local (Wi-Fi ou LAN)
- Compatibilidade:
  - Computadores (Windows/Linux/macOS)
  - Celulares Android (via Pydroid 3)
  - Navegadores (em versão Web)

---

## 5. Extras Futuramente Implementáveis

- Criptografia das mensagens para maior segurança.
- Identificação por nome ou ID do votante.
- Armazenamento dos resultados em banco de dados local (SQLite).
- Adaptação para interface web com Flask (permite uso em celulares via navegador).
