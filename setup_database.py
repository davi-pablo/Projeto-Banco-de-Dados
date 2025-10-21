#!/usr/bin/env python3
"""
Script para configurar o banco de dados MySQL
Execute este script após configurar o MySQL
"""

import pymysql
import os
import sys

def conectar_mysql():
    """Conectar ao MySQL sem especificar banco"""
    try:
        # Configurações do MySQL (ajuste conforme necessário)
        host = 'localhost'
        port = 3306
        user = 'root'
        password = input("Digite a senha do MySQL root: ")
        
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset='utf8mb4'
        )
        
        print("✅ Conectado ao MySQL com sucesso!")
        return connection, password
        
    except Exception as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")
        return None, None

def criar_banco(connection):
    """Criar o banco de dados"""
    try:
        cursor = connection.cursor()
        
        # Verificar se o banco já existe
        cursor.execute("SHOW DATABASES LIKE 'universi_tour'")
        if cursor.fetchone():
            print("ℹ️  Banco 'universi_tour' já existe")
            resposta = input("Deseja recriar o banco? (s/N): ").lower()
            if resposta == 's':
                cursor.execute("DROP DATABASE universi_tour")
                print("🗑️  Banco removido")
            else:
                cursor.close()
                return True
        
        # Criar o banco
        cursor.execute("CREATE DATABASE universi_tour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ Banco 'universi_tour' criado com sucesso!")
        
        cursor.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar banco: {e}")
        return False

def executar_script_sql(connection, script_path):
    """Executar um script SQL"""
    try:
        cursor = connection.cursor()
        
        # Ler o arquivo SQL
        with open(script_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        
        # Executar o script
        for statement in sql_script.split(';'):
            statement = statement.strip()
            if statement:
                cursor.execute(statement)
        
        connection.commit()
        print(f"✅ Script {script_path} executado com sucesso!")
        cursor.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro ao executar script {script_path}: {e}")
        return False

def verificar_tabelas(connection):
    """Verificar se as tabelas foram criadas"""
    try:
        cursor = connection.cursor()
        cursor.execute("USE universi_tour")
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        
        print("\n📋 Tabelas criadas:")
        for tabela in tabelas:
            print(f"  - {tabela[0]}")
        
        cursor.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro ao verificar tabelas: {e}")
        return False

def main():
    print("🚀 Configurando banco de dados MySQL para Universi Tour")
    print("=" * 50)
    
    # Conectar ao MySQL
    connection, password = conectar_mysql()
    if not connection:
        sys.exit(1)
    
    try:
        # Criar banco de dados
        if not criar_banco(connection):
            sys.exit(1)
        
        # Conectar ao banco específico
        connection.select_db('universi_tour')
        
        # Executar script de criação das tabelas
        script_path = 'database/create_tables.sql'
        if os.path.exists(script_path):
            if not executar_script_sql(connection, script_path):
                sys.exit(1)
        else:
            print(f"⚠️  Arquivo {script_path} não encontrado")
        
        # Perguntar se deseja inserir dados de exemplo
        resposta = input("\nDeseja inserir dados de exemplo? (s/N): ").lower()
        if resposta == 's':
            script_exemplo = 'database/insert_sample_data.sql'
            if os.path.exists(script_exemplo):
                executar_script_sql(connection, script_exemplo)
            else:
                print(f"⚠️  Arquivo {script_exemplo} não encontrado")
        
        # Verificar tabelas
        verificar_tabelas(connection)
        
        print("\n🎉 Configuração concluída com sucesso!")
        print("\n📝 Próximos passos:")
        print("1. Edite o arquivo backend/app.py e ajuste a senha do MySQL")
        print("2. Execute: python backend/app.py")
        print("3. Acesse: http://localhost:5000/api/destinos")
        
    finally:
        connection.close()

if __name__ == '__main__':
    main()
