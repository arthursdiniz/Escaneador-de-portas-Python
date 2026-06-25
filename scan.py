import socket
import time
from concurrent.futures import ThreadPoolExecutor
from sys import argv, exit

portas_abertas = []


def scan_port(ip, porta):


    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.3)

            resultado = sock.connect_ex((ip, porta))

            if resultado == 0:

                try:
                    servico = socket.getservbyport(porta)
                except:
                    servico = "Desconhecido"

                print(f"[+] Porta {porta:<5} Aberta ({servico})")

                portas_abertas.append((porta, servico))

    except:
        pass


def port_scan(alvo, porta_inicial, porta_final):

    try:
        ip = socket.gethostbyname(alvo)
    except socket.gaierror:
        print("Host inválido.")
        exit()

    print("=" * 50)
    print(f"Alvo : {alvo}")
    print(f"IP   : {ip}")
    print(f"Portas: {porta_inicial} - {porta_final}")
    print("=" * 50)

    inicio = time.time()

    with ThreadPoolExecutor(max_workers=100) as executor:

        for porta in range(porta_inicial, porta_final + 1):
            executor.submit(scan_port, ip, porta)

    fim = time.time()

    print("\n" + "=" * 50)

    if portas_abertas:

        print("Portas encontradas:\n")

        for porta, servico in sorted(portas_abertas):
            print(f"{porta:<6} {servico}")

    else:
        print("Nenhuma porta aberta encontrada.")

    print("\nTempo de execução: {:.2f} segundos".format(fim - inicio))


if __name__ == "__main__":

    if len(argv) != 4:
        print("Uso:")
        print("python scan.py HOST PORTA_INICIAL PORTA_FINAL")
        exit()

    alvo = argv[1]
    porta_inicial = int(argv[2])
    porta_final = int(argv[3])

    port_scan(alvo, porta_inicial, porta_final)