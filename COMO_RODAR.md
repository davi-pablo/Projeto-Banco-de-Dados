# 🚀 Como Rodar o Projeto Universi Tour

## ⚡ Método Rápido (Recomendado)

### 1. **Duplo clique no arquivo:**
```
rodar_projeto.bat
```

Este arquivo vai:
- ✅ Verificar e instalar dependências
- ✅ Iniciar o backend Flask
- ✅ Abrir o frontend no navegador
- ✅ Mostrar todas as URLs disponíveis

---

## 🛠️ Método Manual (Passo a Passo)

### 1. **Rodar o Backend:**
```bash
cd backend/backend
python app.py
```
*Mantenha esta janela aberta*

### 2. **Abrir o Frontend:**
- Navegue até: `Front/frontend/frontend/`
- Abra o arquivo: `html.html` no navegador

### 3. **Acessar o Painel Admin (Opcional):**
- Abra o arquivo: `Front/frontend/frontend/admin.html` no navegador

---

## 📋 URLs Disponíveis

| Recurso | URL |
|---------|-----|
| **Frontend Principal** | `Front/frontend/frontend/html.html` |
| **Painel Administrativo** | `Front/frontend/frontend/admin.html` |
| **API de Destinos** | `http://127.0.0.1:5000/api/destinos` |
| **API de Usuários** | `http://127.0.0.1:5000/api/usuarios` |
| **API de Reservas** | `http://127.0.0.1:5000/api/reservas` |
| **API de Contatos** | `http://127.0.0.1:5000/api/contatos` |

---

## ✅ Funcionalidades Disponíveis

### 🌐 **Frontend:**
- ✅ Listar destinos de viagem
- ✅ Filtrar por nome, distância e preço
- ✅ Fazer reservas de viagem
- ✅ Enviar mensagens de contato
- ✅ Interface responsiva e moderna

### 🔧 **Painel Administrativo:**
- ✅ Ver estatísticas do sistema
- ✅ Gerenciar reservas (confirmar/cancelar)
- ✅ Responder mensagens de contato
- ✅ Ver usuários cadastrados
- ✅ Dashboard completo

### 🗄️ **Banco de Dados:**
- ✅ MySQL local configurado
- ✅ 4 tabelas: destino, usuario, reserva, contato
- ✅ Dados de exemplo incluídos
- ✅ Relacionamentos configurados

---

## 🚨 Solução de Problemas

### **Backend não inicia:**
1. Verifique se o MySQL está rodando
2. Confirme as credenciais no `backend/app.py` (linhas 13-17)
3. Execute: `pip install -r backend/requirements.txt`

### **Frontend não carrega dados:**
1. Certifique-se que o backend está rodando
2. Abra o console do navegador (F12) para ver erros
3. Teste a API diretamente: `http://127.0.0.1:5000/api/destinos`

### **Erro de banco de dados:**
1. Execute: `python backend/create_tables_simple.py`
2. Verifique se o banco `universi_tour` existe
3. Confirme usuário e senha do MySQL

---

## 🎯 Próximos Passos

1. **Teste todas as funcionalidades:**
   - Fazer uma reserva
   - Enviar uma mensagem de contato
   - Usar os filtros de destino
   - Acessar o painel administrativo

2. **Personalize o sistema:**
   - Adicione novos destinos
   - Modifique preços e descrições
   - Personalize o visual

3. **Explore a API:**
   - Teste todas as rotas REST
   - Veja os dados em formato JSON
   - Use o painel admin para gerenciar

---

**🎉 Sistema completo e funcional!**
