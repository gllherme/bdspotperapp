from edit_playlist_functions import add_faixa, add_album, remover_faixas
from queries import get_albuns_e_faixas
from print_functions import print_albuns_e_faixas, print_faixas_selecionadas
from help import criar_playlist_help, error_msg
from dbconnection import cursor


def salvar_nova_playlist(nome_playlist, playlist):
    cursor.execute('SELECT TOP 1 cod FROM playlist ORDER BY cod DESC')
    last_cod = cursor.fetchone()[0]
    cod = last_cod + 1  # incrementar a primary key

    duracao = 0
    for p in playlist:
        duracao += p[3]

    playlist_params = (cod, nome_playlist, duracao)
    cursor.execute("INSERT INTO playlist(cod, nome, duracao_total) VALUES (?, ?, ?)", playlist_params)

    faixa_playlist_params = [(cod, p[1]) for p in playlist]
    cursor.executemany('INSERT INTO faixa_playlist(cod_playlist, cod_faixa) VALUES (?, ?)', faixa_playlist_params)

    cursor.commit()


def criar_playlist():
    albuns, faixas = get_albuns_e_faixas()

    nome_playlist = input('Escolha um nome para a playlist: ')

    print('=== Albuns e faixas ===')
    print_albuns_e_faixas(albuns, faixas)
    criar_playlist_help()

    playlist = []

    while True:
        cmd_playlist, *args = str.split(input(f'[Criando] {nome_playlist} > '))
        args = list(map(int, args))

        match cmd_playlist:
            case 'add-faixa':
                add_faixa(faixas, playlist, args)
            case 'add-album':
                add_album(faixas, playlist, args)
            case 'remover':
                remover_faixas(playlist, args)
            case 'status':
                print_faixas_selecionadas(playlist)
            case 'salvar':
                salvar_nova_playlist(nome_playlist, playlist)

                print(f'Playlist {nome_playlist} criada e salva no banco de dados!')
                print('Voltando ao menu principal...')
                break
            case 'voltar':
                break
            case _:
                error_msg(cmd_playlist)
