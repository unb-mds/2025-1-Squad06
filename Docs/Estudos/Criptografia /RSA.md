# RSA - Criptografia Assimétrica

## O que é o RSA?

O **RSA** (Rivest-Shamir-Adleman) é um algoritmo de criptografia assimétrica, o que significa que ele usa uma **chave pública** para criptografar os dados e uma **chave privada** para descriptografá-los. A segurança do RSA é baseada na dificuldade de fatorar números grandes, o que o torna resistente a ataques.

## Como o RSA Funciona?

O algoritmo RSA envolve três etapas principais: **geração de chaves**, **criptografia** e **descriptografia**. 

### 1. **Geração de Chaves**
   - **Chave Pública**: Usada para criptografar os dados. Pode ser compartilhada abertamente.
   - **Chave Privada**: Usada para descriptografar os dados. Deve ser mantida em segredo.
   
   A geração das chaves é realizada a partir de dois números primos grandes, os quais são multiplicados para gerar um número composto. A segurança do RSA depende da dificuldade de fatorar esse número composto.

### 2. **Criptografia**
   - Para criptografar uma mensagem, o remetente utiliza a chave pública do destinatário. A mensagem é convertida em um número (normalmente através de codificação) e, em seguida, criptografada usando a chave pública.

### 3. **Descriptografia**
   - O destinatário utiliza sua chave privada para descriptografar a mensagem recebida, convertendo o número de volta para o texto original.

## Características do RSA

- **Criptografia Assimétrica**: Usa duas chaves diferentes (pública e privada).
- **Segurança**: A segurança do RSA é baseada na dificuldade de fatoração de números grandes, o que o torna resistente a ataques de força bruta.
- **Escalabilidade**: RSA permite a troca segura de informações sem a necessidade de um canal seguro, uma vez que a chave pública pode ser distribuída livremente.

## Como o RSA Pode Ajudar no Projeto de Votação Presencial?

No contexto de um aplicativo de **votação presencial** com rede local (utilizando **UDP**), o **RSA** pode ser utilizado para garantir a **confidencialidade** e a **autenticidade** dos votos e das comunicações.

### 1. **Segurança da Comunicação**
   - O **RSA** pode ser usado para criptografar os dados que são enviados entre os participantes da votação e o servidor, garantindo que as mensagens não sejam interceptadas e lidas por partes não autorizadas.
   - A chave pública pode ser usada para criptografar os votos dos usuários antes que eles sejam enviados para o servidor de votação.

### 2. **Autenticação**
   - A chave privada pode ser utilizada para assinar digitalmente as mensagens e garantir a **autenticidade** do remetente. Isso é útil para garantir que o voto enviado foi realmente de um participante autorizado.
   - Por exemplo, cada participante pode usar sua chave privada para assinar digitalmente o seu voto, e o servidor pode verificar a assinatura usando a chave pública associada.

### 3. **Integridade dos Dados**
   - O uso de **assinaturas digitais** no RSA assegura que os dados não foram alterados durante a transmissão. Isso é essencial em sistemas de votação, onde a integridade dos votos deve ser garantida.

### 4. **Troca Segura de Chaves**
   - Como o RSA é um algoritmo de criptografia assimétrica, ele pode ser usado para realizar uma **troca segura de chaves**. Por exemplo, os participantes podem usar RSA para trocar chaves simétricas que serão utilizadas para criptografar as mensagens durante a comunicação subsequente, aproveitando a eficiência de algoritmos simétricos como AES.

## Como Implementar o RSA no Projeto

### 1. **Geração de Chaves**
   - O servidor pode gerar um par de chaves RSA (pública e privada). A chave pública é distribuída para todos os participantes, enquanto a chave privada é mantida em segredo no servidor.

### 2. **Criptografia e Descriptografia**
   - Os participantes do sistema usam a chave pública para criptografar seus votos antes de enviá-los ao servidor.
   - O servidor, por sua vez, usa a chave privada para descriptografar os votos e processar os resultados da votação.

### 3. **Assinaturas Digitais**
   - Para garantir a autenticidade dos votos, o servidor pode usar a chave privada para assinar as mensagens de confirmação de recebimento de votos, e os participantes podem verificar a assinatura utilizando a chave pública.

### 4. **Exemplo de Fluxo de Votação**
   1. O servidor gera um par de chaves RSA (pública e privada).
   2. O servidor distribui a chave pública aos participantes.
   3. Os participantes criptografam seus votos com a chave pública e os enviam via UDP.
   4. O servidor descriptografa os votos com a chave privada e conta os votos.
   5. O servidor pode assinar as confirmações de recebimento com a chave privada para garantir a autenticidade.

## Considerações Finais

O **RSA** oferece uma excelente maneira de garantir a **segurança** e **autenticidade** das comunicações em um sistema de votação, mesmo em ambientes com conectividade limitada ou inexistente, como é o caso de redes locais via **UDP**. Sua utilização garante que os dados de voto sejam protegidos contra interceptações e que a identidade de cada votante seja validada, tudo isso sem a necessidade de uma infraestrutura centralizada de comunicação segura.

Ao utilizar **RSA** no projeto de votação, é possível construir um sistema mais robusto, com forte proteção contra ataques de **interceptação** e **modificação** de dados.
