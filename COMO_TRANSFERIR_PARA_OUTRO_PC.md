# 📦 Como Rodar o Projeto em Outro PC

## 🎯 **Método Mais Fácil (Recomendado)**

### **1. Pacote de Instalação Automática**
✅ **Arquivo criado:** `UNIVERSI_TOUR_INSTALACAO.zip` (1.3 MB)

**Para transferir:**
1. **Copie** o arquivo `UNIVERSI_TOUR_INSTALACAO.zip`
2. **Envie** para o outro PC (pendrive, email, nuvem)
3. **Extraia** o arquivo ZIP
4. **Execute:** `python instalar_projeto.py`

### **2. O que o Script de Instalação Faz:**
- ✅ **Verifica Python** instalado
- ✅ **Detecta MySQL** automaticamente
- ✅ **Instala dependências** Python
- ✅ **Cria banco de dados** automaticamente
- ✅ **Configura conexões** MySQL
- ✅ **Cria script de execução** (EXECUTAR.bat)

---

## 🔧 **Método Manual (Alternativo)**

### **1. Copiar Arquivos Essenciais**
```
ProjetoViagem/
├── backend/
│   ├── backend/app.py
│   ├── requirements.txt
│   ├── database/
│   │   ├── create_tables.sql
│   │   └── insert_sample_data.sql
│   └── create_tables_simple.py
├── Front/frontend/frontend/
│   ├── html.html
│   ├── javasite.js
│   ├── site.css
│   ├── admin.html
│   └── Imagens/
├── servidor_frontend.py
├── rodar_tudo.py
└── GUIA_INSTALACAO.md
```

### **2. Pré-requisitos no PC Destino**
- **Python 3.8+** instalado
- **MySQL Server** instalado e rodando

### **3. Configuração Manual**
1. **Instalar dependências:**
   ```bash
   pip install -r backend/requirements.txt
   ```

2. **Configurar MySQL:**
   ```sql
   CREATE DATABASE universi_tour CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **Ajustar credenciais** em `backend/backend/app.py`:
   ```python
   MYSQL_USER = 'seu_usuario'
   MYSQL_PASSWORD = 'sua_senha'
   ```

4. **Criar tabelas:**
   ```bash
   python backend/create_tables_simple.py
   ```

### **4. Executar**
```bash
python rodar_tudo.py
```

---

## 🚀 **Execução no PC Destino**

### **Opção 1 - Script Automático (Windows)**
```bash
EXECUTAR.bat
```

### **Opção 2 - Python**
```bash
python rodar_tudo.py
```

### **Opção 3 - Manual**
```bash
# Terminal 1 - Backend
cd backend/backend
python app.py

# Terminal 2 - Frontend
python servidor_frontend.py
```

---

## 🌐 **URLs do Sistema**

| Serviço | URL |
|---------|-----|
| **🏠 Site Principal** | `http://localhost:8080/html.html` |
| **🔧 Painel Admin** | `http://localhost:8080/admin.html` |
| **📡 API Backend** | `http://127.0.0.1:5000/api/destinos` |

---

## 🔧 **Solução de Problemas Comuns**

### **Erro: "ModuleNotFoundError"**
```bash
pip install -r backend/requirements.txt
```

### **Erro: "Can't connect to MySQL"**
1. Verifique se MySQL está rodando
2. Confirme usuário/senha no `app.py`
3. Teste conexão:
   ```bash
   python backend/create_tables_simple.py
   ```

### **Erro: "Port already in use"**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [NUMERO_PID] /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### **MySQL não encontrado**
- **Windows:** Instale MySQL Server ou XAMPP
- **Linux:** `sudo apt install mysql-server`
- **Mac:** `brew install mysql`

---

## 📋 **Checklist de Instalação**

- [ ] **Python 3.8+** instalado
- [ ] **MySQL Server** instalado e rodando
- [ ] **Arquivos copiados** para o PC destino
- [ ] **Dependências instaladas** (`pip install -r requirements.txt`)
- [ ] **Banco de dados criado** (`universi_tour`)
- [ ] **Configurações ajustadas** (usuário/senha MySQL)
- [ ] **Tabelas criadas** (script create_tables_simple.py)
- [ ] **Projeto executando** (python rodar_tudo.py)
- [ ] **Site acessível** (http://localhost:8080/html.html)

---

## 🎯 **Funcionalidades Testadas**

✅ **Sistema de Destinos**
- Listagem dinâmica do banco MySQL
- Filtros por nome, distância, preço
- Imagens e descrições

✅ **Sistema de Reservas**
- Modal interativo com formulário completo
- Cálculo automático de preços
- Validação de dados
- Salvamento no banco MySQL

✅ **Sistema de Contatos**
- Formulário de contato funcional
- Armazenamento no banco
- Feedback visual

✅ **Painel Administrativo**
- Gerenciamento de destinos
- Visualização de reservas
- Estatísticas do sistema

---

**🎉 Sistema 100% funcional e pronto para usar em qualquer PC!**

Para dúvidas, consulte o arquivo `GUIA_INSTALACAO.md` incluído no pacote.
