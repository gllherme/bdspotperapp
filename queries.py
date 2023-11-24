from dbconnection import cursor


def get_albuns_e_faixas():
    cursor.execute('SELECT cod, descr FROM album')
    albuns = cursor.fetchall()

    cursor.execute('SELECT cod_album, cod, descr, duracao FROM faixa')
    faixas = list(map(tuple, cursor.fetchall()))

    return albuns, faixas


def get_all_playlists():
    cursor.execute('SELECT cod, nome FROM playlist')
    playlists = cursor.fetchall()
    return playlists


def get_playlist(cod):
    cursor.execute('SELECT cod, nome FROM playlist WHERE cod=?', cod)
    playlist = cursor.fetchone()
    return playlist


def get_faixas_from_playlist(cod_playlist):
    cursor.execute('select f.cod_album, f.cod, f.descr, f.duracao '
                   'from faixa f, faixa_playlist fp '
                   'where fp.cod_playlist=? and f.cod=fp.cod_faixa', cod_playlist)
    faixas = list(map(tuple, cursor.fetchall()))
    return faixas
