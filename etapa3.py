import time
with open("ssh.log", "w") as file:
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")
    file.write("Dec 12 10:02:13 server sshd[1111]: Failed password for admin from 88.77.66.55 port 40101\n")
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")
    file.write("Dec 12 10:02:13 server sshd[1111]: Failed password for admin from 88.77.66.55 port 40101\n")
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")
    file.write("Dec 12 10:02:13 server sshd[1111]: Failed password for admin from 88.77.66.55 port 40101\n")
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")
    file.write("Dec 12 10:02:13 server sshd[1111]: Failed password for admin from 88.77.66.55 port 40101\n")
    file.write("Dec 12 10:02:12 server sshd[1111]: Failed password for root from 123.123.123.1 port 44222\n")


def ler_em_tempo_real(caminho_do_log):
    with open(caminho_do_log, "r") as file:
        while True:
            linha = file.readline()
            if not linha:
                time.sleep(0.5)

def extrair_ip(linha):
    partes = linha.split()
    for i, parte in enumerate(partes):
        if parte == "from" and i + 1 < len(partes):
            return partes[i + 1]
    return None