# 🚀 UNIVERSI TOUR - Guia de Instalação

## 📋 Pré-requisitos

### 1. **Python 3.8+**
- Baixe em: https://python.org/downloads/
- ✅ Marque "Add Python to PATH" durante instalação

### 2. **MySQL Server**
- Baixe em: https://dev.mysql.com/downloads/mysql/
- Ou use XAMPP: https://www.apachefriends.org/

## 🔧 Configuração Inicial

### 1. **Copiar Arquivos**
```
ProjetoViagem/
├── backend/
│   ├── backend/
│   │   ├── app.py
│   │   └── requirements.txt
│   ├── database/
│   │   ├── create_tables.sql
│   │   └── insert_sample_data.sql
│   └── create_tables_simple.py
├── Front/
│   └── frontend/
│       └── frontend/
│           ├── html.html
│           ├── javasite.js
│           ├── site.css
│           ├── admin.html
│           └── Imagens/
├── servidor_frontend.py
└── rodar_tudo.py
```

### 2. **Configurar MySQL**
```sql
-- Criar banco de dados
CREATE DATABASE universi_tour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Criar usuário (opcional)
CREATE USER 'usuario_tour'@'localhost' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON universi_tour.* TO 'usuario_tour'@'localhost';
FLUSH PRIVILEGES;
```

### 3. **Ajustar Configurações**
Edite `backend/backend/app.py` nas linhas 8-12:

```python
# Configurações do MySQL - AJUSTE AQUI
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'  # Seu usuário MySQL
MYSQL_PASSWORD = 'SUA_SENHA'  # Sua senha MySQL
MYSQL_DATABASE = 'universi_tour'
```

## 🚀 Executar o Projeto

### Método 1: Script Automático (Recomendado)
```bash
python rodar_tudo.py
```

### Método 2: Manual
```bash
# Terminal 1 - Backend
cd backend/backend
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend
python servidor_frontend.py
```

### Método 3: Windows Batch
```bash
rodar_projeto.bat
```

## 🌐 Acessar o Sistema

- **Site Principal:** http://localhost:8080/html.html
- **Painel Admin:** http://localhost:8080/admin.html
- **API Backend:** http://127.0.0.1:5000/api/destinos

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
pip install -r backend/requirements.txt
```

### Erro: "Can't connect to MySQL"
1. Verifique se MySQL está rodando
2. Confirme usuário/senha no app.py
3. Teste conexão:
```bash
python backend/create_tables_simple.py
```

### Erro: "Port already in use"
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [NUMERO_PID] /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Erro: "UnicodeEncodeError"
- Use terminal que suporte UTF-8
- Ou rode sem emojis (já corrigido no código)

## 📱 Funcionalidades

✅ **Sistema de Destinos**
- Listagem dinâmica do banco
- Filtros por nome, distância, preço
- Imagens e descrições

✅ **Sistema de Reservas**
- Modal interativo
- Cálculo automático de preços
- Validação de formulários
- Salvamento no banco

✅ **Sistema de Contatos**
- Formulário de contato
- Armazenamento no banco
- Feedback visual

✅ **Painel Administrativo**
- Gerenciamento de destinos
- Visualização de reservas
- Estatísticas do sistema

## 🔄 Backup e Restauração

### Backup do Banco
```bash
mysqldump -u root -p universi_tour > backup.sql
```

### Restaurar Banco
```bash
mysql -u root -p universi_tour < backup.sql
```

## 📞 Suporte

Em caso de problemas:
1. Verifique se MySQL está rodando
2. Confirme as configurações no app.py
3. Teste a conexão com o banco
4. Verifique as portas 5000 e 8080

---
**🎯 Sistema testado e funcionando em Windows, Linux e macOS!**
