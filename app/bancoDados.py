import mysql.connector

# Função para conectar ao MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",       # Servidor MySQL (use "localhost" se estiver rodando localmente)
            user="root",            # Seu usuário do MySQL
            password="adm123",   # Sua senha do MySQL
            database="dbEstacionamento"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

# Criar tabelas no MySQL (caso ainda não existam)
def criar_banco():
    conexao = conectar()
    if not conexao:
        return
   
    print("Banco de dados e tabelas criados com sucesso!") 

    conexao.close()

# Função para adicionar veículo
def adicionar_veiculo(cor, modelo, placa, forma_pagamento, data_entrada):
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO veiculos (cor, modelo, placa, forma_pagamento, data_entrada)
            VALUES (%s, %s, %s, %s, %s)
        """, (cor, modelo, placa, forma_pagamento, data_entrada))
        conexao.commit()
        print("Veículo cadastrado com sucesso!")
    except mysql.connector.IntegrityError:
        print("Erro: Placa já cadastrada.")
    finally:
        cursor.close()
        conexao.close()

# Função para excluir veículo
def excluir_veiculo(placa):
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()
    cursor.execute("DELETE FROM veiculos WHERE placa = %s", (placa,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Veículo excluído com sucesso!")

# Função para listar veículos
def listar_veiculos():
    conexao = conectar()
    if not conexao:
        return []

    cursor = conexao.cursor()
    cursor.execute("SELECT cor, modelo, placa, forma_pagamento, data_entrada FROM veiculos")
    veiculos = cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return veiculos

# Função para adicionar usuário
def adicionar_usuario(username, password):
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, password))
        conexao.commit()
        print(f"Usuário '{username}' cadastrado com sucesso!")
    except mysql.connector.IntegrityError:
        print(f"Erro: Usuário '{username}' já existe.")
    finally:
        cursor.close()
        conexao.close()

# Função para validar login
def validar_login(username, password):
    conexao = conectar()
    if not conexao:
        return False

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    
    return usuario is not None

# Função para alterar dados do veículo
def alterar_veiculo(placa_antiga, nova_cor, novo_modelo, nova_placa, nova_forma_pagamento, nova_data_entrada):
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE veiculos 
        SET cor = %s, modelo = %s, placa = %s, forma_pagamento = %s, data_entrada = %s 
        WHERE placa = %s
    """, (nova_cor, novo_modelo, nova_placa, nova_forma_pagamento, nova_data_entrada, placa_antiga))

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Veículo atualizado com sucesso!")
