# Roteiro de Levantamento de Requisitos  
Sistema de Votação Presencial em Rede Local (Protocolo UDP)

## 1. Objetivo Geral

**1.1** Qual é o objetivo principal do sistema?  
Resposta: Permitir a realização de votações presenciais em rede local, de forma rápida e sem necessidade de internet, utilizando o protocolo UDP.

**1.2** Em que ambientes o sistema será utilizado?  
Resposta: Assembleias, plenárias e reuniões onde os participantes estão conectados à mesma rede Wi-Fi.

## 2. Participantes e Papéis

**2.1** Quem são os usuários do sistema e quais são seus papéis?  
Resposta:  
- HOST: Inicia a votação, envia perguntas, recebe e contabiliza os votos, exibe resultados.  
- CLIENTES: Recebem perguntas e enviam votos ao HOST.

## 3. Rede e Comunicação

**3.1** O sistema funciona com ou sem conexão à internet?  
Resposta: Funciona sem internet, utilizando rede local via Wi-Fi.

**3.2** Todos os dispositivos estarão conectados à mesma rede local?  
Resposta: Sim, todos os dispositivos (HOST e CLIENTES) estarão na mesma rede local.

**3.3** Qual protocolo de comunicação será utilizado? Por quê?  
Resposta: UDP, por ser leve e permitir transmissão por broadcast para todos os dispositivos da rede.

## 4. Fluxo da Votação

**4.1** Como o sistema é iniciado?  
Resposta: O HOST inicia o sistema e se prepara para enviar uma nova votação.

**4.2** Como a pergunta é definida e enviada?  
Resposta: O HOST digita a pergunta e a envia via UDP broadcast para todos os CLIENTES.

**4.3** O que acontece após o envio da pergunta?  
Resposta: Os CLIENTES recebem a pergunta automaticamente e a exibem em suas interfaces.

**4.4** Quais são as opções de voto disponíveis para os usuários?  
Resposta: A Favor, Contra, Abstenção.

**4.5** Como os CLIENTES enviam seus votos?  
Resposta: Cada CLIENTE envia seu voto via UDP diretamente ao HOST.

**4.6** O que o HOST faz ao receber os votos?  
Resposta: Valida e contabiliza os votos recebidos, atualizando a contagem em tempo real.

**4.7** O HOST pode visualizar os resultados durante a votação?  
Resposta: Sim, o sistema exibe resultados parciais à medida que os votos chegam.

**4.8** Como a votação é encerrada?  
Resposta: O HOST encerra manualmente a votação, pressionando ENTER ou acionando um comando.

**4.9** O que acontece após o encerramento da votação?  
Resposta: O sistema exibe o resultado final, com a contagem de votos por opção.

**4.10** O sistema permite iniciar nova votação após o fim de uma?  
Resposta: Sim, o processo pode ser reiniciado com uma nova pergunta.

## 5. Interface do Sistema

**5.1** O sistema deve ter interface gráfica?  
Resposta: Sim.  
- No HOST: campo para digitar a pergunta, botão para enviar, painel de resultados em tempo real.  
- Nos CLIENTES: exibição da pergunta e botões para votar.

**5.2** A interface será em qual idioma?  
Resposta: Português.

**5.3** Em quais plataformas o sistema deve funcionar?  
Resposta: Preferencialmente Windows para HOST e Android para CLIENTES. Linux é bem-vindo. iOS não é obrigatório.

## 6. Segurança e Confiabilidade

**6.1** Os votos devem ser anônimos?  
Resposta: Sim, os votos não devem ser identificáveis.

**6.2** É necessário autenticar CLIENTES antes da votação?  
Resposta: Não, basta que o dispositivo esteja na mesma rede local.

**6.3** A comunicação precisa ser criptografada?  
Resposta: Não, visto que o sistema será utilizado em ambientes controlados.

**6.4** Deve haver registro dos votos para auditoria?  
Resposta: Não é necessário inicialmente, mas pode ser considerado no futuro.

## 7. Considerações Finais

**7.1** O sistema precisa salvar os resultados?  
Resposta: Não obrigatoriamente, apenas exibir os resultados na tela do HOST já é suficiente.

## 8. Link do UserFlow (Miro)

[Documento User Flow no Miro](https://miro.com/app/board/uXjVIJOVs_Y=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=view-activity&lid=8hnc0q4xt65k)


## 9. Possíveis telas



![TELAS](https://github.com/user-attachments/assets/bdfccc66-6051-4da2-847d-b0201e734c21)


