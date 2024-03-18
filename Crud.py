import sqlite3
import os
import time

cor_vermelha = "\033[91m"
cor_laranja = "\33[33m"
reset_cor = "\033[0m"

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Função para inserir um novo usuário
def adicionar_usuario(nome, email):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

# Função para listar todos os usuários
def listar_usuarios():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    return usuarios

# Função para atualizar os dados de um usuário
def atualizar_usuario(id, nome, email):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute("UPDATE usuarios SET nome=?, email=? WHERE id=?", (nome, email, id))
    conn.commit()
    conn.close()

# Função para deletar um usuário
def deletar_usuario(id):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Menu principal
def menu():
    os.system('cls')

    print(cor_vermelha + "\nMENU:"+ reset_cor)
    print("1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

    

if __name__ == "__main__":
    criar_tabela()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system('cls')
            nome = input("\nDigite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            adicionar_usuario(nome, email)
            print("\nUsuário adicionado com sucesso!")
            time.sleep(1.50)
        elif opcao == "2":
            os.system('cls')
            print("\nLista de usuários:")
            usuarios = listar_usuarios()

            for usuario in usuarios:
                print(usuario)
            print(" ")

            input("...")
        elif opcao == "3":
            os.system('cls')
            id = input("\nDigite o ID do usuário que deseja atualizar: ")
            nome = input("Digite o novo nome do usuário: ")
            email = input("Digite o novo email do usuário: ")
            atualizar_usuario(id, nome, email)
            print("Usuário atualizado com sucesso!")
            time.sleep(2.5)

        elif opcao == "4":
            os.system('cls')
            id = input("\nDigite o ID do usuário que deseja deletar: ")
            deletar_usuario(id)
            print("Usuário deletado com sucesso!")
            time.sleep(2.5)
        elif opcao == "5":
            os.system('cls')
            print("\nSaindo...")
            time.sleep(2.5)
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")
            time.sleep(1)
