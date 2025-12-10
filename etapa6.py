import time
tentativas = {}


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


def extrair_ip(linha):
    partes = linha.split()
    for i, parte in enumerate(partes):
        if parte == "from" and i + 1 < len(partes):
            return partes[i + 1]
    return None


def registrar_tentativa(ip):
    if ip not in tentativas:
        tentativas[ip] = 1
    else:
        tentativas[ip] += 1
    print(f"registrar_tentativa: {ip} - Total: {tentativas[ip]}")
    return tentativas[ip]

def verificar_ataque(ip, total_tentativas, limite=5):
    if total_tentativas >= limite:
        print(f"🚨 ATAQUE DETECTADO do IP: {ip} – Tentativas: {total_tentativas}")

def detector_tempo_real(caminho_do_log):
    with open(caminho_do_log, "r") as file:
        while True:
            linha = file.readline()
            if not linha:
                time.sleep(0.5)
                continue
            ip = extrair_ip(linha)
            if ip:
                total_tentativas = registrar_tentativa(ip)
                verificar_ataque(ip, total_tentativas)



