# Spotify to DynamoDB

Este script foi criado para receber informações das últimas músicas salvas na biblioteca do usuário do Spotify e armazenar essas informações em uma tabela DynamoDB na AWS.

## Pré-requisitos

Antes de usar este script, é necessário ter as seguintes ferramentas:

- [Python](https://www.python.org/downloads/) (versão 3.x)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
- [AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html)

Você também precisa de credenciais para acessar a API do Spotify e sua conta na AWS.

## Instalação

1. Clone o repositório em sua máquina local

2. Instale as dependências necessárias:

```shell
pip install boto3 spotipy
```

## Para rodar os scripts

```shell
python3 insert_products_dynamo.py
```

```shell
python3 insert_music_dynamo.py
```
