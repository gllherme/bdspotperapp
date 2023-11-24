def main_help():
    print('=== Comandos ===')
    print('criar\t\t\t\tEntra no modo de criação de nova playlist.')
    print('gerenciar\t\t\tEntra no modo de gerenciamento de playlists.')
    print('\n')


def criar_playlist_help():
    print('=== Comandos ===')
    print('add-faixa cod cod ...\t\tAdiciona as faixas à playlist')
    print('add-album cod cod ...\t\tAdiciona todas as faixas do album à playlist')
    print('remover cod cod ...\t\t\tRemove as faixas da playlist.')
    print('status\t\t\t\t\t\tMostra as faixas já adicionadas à playlist.')
    print('salvar\t\t\t\t\t\tSalva e cria a playlist no banco de dados.')
    print('voltar\t\t\t\t\t\tDescarta todas as alterações e sai do modo de criação/edição de playlist.')


def gerenciar_playlist_help():
    print('=== Comandos ===')
    print('selecionar cod\t\t\t\t\t\t\tSeleciona a playlist a ser editada.')
    print('\n')


def error_msg(cmd):
    print(f'Comando "{cmd}" inválido')
