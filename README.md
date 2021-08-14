<h4 align="center"> 
	🚧 Projeto para análise de dados 1.0 🚀 em construção... 🚧
</h4>

# Projeto Análise de dados 🔥

## 💻 Sobre o projeto

Nesse projeto será demonstrado como criar uma pipelines para ingestão, processamento, análise e consumo de dados utilizando algumas das soluções mais utilizadas no mercado atualmente. Para isso utilizaremos:
- Python Flask (Aplicação principal que será acessada pelos usuários finais)
- PostegreSQL (Banco de dados que receberá os dados da aplicação)
- Debezium (Aplicação responsável por coletar os dados do banco de dados e enviar para um tópico do Kafka)
- Apache Kafka (Camada de fila de dados/eventos)
- Apache Flink (...)
- Apache Druid (Agregação e Armazenamento)
- Elasticsearch (Motor de busca/Armazenamento)
- Aplicação Python Consumer (Aplicação responsável por ler os eventos do Kafka e enviar para o Elasticsearch)
- Apache Superset (Painel analítico para monitoramento do fluxo de dados)
- Docker (Gestão dos containers do projeto)

### Diagrama v1
![el-notifier](apoio/projeto_dados.png)

### Web
<h4 align="center">
    🚧 Em construção... 🚧
    Tela de demonstração do mecanismo de busca
</h4>

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python Flask][flask]
- [PostegreSQL][postgresql]
- [Debezium][debezium]
- [Apache Kafka][kafka]
- [Apache Flink][flink]
- [Apache Druid][druid]
- [Elasticsearch][elasticsearch]
- [Aplicação Python Consumer][python-kafka]
- [Apache Superset][superset]
- [Docker][Docker]

## 🚀 Como executar o projeto

1. Execute o arquivo flask_compose
2. Debezium / Kafka
3. Apache Flink
4. Elasticsearch / python engine
5. Druid
6. Superset

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Docker][Docker]
- Além disto é bom ter um editor para trabalhar com o código como [VSCode][vscode], apesar de não ser obrigatório.


### 🎲 Rodando o Backend (Servidor Dev)

```bash
# Clone este repositório
$ git clone https://github.com/j040n3t0/el-tinder.git

# Acesse a pasta do projeto no terminal/cmd
$ cd el-tinder

# Iniciando container Docker
$ docker-compose up

# iniciando o serviço NodeJs
$  yarn dev;

# O serviço XXXX inciará na porta:XXXX - acesse http://localhost:XXXX
```

### 🧭 Rodando a aplicação web (Front End)

🚧 Em construção... 🚧

### 📱Rodando a aplicação mobile

🚧 Em construção... 🚧

## 🧠 Idealizadores

Responsáveis pelo projeto:
- João Neto [joaojose.ti@gmail.com]

## 😯 Como contribuir para o projeto

👋🏽 [Entre em contato!](LINK)

<!-- ## 📝 Licença -->


<h4 align="center"> 
	🚧 api-note-elasticStack 1.0 🚀 em construção... 🚧
</h4>

[vscode]: https://code.visualstudio.com/
[docker]: 