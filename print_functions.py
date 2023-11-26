def print_albuns_e_faixas(albuns, faixas):
    for a in albuns:
        print(f'[{a[0]}] {a[1]}')
        for f in faixas:
            if f[0] == a[0]:
                print('\t', f'[{f[1]}] {f[2]}')
    print('\n')


def print_playlist_titles(playlists):
    print('=== Playlists ===')
    for p in playlists:
        print(f'[{p[0]}] {p[1]}')
    print('\n')


def print_playlist_details(playlist_info, playlist):
    print(f'[{playlist_info[0]}] {playlist_info[1]}')
    for p in playlist:
        print(f'\t[{p[1]}] {p[2]} ({p[3]}s)')
    print('\n')


def print_faixas_selecionadas(playlist):
    print('Faixas selecionadas:')

    for p in playlist:
        print(f'\t[{p[1]}] {p[2]}')


# albuns: (cod, descr, preco)
def print_consulta_a(albuns):
    print('Álbuns com preço de compra maior que a média de preços de compra de todos os álbuns: ')
    for a in albuns:
        print(f'[{a[0]}] {a[1]}\t\t\tR${a[2]}')
    print('\n')
