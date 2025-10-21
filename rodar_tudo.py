#!/usr/bin/env python3
"""
Script para rodar o projeto completo
Backend + Frontend automaticamente
"""

import subprocess
import time
import webbrowser
import sys
import os
from pathlib import Path

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("Verificando dependencias...")
    
    try:
        import flask
        import pymysql
        print("OK - Dependencias instaladas")
        return True
    except ImportError as e:
        print(f"ERRO - Dependencia faltando: {e}")
        print("Instalando dependencias...")
        
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"], check=True)
            print("OK - Dependencias instaladas")
            return True
        except subprocess.CalledProcessError:
            print("ERRO - Nao foi possivel instalar dependencias")
            return False

def iniciar_backend():
    """Inicia o backend Flask"""
    print("Iniciando Backend...")
    
    backend_dir = Path("backend/backend")
    if not backend_dir.exists():
        print("ERRO - Pasta backend nao encontrada!")
        return None
    
    try:
        # Iniciar backend em processo separado
        process = subprocess.Popen(
            [sys.executable, "app.py"],
            cwd=backend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Aguardar um pouco para o backend inicializar
        time.sleep(3)
        
        print("OK - Backend iniciado na porta 5000")
        return process
        
    except Exception as e:
        print(f"ERRO - Erro ao iniciar backend: {e}")
        return None

def iniciar_frontend():
    """Inicia o servidor frontend"""
    print("Iniciando Frontend...")
    
    frontend_dir = Path("Front/frontend/frontend")
    if not frontend_dir.exists():
        print("ERRO - Pasta frontend nao encontrada!")
        return None
    
    try:
        # Iniciar servidor frontend
        process = subprocess.Popen(
            [sys.executable, "servidor_frontend.py"],
            cwd=Path("."),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Aguardar um pouco para o frontend inicializar
        time.sleep(2)
        
        print("OK - Frontend iniciado na porta 8080")
        return process
        
    except Exception as e:
        print(f"ERRO - Erro ao iniciar frontend: {e}")
        return None

def main():
    """Função principal"""
    print("=" * 50)
    print("   UNIVERSI TOUR - Sistema de Viagens")
    print("=" * 50)
    print()
    
    # Verificar dependências
    if not verificar_dependencias():
        return
    
    # Iniciar backend
    backend_process = iniciar_backend()
    if not backend_process:
        return
    
    # Iniciar frontend
    frontend_process = iniciar_frontend()
    if not frontend_process:
        backend_process.terminate()
        return
    
    print()
    print("SUCESSO - Projeto rodando!")
    print()
    print("URLs disponiveis:")
    print("   • Frontend: http://localhost:8080/html.html")
    print("   • Admin: http://localhost:8080/admin.html")
    print("   • API: http://127.0.0.1:5000/api/destinos")
    print()
    print("IMPORTANTE - Mantenha este terminal aberto")
    print("   Para parar: pressione Ctrl+C")
    print()
    
    # Abrir navegador
    try:
        webbrowser.open("http://localhost:8080/html.html")
        print("Navegador aberto automaticamente")
    except:
        print("AVISO - Nao foi possivel abrir o navegador automaticamente")
    
    print()
    
    try:
        # Manter o script rodando
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nParando projeto...")
        
        if frontend_process:
            frontend_process.terminate()
            print("OK - Frontend parado")
        
        if backend_process:
            backend_process.terminate()
            print("OK - Backend parado")
        
        print("Projeto finalizado!")

if __name__ == "__main__":
    main()
