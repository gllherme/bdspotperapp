from queries import get_consulta_a
from print_functions import print_consulta_a
from help import consultas_help, error_msg


def consultas():
    consultas_help()

    while True:
        cmd, *args = str.split(input('[Consultas] > '))

        match cmd:
            case '1':
                print_consulta_a(get_consulta_a())
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case 'voltar':
                break
            case _:
                error_msg(cmd)
