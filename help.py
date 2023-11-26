def main_help():
    print('=== Comandos ===')
    print('criar\t\t\t\tEntra no modo de criação de nova playlist.')
    print('gerenciar\t\t\tEntra no modo de gerenciamento de playlists.')
    print('consultas\t\t\tVer consultas predefinidas.')
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


def consultas_help():
    print('=== Consultas ===')
    print('[1] Álbuns com o preço de compra maior que a média de preços de compra de todos os álbuns.')
    print('[2] Gravadora com maior número de playlists que possuem pelo menos uma faixa composta pelo compositor Dvorack')
    print('[3] Compositor com o maior número de faixas nas playlists existentes.')
    print('[4] Playlists cujas faixas (todas) tem tipo de composição "Concerto" e período "Barroco".')
    print('\n')
    print('Digite o número da consulta a ser realizada.')


def error_msg(cmd):
    print(f'Comando "{cmd}" inválido')
