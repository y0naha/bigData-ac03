# AC03 - BigData DynamoDB

Este script foi criado para receber informações das últimas músicas salvas na biblioteca do usuário do Spotify e armazenar essas informações em uma tabela DynamoDB na AWS.

## Pré-requisitos

Antes de usar este script, é necessário ter as seguintes ferramentas:

- [Python](https://www.python.org/downloads/) (versão 3.x)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
- [AWS CLI](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html) (Opcional caso for realizado a instalação do `aws-shell`)

Você também precisa de credenciais para acessar a API do Spotify e sua conta na AWS.

## Instalação

1. Clone o repositório em sua máquina local

2. Instale as dependências necessárias:

```shell
pip install boto3 spotipy aws-shell
```

3. Tutorial de como configurar e usar o [AWS CLI](https://www.youtube.com/watch?v=yl6G_wRmubs&ab_channel=PrimusLearning) (Opcional caso for realizado a instalação do `aws-shell`)

4. Utilizando o [aws-shell](https://pypi.org/project/aws-shell/) realize o comando:

```shell
aws-shell
```

5. O aws-shell usa as mesmas definições de configuração da AWS CLI. Se você nunca usou a AWS CLI antes, a maneira mais fácil de começar é executar o comando `configure`:

```shell
$ aws-shell
aws> configure
AWS Access Key ID [None]: your-access-key-id
AWS Secret Access Key [None]: your-secret-access-key
Default region name [None]: region-to-use (e.g us-west-2, us-west-1, etc).
Default output format [None]:
aws>
```
## Para rodar os scripts via Replit

1. Acesse o site: https://replit.com/
2. Cria sua conta
3. Importe este repositório
4. Siga este readme a partir da instalação das dependências
5. Caso ser der erro durante o processo do `configure` do `aws-shell`,saia do console da aws (aws> ) utilizando o comando `F10`, e digite os comandos:

```shell
ls -la /home/runner/bigData-ac03/venv/bin/aws
chmod +x /home/runner/bigData-ac03/venv/bin/aws
sudo aws-shell
```

6. Dê o comando `Yes` e prossiga com o passo 5 da instação

7. Para as credenciais do `.env` use o recurso `Secrets` do [Replit](https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables)
## Para rodar os scripts

```shell
python3 insert_products_dynamo.py
```

```shell
python3 insert_music_dynamo.py
```
