# AES-GCM no Projeto de Votação Presencial com Rede Local

## Introdução

O **AES-GCM** (Advanced Encryption Standard - Galois/Counter Mode) é um algoritmo de criptografia simétrica amplamente utilizado para proteger dados em sistemas de comunicação. No contexto de um aplicativo de **votação presencial**, o AES-GCM pode ser utilizado para garantir a **confidencialidade** e **integridade** das mensagens (votos) enviadas entre os dispositivos na rede local.

## O que é AES-GCM?

O **AES-GCM** combina o algoritmo de criptografia **AES** (padrão globalmente aceito para criptografia simétrica) com o modo de operação **Galois/Counter Mode (GCM)**. Ele oferece:

1. **Criptografia**: Protege o conteúdo dos dados (voto).
2. **Autenticação**: Garante que os dados não foram alterados durante o envio, por meio de uma **tag de autenticação**.

### Como o AES-GCM funciona?

1. **Chave de criptografia**: Um valor secreto compartilhado entre o remetente e o receptor.
2. **Nonce**: Um número único para cada mensagem, usado para garantir que a criptografia seja única a cada envio, evitando ataques de repetição (replay attacks).
3. **Texto claro (plaintext)**: A mensagem (voto) que será criptografada.
4. **Dados autenticados (AAD)**: Dados adicionais que são protegidos contra alterações, mas não criptografados (por exemplo, identificador da sessão ou tipo de votação).
5. **Ciphertext**: O texto criptografado que é enviado na rede.
6. **Tag de autenticação**: Um valor gerado durante o processo de criptografia que é usado para verificar a integridade da mensagem ao ser recebida.

## Como o AES-GCM pode ser utilizado no projeto?

No contexto do aplicativo de votação presencial, o **AES-GCM** será utilizado para proteger as mensagens (votos) enviadas entre os dispositivos via **UDP** na rede local.

### 1. **Proteção dos votos**
Cada voto, antes de ser enviado pela rede local, será **criptografado** utilizando o AES-GCM. A mensagem de voto (por exemplo, "a favor", "contra" ou "abstenção") será criptografada com a chave secreta e um **nonce único** gerado para garantir que cada voto seja único e seguro.

### 2. **Autenticação e integridade**
Além da criptografia, o AES-GCM também **autentica** os votos, garantindo que os dados não foram alterados durante o envio. A **tag de autenticação** gerada junto com o ciphertext será verificada pelo servidor ao receber o voto. Caso a tag não corresponda ou o voto tenha sido alterado, ele será rejeitado.

### 3. **Uso do Nonce**
Para evitar ataques de repetição, cada pacote de voto será enviado com um **nonce único**. O **nonce** será gerado aleatoriamente a cada envio, garantindo que, mesmo que o voto seja o mesmo, o resultado da criptografia seja diferente a cada vez. O servidor pode verificar o nonce para garantir que não houve tentativas de retransmitir um voto de forma fraudulenta.

### 4. **Segurança e privacidade**
- **Confidencialidade**: Apenas o servidor, que possui a chave de criptografia, pode **descriptografar** o voto, garantindo a **privacidade** da votação.
- **Integridade**: O servidor pode verificar se a mensagem foi alterada durante o transporte, validando a tag de autenticação.
- **Proteção contra ataques de replay**: O uso do nonce impede que uma mensagem seja repetida ou retransmitida de forma maliciosa.

### 5. **Estrutura do Pacote UDP com AES-GCM**
Ao enviar o voto, o pacote UDP conterá:
- **Nonce**: Um valor único gerado para o voto.
- **Ciphertext**: O voto criptografado com AES-GCM.
- **Tag de autenticação**: Uma tag que permite verificar a integridade da mensagem.
- **Dados autenticados (AAD)**: Metadados que ajudam a garantir a autenticidade da votação, como o ID da sessão ou o tipo de votação.

## Benefícios do AES-GCM para o Projeto

- **Segurança**: Garante que os votos sejam protegidos contra espionagem e manipulação.
- **Eficiência**: O AES-GCM é rápido e eficiente, sendo ideal para um ambiente com recursos limitados como em redes locais.
- **Facilidade de Implementação**: Com bibliotecas modernas, como `cryptography` em Python, a implementação do AES-GCM pode ser realizada de forma simples e eficaz.
- **Autenticação e Criptografia em um único passo**: Não há necessidade de usar dois algoritmos separados para criptografar e autenticar, o que simplifica o sistema e melhora o desempenho.

## Considerações Importantes

- **Chave de Criptografia**: A chave de criptografia (AES 256 bits, por exemplo) deve ser mantida segura. Ela é a base para a criptografia e deve ser compartilhada de forma segura entre os dispositivos participantes.
- **Nonce Único**: Cada mensagem deve ter um nonce único. Se o nonce for reutilizado, isso pode comprometer a segurança do sistema.
- **Validação da Tag de Autenticação**: Ao receber o pacote de voto, o servidor deve validar a tag de autenticação para garantir que os dados não foram alterados.

## Conclusão

O **AES-GCM** é uma excelente escolha para garantir a **segurança**, **confidencialidade** e **integridade** dos votos em sistemas de votação em redes locais. Ele protege os dados contra alterações e interceptações, garantindo que cada voto seja legítimo e que o processo de votação seja transparente e seguro.

Ao utilizar AES-GCM com **nonces únicos** e **tag de autenticação**, o sistema estará protegido contra ataques comuns, como **replay attacks** e **modificação de dados**, garantindo uma experiência de votação confiável e segura.
