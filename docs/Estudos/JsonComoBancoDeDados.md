# Usando Json como um banco de dados
## O que é Json?

Json é uma forma de representar dados, o nome vem de Javascript Object Notation, ela consistente em separar os dados em pares de Chave e Valor.
o uso de tabelas de símbolo é bem comum em outras línguagens, como em c, c++, c#, python, java, e outras, por conta disso praticamente todas as
principais linguagens do mercado possuem alguma biblioteca que lide com Json, fazendo com que seja uma formatação ideal para troca de dados, atualmente
o json vai muito além do javascript e se tornou formatação independente de linguagem.

## Exemplo simples de Json

```json
{
    {
        "nome": "nome1",
        "CPF" : 12345678910,
        "emails" : [ "email_1", "email_2", "email_3" ]
    },
    {
        "nome": "nome2",
        "CPF" : 23456789110,
        "emails" : [ "email_4", "email_5", "email_6" ]
    }
}

```

## Json em Python
Python tem uma biblioteca chamada json, que como o nome indica serve para tratar dados com essa formatação, como visto no exemplo acima a formatação do json
se assemelha muito ao dicionário em python, e os arrays representados por '[]' se assemelham muito as listas.

### principais funções da biblioteca json
**json.dumps()**
recebe uma estrutura em python, como um dicionário ou uma lista e transforma em uma string formatada em json

**json.loads()**
lê uma string formatada em json e transforma em uma estrutura em python

**json.dump()**
recebe uma estrutura em python, e transforma em um arquivo formatado em json

**json.load()**
lê um arquivo formatado em json e transforma em uma estrutura em python

com os métodos acima se torna fácil fazer conversões entre json e estruturas em python

### como usar o json como um banco de dados?

a ideia é relativamente simples, podemos ter um arquivo em json que armazena todos os dados que queremos, usando json.load() pegamos esses dados e podemos manipulá-los
da maneira que quisermos, após isso com a função json.dump() armazenamos o resultado

### exemplo de manipulação de dados com json
A seguir fiz um exemplo simples apenas para ilustrurar como seria feito uma manipulação de dados usando json

#### exemplo de arquivo em json
_antes da modificação_
```json
{
  "votantes": {
    "id_12345": {
      "votos": [
        "a favor",
        "a favor",
        "nulo",
        "contra"
      ]
    },
    "id_54321": {
      "votos": [
        "contra",
        "nulo",
        "contra",
        "a favor"
      ]
    },
    "id_13578": {
      "votos": [
        "a favor",
        "a favor",
        "a favor",
        "a favor"
      ]
    },
    "id_93824": {
      "votos": [
        "contra",
        "contra",
        "a favor",
        "contra"
      ]
    },
    "id_69503": {
      "votos": [
        "nulo",
        "nulo",
        "contra",
        "a favor"
      ]
    }
  },
  "dados gerais": {
    "votação 1": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 1
    },
    "votação 2": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 1,
      "qtd de votos anulados": 2
    },
    "votação 3": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 1
    },
    "votação 4": {
      "qtd de votos a favor": 3,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 0
    }
  }
}
```
#### exemplo de programa em python
abaixo fiz um programa simples que adiciona os dados de uma votação, nesse caso a votação número 5,
o documento acima é processado e tudo com {} se torna um dicionário, que possui pares chave e valor,
a sua syntax é chave : valor, os items com [] se tornam listas.
```python
import json

def adicionar_voto(data, id_do_usuario, voto, votacao):
    data["votantes"][id_do_usuario]["votos"].append(voto)
    if(voto == "a favor"):
        data["dados gerais"][votacao]['qtd de votos a favor'] += 1
    elif(voto == "contra"):
        data["dados gerais"][votacao]['qtd de votos contra'] += 1
    else:
        data["dados gerais"][votacao]['qtd de votos anulados'] += 1

def criar_nova_votacao(data, votacao):
    dicionario = {'qtd de votos a favor': 0, 'qtd de votos contra' : 0, 'qtd de votos anulados': 0}
    data['dados gerais'][votacao] = dicionario

with open('db.json', 'r') as banco_de_dados:
    data = json.load(banco_de_dados)
    #lógica que manipula e altera os dados
    criar_nova_votacao(data, 'votação 5')
    adicionar_voto(data, 'id_12345', 'contra', 'votação 5')
    adicionar_voto(data, 'id_54321', 'a favor', 'votação 5')
    adicionar_voto(data, 'id_13578', 'nulo', 'votação 5')
    adicionar_voto(data, 'id_93824', 'contra', 'votação 5')
    adicionar_voto(data, 'id_69503', 'contra', 'votação 5')

with open('db.json', 'w') as banco_de_dados:
    json.dump(data, banco_de_dados, ensure_ascii=False, indent=2)
```
  
_após a modificação_
```json
{
  "votantes": {
    "id_12345": {
      "votos": [
        "a favor",
        "a favor",
        "nulo",
        "contra",
        "contra"
      ]
    },
    "id_54321": {
      "votos": [
        "contra",
        "nulo",
        "contra",
        "a favor",
        "a favor"
      ]
    },
    "id_13578": {
      "votos": [
        "a favor",
        "a favor",
        "a favor",
        "a favor",
        "nulo"
      ]
    },
    "id_93824": {
      "votos": [
        "contra",
        "contra",
        "a favor",
        "contra",
        "contra"
      ]
    },
    "id_69503": {
      "votos": [
        "nulo",
        "nulo",
        "contra",
        "a favor",
        "contra"
      ]
    }
  },
  "dados gerais": {
    "votação 1": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 1
    },
    "votação 2": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 1,
      "qtd de votos anulados": 2
    },
    "votação 3": {
      "qtd de votos a favor": 2,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 1
    },
    "votação 4": {
      "qtd de votos a favor": 3,
      "qtd de votos contra": 2,
      "qtd de votos anulados": 0
    },
    "votação 5": {
      "qtd de votos a favor": 1,
      "qtd de votos contra": 3,
      "qtd de votos anulados": 1
    }
  }
}
```

## Conclusão
Apesar de diversas desvantagens comparado com um banco de dados propriamente dito, para aplicações pequenas e simples, o uso de Json é
uma boa opção, ele é simples de usar, flexível, cumpre com o objetivo de serializar dados e possui ampla documentação.

### Referências:
https://www.json.org/json-en.html   
https://docs.python.org/3/library/json.html
