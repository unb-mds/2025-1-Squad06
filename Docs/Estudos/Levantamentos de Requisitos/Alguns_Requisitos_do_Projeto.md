# 🗳️ Requisitos do Projeto

## Sistema de Votação Presencial com Rede Local (UDP)

---

## 1. Requisitos Funcionais (RF)

-  O sistema deve permitir que um HOST defina e envie perguntas de votação.
-  Os CLIENTES devem receber as perguntas automaticamente via rede local (UDP Broadcast).
-  Os CLIENTES devem exibir a pergunta para o usuário escolher uma das opções: A Favor, Contra, Abstenção.
-  O CLIENTE deve enviar o voto ao HOST via UDP unicast.
-  O HOST deve contabilizar votos recebidos por tipo.
-  O HOST deve exibir os resultados em tempo real.
-  O HOST deve encerrar a votação manualmente (por comando ou tecla).
-  O sistema deve exibir os resultados finais com total por opção.
-  O sistema deve permitir múltiplas rodadas de votação.

---

## 2. Requisitos Não Funcionais (RNF)

-  O sistema deve funcionar em rede local sem necessidade de acesso à internet.
-  A comunicação entre dispositivos deve utilizar o protocolo UDP.
-  O tempo de resposta entre envio e recebimento de voto deve ser inferior a 1 segundo.
-  A interface deve ser simples e acessível, podendo rodar via terminal.
-  O sistema deve ser compatível com Python 3.x.
-  O sistema deve rodar em ambientes com recursos limitados (ex: Pydroid no Android).
-  O código-fonte deve ser open source, com comentários e documentação básica.

---

## 3. Requisitos de Teste (RT)

-  Testar envio de pergunta e recepção em múltiplos clientes conectados.
-  Testar envio de votos simultâneos e verificação de contagem correta.
-  Testar falha de cliente (desligar um cliente) e estabilidade do sistema.
-  Testar latência de comunicação em diferentes distâncias da rede Wi-Fi.
-  Testar compatibilidade com terminal, Windows, Linux e Android (via Pydroid).
-  Testar bloqueio de votação após finalização pelo HOST.

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

---

## 6. Documentação de requisitos
- [Link do Miro para documentação de requisitos](https://miro.com/app/board/uXjVIJOVs_Y=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=view-activity&lid=8hnc0q4xt65k)
