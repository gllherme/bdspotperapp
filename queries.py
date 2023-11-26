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
    cursor.execute('SELECT f.cod_album, f.cod, f.descr, f.duracao '
                   'FROM faixa f, faixa_playlist fp '
                   'WHERE fp.cod_playlist=? AND f.cod=fp.cod_faixa', cod_playlist)
    faixas = list(map(tuple, cursor.fetchall()))
    return faixas


# a. Listar os álbuns com preço de compra maior que a média de preços de compra de todos os álbuns.
def get_consulta_a():
    cursor.execute('SELECT cod, descr, preco FROM album '
                   'GROUP BY cod, descr, preco '
                   'HAVING avg(preco) > (SELECT avg(preco) FROM album)')
    albuns = cursor.fetchall()
    return albuns


def get_consulta_b():
    return

