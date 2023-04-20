import socket
import sys

def main():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, e )
    except socket.error as e:
        print('A conexão falhou!')
        print('Erro: {}' .format(e))
        sys.exit()

    print('Socket criadp com sucesso')


    HostAlvo = input('Digite o Host ou Ip aa ser conectado: ')
    PortaAlvo = input('Digite a porta  a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP Conectado com Sucesso')
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou!')
        print('Erro: {}' .format(e))
        sys.exit()

if __name__ == '__main__':
    main()
