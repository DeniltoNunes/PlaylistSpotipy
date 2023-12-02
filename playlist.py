import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação na API do Spotify
client_credentials_manager = SpotifyClientCredentials(client_id='1f32d0c2f5254d6184a3cdac7f55e8e7', client_secret='727f2b8e54c44193bd37b0fd66f28837')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Lista de nomes das músicas
nomes_das_musicas = [
]

id_musicas = []
idUsuario = ''
nome_playlist = ''

def login():
    print("Olá, tudo bem?")
    print("Antes de começarmos a criar sua playlist precisamos de alguns dados.")
    autorizacao = str(input('Você autorizou a criação de playlists para o seu perfil?\n')).upper()
    validacao = False
    while validacao == False:
        if (autorizacao == 'SIM'):
            print('Muito obrigado :D')
            validacao = True
            id()
        elif (autorizacao == 'NAO') or (autorizacao == 'NÃO'):
            print('Que penas :(')
            print('Para aprender a autorizar leia o README.md')
            validacao = True  
        else:
            while (autorizacao != ('NÃO') and autorizacao != ('SIM') and autorizacao != ('NAO')):
                print("Mil perdões, a sua resposta foi inválida.")
                autorizacao = str(input('Você autorizou a criação de playlists para o seu perfil?\n')).upper()
            validacao = False        

def id():
    validacao = False
    print('Para continuarmos preciso do seu Id de Perfil')
    autorizacao = str(input('Você sabe o seu Id do Perfil?\n')).upper()
    while validacao == False:
        if (autorizacao == 'SIM'):
            global idUsuario
            idUsuario = input('Qual o seu Id de Usuário?\n')
            validacao = True
            criacao()
        elif (autorizacao == 'NAO') or (autorizacao == 'NÃO'):
            print('Que penas :(')
            print('Para descobrir como leia o README.md')
            validacao = True  
        else:
            while (autorizacao != ('NÃO') and autorizacao != ('SIM') and autorizacao != ('NAO')):
                print("Mil perdões, a sua resposta foi inválida.")
                autorizacao = str(input('Você sabe o seu Id do Perfil?\n')).upper()
            validacao = False
            
            
def criacao():
    validacao = False
    print('Ok, iremos começar a criar a sua Playlist')
    global nome_playlist
    nome_playlist = input(str("Qual nome você gostaria de dar para a sua Playlist?\n"))
    print('Muito obrigado!')
    autorizacao = str(input('Você já adicionou suas músicas?\n')).upper()
    while validacao == False:
        if (autorizacao == 'SIM'):
            print('Ok, iremos começar a criação da sua Playlist')
            validacao = True
            playlist()
        elif (autorizacao == 'NAO') or (autorizacao == 'NÃO'):
            print('Sem problemas, vamos adicionar as suas músicas!')
            musicas()
            validacao = True  
        else:
            while (autorizacao != ('NÃO') and autorizacao != ('SIM') and autorizacao != ('NAO')):
                print("Mil perdões, a sua resposta foi inválida.")
                autorizacao = str(input('Você já adicionou suas músicas?\n')).upper()
            validacao = False
            
def musicas():
    print('Pode adicionar quantas músicas você quiser, basta apenas me dizer o nome.')
    musica = str(input('Qual música você quer adicionar? \nCaso não queira mais adicionar digite "Seguinte."'))
    while musica.upper() != 'SEGUINTE':
        nomes_das_musicas.append(musica)
        musica = str(input('Qual a proxima música você quer adicionar? \nCaso não queira mais adicionar digite "Seguinte."'))
    playlist()

def playlist():
    if len(nomes_das_musicas) == 0:
        print('Músicas insuficientes.')
        musicas()
    else:
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
    playlist = sp.user_playlist_create(user=idUsuario, name=nome_playlist, public=False)
    # Adicionar músicas à playlist
    sp.user_playlist_add_tracks(user=idUsuario, playlist_id=playlist['id'], tracks=id_musicas)
            
login()