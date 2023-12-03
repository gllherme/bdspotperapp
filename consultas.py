from queries import get_consulta_a, get_consulta_c, get_consulta_d
from print_functions import print_consulta_a, print_consulta_c, print_consulta_d
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
                print_consulta_c(get_consulta_c())
            case '4':
                print_consulta_d(get_consulta_d())
            case 'voltar':
                break
            case _:
                error_msg(cmd)
