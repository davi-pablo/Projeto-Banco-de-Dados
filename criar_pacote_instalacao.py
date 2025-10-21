#!/usr/bin/env python3
"""
Script para criar um pacote de instalação do UNIVERSI TOUR
Gera um arquivo ZIP com tudo necessário para instalar em outro PC
"""

import zipfile
import os
from pathlib import Path

def criar_pacote_instalacao():
    """Cria um pacote ZIP com todos os arquivos necessários"""
    
    print("Criando pacote de instalacao...")
    
    # Arquivos e pastas essenciais
    arquivos_essenciais = [
        # Backend
        "backend/backend/app.py",
        "backend/requirements.txt",
        "backend/database/create_tables.sql",
        "backend/database/insert_sample_data.sql",
        "backend/create_tables_simple.py",
        
        # Frontend
        "Front/frontend/frontend/html.html",
        "Front/frontend/frontend/javasite.js",
        "Front/frontend/frontend/site.css",
        "Front/frontend/frontend/admin.html",
        "Front/frontend/frontend/confirmacao.html",
        "Front/frontend/frontend/Imagens/",
        
        # Scripts
        "servidor_frontend.py",
        "rodar_tudo.py",
        "instalar_projeto.py",
        "GUIA_INSTALACAO.md",
        
        # Scripts Windows
        "rodar_projeto.bat",
    ]
    
    # Criar arquivo ZIP
    nome_arquivo = "UNIVERSI_TOUR_INSTALACAO.zip"
    
    with zipfile.ZipFile(nome_arquivo, 'w', zipfile.ZIP_DEFLATED) as zipf:
        
        for arquivo in arquivos_essenciais:
            if os.path.exists(arquivo):
                if os.path.isdir(arquivo):
                    # Adicionar pasta inteira
                    for root, dirs, files in os.walk(arquivo):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arc_path = os.path.relpath(file_path, ".")
                            zipf.write(file_path, arc_path)
                            print(f"Adicionado: {arc_path}")
                else:
                    # Adicionar arquivo
                    zipf.write(arquivo, arquivo)
                    print(f"Adicionado: {arquivo}")
            else:
                print(f"AVISO - Arquivo nao encontrado: {arquivo}")
    
    print(f"\nSUCESSO - Pacote criado: {nome_arquivo}")
    
    # Criar arquivo README para o pacote
    readme_content = """# UNIVERSI TOUR - Sistema de Viagens

## Instalação Rápida

1. **Extraia este arquivo ZIP**
2. **Execute:** `python instalar_projeto.py`
3. **Siga as instruções** na tela

## Pré-requisitos

- Python 3.8+ instalado
- MySQL Server instalado e rodando

## Execução

Após instalação:
- **Windows:** Duplo clique em `EXECUTAR.bat`
- **Linux/Mac:** `python rodar_tudo.py`

## URLs do Sistema

- Site: http://localhost:8080/html.html
- Admin: http://localhost:8080/admin.html
- API: http://127.0.0.1:5000/api/destinos

## Suporte

Consulte `GUIA_INSTALACAO.md` para instruções detalhadas.
"""
    
    with open("README_INSTALACAO.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Adicionar README ao ZIP
    with zipfile.ZipFile(nome_arquivo, 'a', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("README_INSTALACAO.txt", "README_INSTALACAO.txt")
    
    # Remover README temporário
    os.remove("README_INSTALACAO.txt")
    
    print(f"Tamanho do pacote: {os.path.getsize(nome_arquivo) / 1024 / 1024:.1f} MB")
    print("\nPacote pronto para transferir para outro PC!")

if __name__ == "__main__":
    criar_pacote_instalacao()
