# 📌 Guia de Estudo: Git e GitHub 🚀🔥

## 🎯 Introdução

Este documento é um guia de estudo sobre Git e GitHub, abordando desde conceitos básicos até comandos essenciais e boas práticas. O objetivo é ajudar iniciantes a entenderem como versionar seus projetos e colaborar com outros desenvolvedores.

![Git e GitHub](https://wac-cdn.atlassian.com/dam/jcr:d6e012d3-f2f5-4f1e-9646-ea7843a0c7db/hero.svg?cdnVersion=1455)

---

## 🔍 O que é Git?

Git é um sistema de controle de versão distribuído que permite rastrear mudanças no código-fonte e colaborar com outros desenvolvedores. Foi criado por Linus Torvalds em 2005 e é amplamente utilizado no desenvolvimento de software.

### ⭐ Principais Características

- **Distribuído**: Cada desenvolvedor tem uma cópia completa do repositório, permitindo trabalhar offline.
- **Rastreamento de Histórico**: Mantém um histórico detalhado de todas as alterações feitas no projeto.
- **Branching e Merging**: Facilita o desenvolvimento paralelo, permitindo que múltiplas pessoas trabalhem em diferentes funcionalidades ao mesmo tempo.
- **Eficiência**: Rápido e otimizado para grandes projetos, tornando o versionamento ágil e seguro.

![Fluxo de Trabalho Git](https://git-scm.com/images/about/index@2x.png)

---

## 🌐 O que é GitHub?

GitHub é uma plataforma online que hospeda repositórios Git, facilitando a colaboração entre desenvolvedores. Ele oferece recursos como pull requests, issues e integração com ferramentas de CI/CD.

### 🔄 Alternativas ao GitHub

- **GitLab** - Plataforma com recursos avançados de DevOps e CI/CD.
- **Bitbucket** - Mais utilizado por equipes que usam Atlassian (como Jira e Trello).
- **SourceForge** - Plataforma mais antiga para hospedagem de código.

GitHub permite que os desenvolvedores colaborem em projetos de código aberto e fechado, tornando a contribuição global mais acessível.

![Interface do GitHub](https://www.softwaretestinghelp.com/wp-content/qa/uploads/2020/09/Github-home-page.png)

---

## 🔧 Instalando o Git

Para instalar o Git, siga os passos abaixo:

### Windows:

1. Baixe o instalador no site oficial: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Execute o instalador e siga as instruções.
3. Durante a instalação, selecione a opção para adicionar o Git ao PATH do sistema.

### Linux:

```sh
sudo apt update
sudo apt install git -y
```

### MacOS:

```sh
brew install git
```

Verifique a instalação com:

```sh
git --version
```

Se o Git estiver instalado corretamente, o comando acima exibirá a versão instalada.

![Instalação do Git](https://git-scm.com/images/about/index@2x.png)

---

## ⚙️ Configuração Inicial do Git

Após instalar, configure seu nome e e-mail (importante para identificação de commits):

```sh
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Para verificar a configuração:

```sh
git config --list
```

Essa configuração é necessária para que cada commit feito possa ser identificado corretamente.

![Configuração do Git](https://www.journaldev.com/wp-content/uploads/2018/06/git-config-username-email.png)

**Dica**: Você também pode configurar localmente, usando os mesmos comandos sem a flag `--global`.

---

## 🚀 Trabalhando com GitHub

### 🔨 Criando um repositório no GitHub

1. Acesse [https://github.com/](https://github.com/)
2. Clique em "New repository".
3. Escolha um nome e defina as configurações desejadas (público/privado, README, licença etc.).

![Criando um Repositório no GitHub](https://docs.github.com/assets/images/help/repository/create-repository-name.png)

### 🔗 Conectar repositório local ao GitHub

```sh
git remote add origin <URL_DO_REPOSITORIO>
git branch -M main
git push -u origin main
```

![Comando Git Push](https://miro.medium.com/max/1200/1*fBLapN2-tTpyMLqPxbRn8A.png)

### 🧠 Comandos Git úteis

```sh
git init              # Inicializa um novo repositório Git
```
```sh
git clone <url>       # Clona um repositório remoto
```
```sh
git status            # Mostra o status das alterações
```
```sh
git add <arquivo>     # Adiciona arquivos ao staging
```
```sh
git commit -m "msg"   # Cria um commit com mensagem
```
```sh
git pull              # Puxa atualizações do repositório remoto
```
```sh
git push              # Envia alterações para o repositório remoto
```

### 🛠️ Fluxo de trabalho sugerido

1. `git pull` para obter atualizações.
2. Realize alterações locais.
3. `git add` para adicionar arquivos modificados.
4. `git commit -m` para salvar com mensagem.
5. `git push` para enviar as alterações.

---

## ⚔️ Lidando com Conflitos no Git 😬🛠️

Durante o trabalho colaborativo, é comum ocorrerem **conflitos** quando duas ou mais pessoas modificam a mesma parte do código. Isso geralmente acontece durante o `git merge` ou `git pull`.

### 💥 Quando acontece um conflito?

Um conflito ocorre, por exemplo, quando:

- Você e outra pessoa modificam a mesma linha de um arquivo e tentam dar `git push` ou `git merge`.
- Alguém remove um arquivo que você modificou.
- Branches com alterações incompatíveis são mescladas.

### 🧪 Como resolver um conflito?

1. Execute o comando que causou o conflito (geralmente `git pull` ou `git merge`).
2. O Git mostrará quais arquivos estão em conflito:

```sh
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

3. **Abra os arquivos com conflito**. Eles terão marcações assim:

```txt
<<<<<<< HEAD
Código da sua branch atual
=======
Código da outra branch
>>>>>>> outra-branch
```

4. **Edite o arquivo**, mantendo apenas a versão correta do código (ou mesclando as duas, se necessário).

5. Após resolver todos os conflitos, adicione os arquivos com:

```sh
git add <arquivo>
```

6. Finalize o merge com:

```sh
git commit
```

### ✅ Dicas para evitar conflitos

- Sempre dê `git pull` antes de começar a trabalhar.
- Comunique-se com o time sobre as partes do código que cada um está alterando.
- Divida as tarefas em pequenas branches e faça commits frequentes.
- Use ferramentas visuais como o **VS Code**, **Sourcetree** ou **GitKraken** para facilitar a resolução visual de conflitos.

### 📺 Vídeos úteis

- [Como Resolver Conflitos no Git (Rocketseat)](https://www.youtube.com/watch?v=etxqU2U9QRE)
- [Git Merge Conflicts Visualizado (DevDojo)](https://www.youtube.com/watch?v=JtIX3HJKwfo)

---

## 📚 Bibliografia e Referências

- Documentação oficial do Git: [https://git-scm.com/doc](https://git-scm.com/doc)
- Guia oficial do GitHub: [https://docs.github.com/](https://docs.github.com/)
- Livro "Pro Git" (gratuito): [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
- Guia completo sobre Git: [https://rogerdudler.github.io/git-guide/index.pt_BR.html](https://rogerdudler.github.io/git-guide/index.pt_BR.html)

### 🎥 Vídeos Recomendados no YouTube

- [Curso de Git e GitHub para iniciantes](https://www.youtube.com/watch?v=UBAX-13g8OM)
- [Git e GitHub na prática](https://www.youtube.com/watch?v=2alg7MQ6_sI)
- [Dominando o Git](https://www.youtube.com/watch?v=MwdH6h7mZrY)
- [Entenda Git de forma fácil (com GIFs explicativos)](https://dev.to/unseenwizzard/learn-git-concepts-not-commands-4gjc)

![GIF Explicativo de Git](https://wac-cdn.atlassian.com/dam/jcr:e4e12382-29ab-4b7e-90ad-0ac59d3802f4/Git-featurebranch-flow.png?cdnVersion=1463)

---

## 🧪 Extras: Dicas e Boas Práticas

- Sempre escreva mensagens de commit claras e objetivas.
- Use `.gitignore` para evitar subir arquivos desnecessários.
- Faça commits pequenos e frequentes para facilitar o rastreamento de mudanças.
- Mantenha o repositório organizado com branches nomeadas (ex: `feature/login`, `bugfix/footer`).
- Antes de subir código, execute `git pull` para evitar conflitos.
- Utilize Pull Requests e Code Reviews em projetos colaborativos.

---