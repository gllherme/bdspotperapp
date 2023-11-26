from criar_playlist import criar_playlist
from gerenciar_playlists import gerenciar_playlists
from consultas import consultas
from help import main_help, error_msg


while True:
    print('=== BDSPotPer ===')
    print('[!] Digite "ajuda" para ver a lista de comandos ')
    cmd, *args = str.split(input('> '))

    match cmd:
        case 'criar':
            criar_playlist()
        case 'gerenciar':
            gerenciar_playlists()
        case 'consultas':
            consultas()
        case 'ajuda':
            main_help()
        case 'sair':
            break
        case _:
            error_msg(cmd)
