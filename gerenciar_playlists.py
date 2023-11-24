from help import error_msg
from help import gerenciar_playlist_help, criar_playlist_help
from queries import get_playlist, get_faixas_from_playlist, get_all_playlists, get_albuns_e_faixas
from print_functions import print_playlist_titles, print_playlist_details, print_albuns_e_faixas, print_faixas_selecionadas
from edit_playlist_functions import add_faixa, add_album, remover_faixas
from dbconnection import cursor


def atualizar_playlist(cod_playlist, original_playlist, playlist):
    remover = list(set(original_playlist) - set(playlist))
    adicionar = list(set(playlist) - set(original_playlist))

    remover_faixa_playlist_params = [(cod_playlist, r[1]) for r in remover]
    if remover_faixa_playlist_params:
        cursor.executemany('DELETE FROM faixa_playlist WHERE cod_playlist=? and cod_faixa=?', remover_faixa_playlist_params)

    adicionar_faixa_playlist_params = [(cod_playlist, a[1]) for a in adicionar]
    if adicionar_faixa_playlist_params:
        cursor.executemany('INSERT INTO faixa_playlist(cod_playlist, cod_faixa) VALUES (?, ?)', adicionar_faixa_playlist_params)

    cursor.commit()


def gerenciar_playlist_selecionada(cod_playlist):
    albuns, faixas = get_albuns_e_faixas()

    selected_playlist_info = get_playlist(cod_playlist)
    nome_playlist = selected_playlist_info[1]
    original_playlist = get_faixas_from_playlist(cod_playlist)
    playlist = original_playlist.copy()

    print('=== Playlist ===')
    print_playlist_details(selected_playlist_info, playlist)

    print('=== Faixas Disponíveis ===')
    print_albuns_e_faixas(albuns, faixas)

    criar_playlist_help()

    while True:
        cmd_gerenciar, *args = str.split(input(f'[Gerenciando] {nome_playlist} > '))
        args = list(map(int, args))

        match cmd_gerenciar:
            case 'add-faixa':
                add_faixa(faixas, playlist, args)
            case 'add-album':
                add_album(faixas, playlist, args)
            case 'remover':
                remover_faixas(playlist, args)
            case 'status':
                print_faixas_selecionadas(playlist)
            case 'salvar':
                atualizar_playlist(cod_playlist, original_playlist, playlist)
                break
            case 'voltar':
                break
            case _:
                error_msg(cmd_gerenciar)


def gerenciar_playlists():
    playlists = get_all_playlists()
    print_playlist_titles(playlists)
    gerenciar_playlist_help()

    while True:
        cmd_gerenciar, *args = str.split(input(f'[Gerenciando] > '))

        match cmd_gerenciar:
            case 'selecionar':
                if len(args) > 0: gerenciar_playlist_selecionada(args[0])
                else: print('Informe o codigo da playlist selecionada')
            case 'voltar':
                break
            case _:
                error_msg(cmd_gerenciar)
