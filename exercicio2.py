def colorir(texto,cor):
    cores = {"VERMELHO": "\033[31m","VERDE": "\033[32m","AMARELO": "\033[33m","AZUL": "\033[34m","ROXO": "\033[35m","RESET": "\033[0m"}
    return cores[cor] + texto + cores["RESET"]