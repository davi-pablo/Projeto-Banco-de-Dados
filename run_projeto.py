#!/usr/bin/env python3
"""
Script para rodar todo o projeto - Backend + Frontend
"""

import subprocess
import webbrowser
import time
import os
import sys
from pathlib import Path

def rodar_backend():
    """Roda o backend Flask"""
    print("🚀 Iniciando Backend Flask...")
    
    # Navegar para a pasta do backend
    backend_path = Path("backend/backend")
    
    if not backend_path.exists():
        print("❌ Pasta backend não encontrada!")
        return False
    
    try:
        # Rodar o backend
        process = subprocess.Popen(
            [sys.executable, "app.py"],
            cwd=backend_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("✅ Backend iniciado!")
        print("📡 API rodando em: http://127.0.0.1:5000")
        return process
        
    except Exception as e:
        print(f"❌ Erro ao iniciar backend: {e}")
        return None

def abrir_frontend():
    """Abre o frontend no navegador"""
    print("🌐 Abrindo Frontend...")
    
    frontend_path = Path("Front/frontend/frontend/html.html")
    
    if not frontend_path.exists():
        print("❌ Arquivo html.html não encontrado!")
        return False
    
    try:
        # Abrir no navegador padrão
        webbrowser.open(f"file://{frontend_path.absolute()}")
        print("✅ Frontend aberto no navegador!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao abrir frontend: {e}")
        return False

def abrir_admin():
    """Abre o painel administrativo"""
    print("🔧 Abrindo Painel Administrativo...")
    
    admin_path = Path("Front/frontend/frontend/admin.html")
    
    if not admin_path.exists():
        print("❌ Arquivo admin.html não encontrado!")
        return False
    
    try:
        # Abrir no navegador padrão
        webbrowser.open(f"file://{admin_path.absolute()}")
        print("✅ Painel Admin aberto no navegador!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao abrir admin: {e}")
        return False

def main():
    print("🎯 UNIVERSI TOUR - Sistema de Viagens")
    print("=" * 50)
    
    # Verificar se estamos na pasta correta
    if not Path("backend").exists() or not Path("Front").exists():
        print("❌ Execute este script na pasta raiz do projeto!")
        print("   Deve conter as pastas 'backend' e 'Front'")
        return
    
    # Rodar backend
    backend_process = rodar_backend()
    if not backend_process:
        return
    
    # Aguardar o backend inicializar
    print("⏳ Aguardando backend inicializar...")
    time.sleep(3)
    
    # Abrir frontend
    abrir_frontend()
    time.sleep(1)
    
    # Perguntar se quer abrir admin
    resposta = input("\n❓ Deseja abrir o Painel Administrativo? (s/N): ").lower()
    if resposta == 's':
        abrir_admin()
    
    print("\n🎉 Projeto rodando!")
    print("📋 URLs disponíveis:")
    print("   • Frontend: html.html (aberto no navegador)")
    print("   • Admin: admin.html")
    print("   • API: http://127.0.0.1:5000/api/destinos")
    print("\n⚠️  Mantenha este terminal aberto para o backend funcionar")
    print("   Para parar: pressione Ctrl+C")
    
    try:
        # Manter o processo rodando
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Parando o projeto...")
        backend_process.terminate()
        print("✅ Projeto parado!")

if __name__ == '__main__':
    main()
