#!/usr/bin/env python3
"""
Servidor HTTP simples para servir o frontend
Resolve problemas de CORS ao abrir arquivos locais
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def iniciar_servidor_frontend():
    """Inicia um servidor HTTP para servir o frontend"""
    
    # Pasta do frontend
    frontend_dir = Path("Front/frontend/frontend")
    
    if not frontend_dir.exists():
        print("❌ Pasta do frontend não encontrada!")
        return
    
    # Mudar para a pasta do frontend
    os.chdir(frontend_dir)
    
    # Configurar o servidor
    PORT = 8080
    
    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Adicionar headers CORS
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
        
        def do_OPTIONS(self):
            self.send_response(200)
            self.end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("Servidor Frontend iniciado!")
            print(f"Rodando em: http://localhost:{PORT}")
            print(f"Servindo arquivos de: {frontend_dir.absolute()}")
            print("\nURLs disponíveis:")
            print(f"   • Frontend: http://localhost:{PORT}/html.html")
            print(f"   • Admin: http://localhost:{PORT}/admin.html")
            print("\nMantenha este terminal aberto")
            print("Para parar: pressione Ctrl+C")
            
            # Abrir automaticamente o frontend
            webbrowser.open(f"http://localhost:{PORT}/html.html")
            
            # Iniciar o servidor
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServidor frontend parado!")
    except Exception as e:
        print(f"Erro ao iniciar servidor: {e}")

if __name__ == '__main__':
    iniciar_servidor_frontend()
