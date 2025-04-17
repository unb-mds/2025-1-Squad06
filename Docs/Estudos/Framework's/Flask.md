# Guia Completo sobre o Flask

## O que é o Flask?

O Flask é um framework web minimalista para a linguagem de programação Python. Ele é projetado para ser simples, flexível e fácil de aprender, oferecendo as ferramentas essenciais para construir aplicações web, mas deixando as escolhas sobre como estruturá-las em mãos do desenvolvedor. 

O Flask é classificado como um "microframework" porque, por padrão, ele não inclui muitas funcionalidades prontas como outros frameworks mais pesados, como o Django. No entanto, ele permite a adição de extensões, que podem adicionar várias funcionalidades conforme as necessidades do projeto.

## Por que usar o Flask?

O Flask é ideal para desenvolvedores que precisam de controle total sobre a estrutura de suas aplicações ou que desejam algo mais leve e simples do que frameworks maiores. É uma excelente escolha para projetos menores ou quando você precisa de um início rápido para uma aplicação, com a flexibilidade para adicionar mais recursos conforme necessário.

### Principais Vantagens do Flask

- **Simples e Flexível**: O Flask não impõe uma estrutura rígida, permitindo que os desenvolvedores escolham como organizar e configurar a aplicação.
- **Extensível**: Ele pode ser facilmente expandido com extensões para adicionar funcionalidades como autenticação de usuários, gerenciamento de banco de dados, validação de formulários, entre outros.
- **Minimalista**: A abordagem minimalista significa que o Flask oferece apenas o básico para criar uma aplicação web, permitindo que você adicione apenas o que precisa.
- **Boa Documentação**: O Flask tem uma documentação excelente e comunidade ativa, o que facilita muito para quem está começando.

## Como funciona o Flask?

O Flask segue a arquitetura **Wsgi** (Web Server Gateway Interface) e adota uma abordagem de **Roteamento** de requisições, onde as URLs são associadas a funções no código, chamadas de "views". Ou seja, quando uma requisição é feita para uma URL específica, uma função Python é executada para processar essa requisição.

Por ser um framework minimalista, o Flask não faz muitas suposições sobre como sua aplicação deve ser organizada. Ele fornece as ferramentas básicas para começar e oferece grande flexibilidade para você decidir como estruturar o seu projeto.

### Conceitos Básicos

1. **Roteamento (Routing)**: O Flask permite associar URLs a funções Python. Quando uma URL é acessada, a função associada a ela é chamada. Isso é feito através do uso do decorador `@app.route`.
2. **Views**: As views são funções que recebem uma requisição HTTP e retornam uma resposta. O Flask usa essas funções para manipular e responder a requisições de diferentes tipos, como GET e POST.
3. **Templates**: O Flask usa o Jinja2, um motor de templates, para renderizar as páginas HTML. Com Jinja2, você pode passar dados dinâmicos para os templates e exibi-los na página.
4. **Sessões e Cookies**: O Flask tem suporte interno para gerenciamento de sessões, o que é útil para armazenar dados temporários entre requisições, como informações do usuário autenticado.

### Fluxo de Requisição no Flask

Quando um usuário faz uma requisição para uma URL, o Flask passa por várias etapas até gerar a resposta:

1. **Entrada da Requisição**: A requisição do usuário chega ao servidor Flask.
2. **Roteamento**: O Flask mapeia a URL para a função view correspondente.
3. **Processamento**: A função view é executada e pode acessar dados, processar informações e interagir com bancos de dados.
4. **Resposta**: A função view retorna uma resposta, geralmente um HTML renderizado, que é enviada de volta ao navegador do usuário.

## Observação
Quando se trata de um aplicativo que usará apenas a rede UDP (User Datagram Protocol) para comunicação, o Flask pode não ser a escolha ideal para o backend. O Flask é projetado para trabalhar com HTTP e HTTPS, que são protocolos orientados a conexão, o que significa que ele se baseia na troca de requisições e respostas entre cliente e servidor, um modelo mais adequado para a web tradicional.

Já o UDP é um protocolo sem conexão, usado para transmitir pacotes de dados de forma rápida e sem garantir a entrega ou ordem dos pacotes. Ele é frequentemente usado para aplicações que exigem baixa latência, como jogos em tempo real, chamadas de voz e outras comunicações em rede que não precisam da confiabilidade e controle de fluxo do TCP.  

## Referências

["Flask Python: o que é e como funciona?"](https://www.locaweb.com.br/blog/temas/codigo-aberto/flask-phyton-o-que-e/)