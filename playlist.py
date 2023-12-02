""" import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação na API do Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='1f32d0c2f5254d6184a3cdac7f55e8e7', client_secret='727f2b8e54c44193bd37b0fd66f28837')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

nome_playlist = input(str("Qual será o nome da sua Playlist?"))

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
playlist = sp.user_playlist_create(user=idUsuario, name= nome_playlist, public=False)

# Adicionar músicas à playlist
sp.user_playlist_add_tracks(user=idUsuario, playlist_id=playlist['id'], tracks=id_musicas) """



def login():
    print("Olá, tudo bem?")
    print("Antes de começarmos a criar sua playlist precisamos de alguns dados.")
    autorizacao = str(input('Você autorizou a criação de playlists para o seu perfil?')).upper()
    validacao = False
    while validacao == False:
        if (autorizacao == 'SIM'):
            print('Muito obrigado :D')
            idUsuario = input('Qual o seu Id de Usuário?')
            validacao = True
        elif (autorizacao == 'NAO') or (autorizacao == 'NÃO'):
            print('Que penas :(')
            print('Para aprender a autorizar leia o README.md')
            validacao = True  
        else:
            while (autorizacao != ('NÃO') and autorizacao != ('SIM') and autorizacao != ('NAO')):
                print("Mil perdões, a sua resposta foi inválida.")
                autorizacao = str(input('Você autorizou a criação de playlists para o seu perfil?')).upper()
            validacao = False        
    
login()