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


def get_consulta_c():
    cursor.execute("SELECT nome, "
                   "(SELECT count(fc.cod_compositor) FROM faixa_compositor fc "
                   "INNER JOIN faixa_playlist fp ON fp.cod_faixa=fc.cod_faixa "
                   "WHERE fc.cod_compositor=cod) AS 'qtd' "
                   "FROM compositor "
                   "ORDER BY qtd DESC")

    results = cursor.fetchall()
    return results


def get_consulta_d():
    cursor.execute('SELECT p.nome, dbo.fn_Check_Composicao_Periodo_Playlist(p.cod), p.cod AS Checks FROM playlist p ')
    results = cursor.fetchall()

    filtered = [(r[2], r[0]) for r in results if r[1]]

    return filtered


get_consulta_d()
