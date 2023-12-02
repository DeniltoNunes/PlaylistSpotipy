import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação na API do Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='SuaClientID', client_secret='SuaClientSecret')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Lista de nomes das músicas
nomes_das_musicas = [

]

id_musicas = []

# Para cada música na lista, busca o ID correspondente
for nome_da_musica in nomes_das_musicas:
    # Realiza a busca na API do Spotify
    results = sp.search(q=nome_da_musica, limit=1, type='track')

    # Obtém o ID da primeira música encontrada na busca
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        id_musicas.append(track_id)
    else:
        print(f"Música '{nome_da_musica}' não encontrada.")

# Criar uma nova playlist
playlist = sp.user_playlist_create(user='IDUser', name='playlist teste', public=False)

# Adicionar músicas à playlist
sp.user_playlist_add_tracks(user='IDUser', playlist_id=playlist['id'], tracks=id_musicas)