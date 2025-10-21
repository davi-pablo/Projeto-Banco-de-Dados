#!/usr/bin/env python3
"""
Script de instalação automática do UNIVERSI TOUR
Funciona em qualquer PC com Python e MySQL
"""

import subprocess
import sys
import os
import pymysql
from pathlib import Path

def verificar_python():
    """Verifica se Python está instalado"""
    print("🔍 Verificando Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Versão 3.8+ necessária")
        return False

def verificar_mysql():
    """Verifica se MySQL está instalado e acessível"""
    print("🔍 Verificando MySQL...")
    
    try:
        # Tentar conectar com configurações padrão
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Senha vazia por padrão
            charset='utf8mb4'
        )
        connection.close()
        print("✅ MySQL conectado (usuário: root, senha: vazia)")
        return True, 'root', ''
        
    except pymysql.Error as e:
        print("⚠️  MySQL não encontrado ou configuração diferente")
        
        # Tentar com senha comum
        senhas_comuns = ['1234', '123456', 'password', 'root']
        
        for senha in senhas_comuns:
            try:
                connection = pymysql.connect(
                    host='localhost',
                    user='root',
                    password=senha,
                    charset='utf8mb4'
                )
                connection.close()
                print(f"✅ MySQL conectado (usuário: root, senha: {senha})")
                return True, 'root', senha
            except:
                continue
        
        print("❌ Não foi possível conectar ao MySQL")
        print("💡 Instale MySQL ou configure as credenciais")
        return False, None, None

def instalar_dependencias():
    """Instala as dependências Python"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"
        ], check=True, capture_output=True, text=True)
        print("✅ Dependências instaladas")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def configurar_banco_dados(usuario, senha):
    """Configura o banco de dados"""
    print("🗄️  Configurando banco de dados...")
    
    try:
        # Conectar ao MySQL
        connection = pymysql.connect(
            host='localhost',
            user=usuario,
            password=senha,
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Criar banco de dados
        cursor.execute("CREATE DATABASE IF NOT EXISTS universi_tour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✅ Banco 'universi_tour' criado")
        
        # Usar o banco
        cursor.execute("USE universi_tour")
        
        # Executar script de criação das tabelas
        with open('backend/database/create_tables.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        # Executar comandos SQL
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        print("✅ Tabelas criadas")
        
        # Executar script de dados de exemplo
        with open('backend/database/insert_sample_data.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        print("✅ Dados de exemplo inseridos")
        
        connection.commit()
        connection.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao configurar banco: {e}")
        return False

def atualizar_configuracoes(usuario, senha):
    """Atualiza as configurações do backend"""
    print("⚙️  Atualizando configurações...")
    
    app_py_path = Path("backend/backend/app.py")
    
    try:
        # Ler arquivo atual
        with open(app_py_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substituir configurações
        content = content.replace("MYSQL_USER = 'root'", f"MYSQL_USER = '{usuario}'")
        content = content.replace("MYSQL_PASSWORD = '1234'", f"MYSQL_PASSWORD = '{senha}'")
        
        # Escrever arquivo atualizado
        with open(app_py_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Configurações atualizadas")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao atualizar configurações: {e}")
        return False

def criar_script_execucao():
    """Cria script para executar o projeto"""
    print("📝 Criando script de execução...")
    
    script_content = '''@echo off
echo ========================================
echo    UNIVERSI TOUR - Sistema de Viagens
echo ========================================
echo.

echo Iniciando projeto...
python rodar_tudo.py

pause
'''
    
    try:
        with open('EXECUTAR.bat', 'w', encoding='utf-8') as f:
            f.write(script_content)
        print("✅ Script 'EXECUTAR.bat' criado")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar script: {e}")
        return False

def main():
    """Função principal de instalação"""
    print("=" * 60)
    print("   UNIVERSI TOUR - Instalação Automática")
    print("=" * 60)
    print()
    
    # 1. Verificar Python
    if not verificar_python():
        input("Pressione Enter para sair...")
        return
    
    # 2. Verificar MySQL
    mysql_ok, usuario, senha = verificar_mysql()
    if not mysql_ok:
        print("\n💡 Instruções para instalar MySQL:")
        print("   1. Baixe em: https://dev.mysql.com/downloads/mysql/")
        print("   2. Ou use XAMPP: https://www.apachefriends.org/")
        print("   3. Execute este script novamente após instalar")
        input("Pressione Enter para sair...")
        return
    
    # 3. Instalar dependências
    if not instalar_dependencias():
        input("Pressione Enter para sair...")
        return
    
    # 4. Configurar banco de dados
    if not configurar_banco_dados(usuario, senha):
        input("Pressione Enter para sair...")
        return
    
    # 5. Atualizar configurações
    if not atualizar_configuracoes(usuario, senha):
        input("Pressione Enter para sair...")
        return
    
    # 6. Criar script de execução
    criar_script_execucao()
    
    print()
    print("🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print()
    print("📋 Para executar o projeto:")
    print("   • Duplo clique em: EXECUTAR.bat")
    print("   • Ou execute: python rodar_tudo.py")
    print()
    print("🌐 URLs do sistema:")
    print("   • Site: http://localhost:8080/html.html")
    print("   • Admin: http://localhost:8080/admin.html")
    print()
    print("⚠️  Mantenha o MySQL rodando para usar o sistema")
    print()
    
    # Perguntar se quer executar agora
    resposta = input("Deseja executar o projeto agora? (s/n): ").lower()
    if resposta in ['s', 'sim', 'y', 'yes']:
        print("\n🚀 Iniciando projeto...")
        try:
            subprocess.run([sys.executable, "rodar_tudo.py"])
        except KeyboardInterrupt:
            print("\n👋 Projeto finalizado!")
    
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
