import os
from dotenv import load_dotenv

# Link para documentação de como criar app no Spotify para ter as credenciais
# https://developer.spotify.com/documentation/web-api

# carrega as variáveis do arquivo .env
load_dotenv()

# acessa as variáveis do arquivo .env como se fossem variáveis normais em Python
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")
tabela_musicas = os.getenv("tabela_musicas")
tabela_produtos = os.getenv("tabela_produtos")