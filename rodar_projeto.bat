@echo off
echo ========================================
echo    UNIVERSI TOUR - Sistema de Viagens
echo ========================================
echo.

echo [1/4] Verificando dependencias...
cd backend\backend
python -c "import flask, pymysql" 2>nul
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r ..\requirements.txt
)

echo [2/4] Iniciando Backend...
start "Backend Flask" cmd /k "python app.py"

echo [3/4] Aguardando backend inicializar...
ping 127.0.0.1 -n 6 >nul

echo [4/4] Iniciando Servidor Frontend...
start "Servidor Frontend" cmd /k "python ..\..\servidor_frontend.py"

echo.
echo ✅ Projeto rodando!
echo.
echo 📋 URLs disponíveis:
echo    • Frontend: http://localhost:8080/html.html (aberto no navegador)
echo    • Admin: http://localhost:8080/admin.html
echo    • API: http://127.0.0.1:5000/api/destinos
echo.
echo ⚠️  Mantenha as janelas abertas para funcionar
echo    Para parar: feche as janelas do terminal
echo.
pause
