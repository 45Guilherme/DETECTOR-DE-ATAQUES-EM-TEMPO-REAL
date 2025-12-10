import time
tentativas = {}
ips_bloqueados = set()



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
        if ip in ips_bloqueados:
            print(f"⛔ Tentativa ignorada (IP bloqueado): {ip}")
            return tentativas.get(ip, 0)
        tentativas[ip] = tentativas.get(ip, 0) + 1
        msg = f"registrar_tentativa: {ip} - Total: {tentativas[ip]}"
        print(colorir(msg, "AMARELO"))
        return tentativas[ip]
     


def verificar_ataque(ip, total_tentativas, limite=5):
    if total_tentativas >= limite:
        msg = f"🚨 ATAQUE DETECTADO do IP: {ip} Tentativas: {total_tentativas}"
        print(colorir(msg, "VERMELHO"))
        ip_bloqueado(ip)

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

def ip_bloqueado(ip):
    if ip not in ips_bloqueados:
        ips_bloqueados.add(ip)
        msg = f"🔒 IP bloqueado: {ip}"
        print(colorir(msg, "ROXO"))

def colorir(texto,cor):
    cores = {"VERMELHO": "\033[31m","VERDE": "\033[32m","AMARELO": "\033[33m","AZUL": "\033[34m","ROXO": "\033[35m","RESET": "\033[0m"}
    return cores.get(cor, cores["RESET"]) + texto + cores["RESET"]

detector_tempo_real("ssh.log")





        

