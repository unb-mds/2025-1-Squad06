# **Arquitetura de Software**

## **Nosso Documento de Arquitetura de Software**

-Após discussões sobre organização em algumas Sprints, optamos em usar o modelo MVC (Model-View-Controller)
-O documento de arquitetura se encontra nesse link do Miro, em que também está presente os documentos de requisitos: [Miro](https://miro.com/app/board/uXjVIJOVs_Y=/?share_link_id=65146293093)

---

## **O que é Arquitetura de Software?**
A arquitetura de um software é uma estrutura que estabelece a divisão dos seus componentes e como eles se comunicam entre si, dessa forma define como será a construção do sistema e como ele vai crescer ao longo do tempo. A criação de uma arquitetura de software é muito importante para direcionar o projeto como um todo.

Quando eu falo sobre "componentes" me refiro a módulos que realizam determinadas funções, então na hora da arquitetar um software, você pode por exemplo estabelecer que vai ter um módulo dedicado ao banco de dados, um módulo dedicado ao processamento desses dados, um módulo dedicado ao design do UI e etc, todas essas repartições são definidas na arquitetura, e o modo como elas vão interagir entre si também, então por exemplo como o banco de dados vai interagir com o módulo que vai processar os dados? por meio de uma API? ou vão interagir de modo direto dentro do código? isso também será definido na arquitetura, além disso outras coisas como a sequência que o software seguirá na sua execução, como o código vai ser organizado nos diretórios e muitas outras coisas podem ser definidas na arquitetura. 

## **Documentação de uma Arquitetura**
Devido a grande amplitude de uma arquitetura sua representação como um todo exige vários tipos diferentes de documentação tanto em forma de texto como em forma de diagramas, cada documento vai esclarecer aspectos diferentes do software.

[Exemplos de documentos](https://www.youtube.com/watch?v=BwwD5v1yDz0&t=168s&ab_channel=EuTIEnsino) (2:48-3:29)

## **Padrões de Arquiteturais**
Em vez de sempre fazer uma arquitetura do absoluto zero, é possível utilizar padrões já estabelecidos e apenas modificá-los de acordo com a necessidade do projeto. Existem vários padrões de arquitetura conhecidos e que já foram amplamente testados e comprovados, porém não existe uma arquitetura perfeita, cada arquitetura tem seus prós e contras, uma determinada arquitetura vai ser boa em uma determinada coisa, porém será ruim em outra e pode existir uma outra arquitetura que é ruim no que essa é boa mas boa no que essa é ruim, os prós e os contras de uma arquitetura de software são chamados de tradeoffs.

## **Exemplos de Padrões Arquiteturais**

### **1. Arquitetura MVC (Model-View-Controller)**

O **MVC** é um padrão arquitetural que divide uma aplicação em três camadas principais:

#### **Componentes:**
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

### **2. Arquitetura Cliente-Servidor**

Essa arquitetura separa o sistema em duas partes fundamentais:

#### **Componentes:**
- **Cliente:**  
  - Responsável por solicitar serviços ao servidor.  
  - Pode ser um navegador, aplicativo mobile ou qualquer sistema que faz requisições.  
  - **Exemplo:** Um navegador que solicita uma página web.

- **Servidor:**  
  - Responde às solicitações do cliente e processa os dados.  
  - Pode armazenar informações, executar cálculos e retornar os resultados ao cliente.  
  - **Exemplo:** Um servidor web que entrega páginas HTML e processa login de usuários.

#### **API (Application Programming Interface):**  
- Um conjunto de definições e protocolos que permite que diferentes sistemas se comuniquem.  
- No contexto cliente-servidor, a API define como o cliente pode solicitar dados do servidor.  
- **Exemplo:** Uma API de previsão do tempo permite que um aplicativo móvel solicite dados climáticos de um servidor.

---

### **3. Arquiteturas Monolítica, SOA e Microsserviços**

Cada uma dessas arquiteturas organiza os sistemas de maneira diferente:

#### **Arquitetura Monolítica**
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

#### **Arquitetura SOA (Service-Oriented Architecture)**
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

#### **Arquitetura de Microsserviços**
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

## **Criação de uma Arquitetura** 
Ao criar uma arquitetura é necessário estar plenamente ciente dos Requisitos de Software pois isso que vai ditar quais tradeoffs valem a pena ou não e qual são os aspectos do sistema que devem ser priorizados na hora de tomar decisões, toda a escolha da arquitetura tem como objetivo cumprir tais resquisitos.

## **Fontes**
- [MVC em 3 Minutos | Model - View - Controller](https://www.youtube.com/watch?v=ZW2JLtX4Dag)
- [Arquitetura Cliente-servidor | O que é, Como Funciona e Exemplo](https://www.youtube.com/watch?v=FWeHPCqD67c)
- [Arquitetura de Software: Monolítica x SOA x Microsserviços - APS08](https://www.youtube.com/watch?v=suZfVAk7hco)
- [Arquitetura de Software](https://www.youtube.com/playlist?list=PLX0VJrazYICCC2a_Ab-sZwLn_LIO8gc4T)
- [Intro to Software Architecture | Overview, Examples, and Diagrams](https://www.youtube.com/watch?v=k3hKLd7vYZ8&ab_channel=FaradayAcademy)
