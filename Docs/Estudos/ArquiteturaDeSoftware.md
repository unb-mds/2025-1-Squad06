# **Exemplos de Arquitetura de Software**

## **1. Arquitetura MVC (Model-View-Controller)**

O **MVC** é um padrão arquitetural que divide uma aplicação em três camadas principais:

### **Componentes:**
- **Model (Modelo):**  
  - Representa os dados e a lógica de negócios.  
  - Gerencia a recuperação, atualização e armazenamento de informações.  
  - **Exemplo:** Em um sistema de e-commerce, o "Model" pode ser uma classe que gerencia informações sobre produtos e pedidos.

- **View (Visão):**  
  - Responsável pela interface com o usuário.  
  - Exibe os dados do Model e captura a entrada do usuário.  
  - **Exemplo:** No mesmo e-commerce, a View pode ser a página HTML que exibe os produtos disponíveis.

- **Controller (Controlador):**  
  - Atua como intermediário entre Model e View.  
  - Processa entradas do usuário e aciona as alterações necessárias no Model e View.  
  - **Exemplo:** Se um usuário adicionar um produto ao carrinho, o Controller recebe a ação e atualiza o Model.

---

## **2. Arquitetura Cliente-Servidor**

Essa arquitetura separa o sistema em duas partes fundamentais:

### **Componentes:**
- **Cliente:**  
  - Responsável por solicitar serviços ao servidor.  
  - Pode ser um navegador, aplicativo mobile ou qualquer sistema que faz requisições.  
  - **Exemplo:** Um navegador que solicita uma página web.

- **Servidor:**  
  - Responde às solicitações do cliente e processa os dados.  
  - Pode armazenar informações, executar cálculos e retornar os resultados ao cliente.  
  - **Exemplo:** Um servidor web que entrega páginas HTML e processa login de usuários.

### **API (Application Programming Interface):**  
- Um conjunto de definições e protocolos que permite que diferentes sistemas se comuniquem.  
- No contexto cliente-servidor, a API define como o cliente pode solicitar dados do servidor.  
- **Exemplo:** Uma API de previsão do tempo permite que um aplicativo móvel solicite dados climáticos de um servidor.

---

## **3. Arquiteturas Monolítica, SOA e Microsserviços**

Cada uma dessas arquiteturas organiza os sistemas de maneira diferente:

### **Arquitetura Monolítica**
- **Componentes:**  
  - Aplicação única e indivisível.  
  - Um único banco de dados para todos os módulos.  
  - Comunicação interna direta entre os módulos.

- **Vantagens:**  
  - Simplicidade no desenvolvimento e na implantação.  
  - Fácil depuração, pois tudo está num único sistema.

- **Desvantagens:**  
  - Dificuldade de escalar e manter conforme o sistema cresce.  
  - Qualquer pequena mudança exige reimplantar toda a aplicação.

### **Arquitetura SOA (Service-Oriented Architecture)**
- **Componentes:**  
  - Conjunto de **serviços** independentes que se comunicam entre si.  
  - Um barramento de mensagens ou middleware para orquestração.  
  - **Exemplo:** Um serviço de pagamento pode ser separado de um serviço de envio de pedidos.

- **Vantagens:**  
  - Reutilização de serviços para diferentes aplicações.  
  - Facilidade de integração com outros sistemas.

- **Desvantagens:**  
  - Complexidade na comunicação entre serviços.  
  - Pode gerar sobrecarga na rede devido ao uso de mensagens para comunicação.

### **Arquitetura de Microsserviços**
- **Componentes:**  
  - Pequenos serviços independentes que rodam separadamente.  
  - Comunicação via **APIs REST** ou **mensageria**.  
  - Cada microsserviço pode ter seu próprio banco de dados.

- **Vantagens:**  
  - **Escalabilidade:** cada serviço pode ser escalado separadamente.  
  - **Independência:** mudanças em um serviço não afetam toda a aplicação.  
  - **Exemplo:** No Netflix, um microsserviço gerencia recomendações, enquanto outro cuida do processamento de vídeo.

- **Desvantagens:**  
  - Complexidade maior na orquestração dos serviços.  
  - Monitoramento e deploy são mais desafiadores.

---

## **Fontes**
- [MVC em 3 Minutos | Model - View - Controller](https://www.youtube.com/watch?v=ZW2JLtX4Dag)
- [Arquitetura Cliente-servidor | O que é, Como Funciona e Exemplo](https://www.youtube.com/watch?v=FWeHPCqD67c)
- [Arquitetura de Software: Monolítica x SOA x Microsserviços - APS08](https://www.youtube.com/watch?v=suZfVAk7hco)
