def generic_add(faixas, playlist, cods_to_add, index_to_compare):
    # parametro index_to_comapare indica qual atributo da faixa vai
    # ser utilizado como referencia para adiciona à playlist
    # index_to_compare = 0 -> adiciona pelo codigo do album
    # index_to_compare = 1 -> adiciona pelo codigo da faixa

    for f in faixas:
        if f[index_to_compare] in cods_to_add and f not in playlist:
            playlist.append(f)


def add_faixa(faixas, playlist, cods_to_add):
    generic_add(faixas, playlist, cods_to_add, 1)
    print('Faixas selecionadas, digite "status" para ver as faixas adicionadas.')


def add_album(faixas, playlist, cods_to_add):
    generic_add(faixas, playlist, cods_to_add, 0)
    print('Todas as faixas dos albuns selecionados adicionadas, digite "status" para ver as faixas adicionadas.')


def remover_faixas(playlist, cods_to_remove):
    ref_playlist = playlist.copy()
    for p in ref_playlist:
        if p[1] in cods_to_remove:
            playlist.remove(p)
    print('Faixas removidas, digite "status" para ver as faixas adicionadas.')
