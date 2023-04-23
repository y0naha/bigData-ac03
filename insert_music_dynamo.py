import boto3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credential import client_id, client_secret, redirect_uri, tabela_musicas

# Crie uma instância de autenticação da API do Spotify
auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                    redirect_uri=redirect_uri, scope='user-library-read')
sp = spotipy.Spotify(auth_manager=auth)

# Recebe as musicas
tracks = sp.current_user_saved_tracks(limit=10)

# Cria conexão com aws - dynamodb
boto3.setup_default_session(profile_name="default")
dynamodb_client = boto3.client("dynamodb")
table_name = tabela_musicas

for track in tracks['items']:
    duration = track['track']['duration_ms'] // 1000
    minutes, seconds = divmod(duration, 60)

    response = dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "nome_musica": {"S": track['track']['name']},
            "artista": {"S": track['track']['artists'][0]['name']},
            "album": {"S": track['track']['album']['name']},
            "ano": {"N": track['track']['album']['release_date'][:4]},
            "duracao": {"S": "{:02d}:{:02d}".format(minutes, seconds)},
        }
    )
