@echo off
echo ========================================
echo    TESTE DO SISTEMA UNIVERSI TOUR
echo ========================================
echo.

echo [1/3] Testando Backend...
curl -s http://127.0.0.1:5000/api/destinos >nul 2>&1
if errorlevel 1 (
    echo ❌ Backend não está rodando!
    echo 💡 Execute: cd backend\backend ^&^& python app.py
    echo.
    pause
    exit
) else (
    echo ✅ Backend funcionando!
)

echo.
echo [2/3] Testando API...
curl -s http://127.0.0.1:5000/api/destinos
echo.
echo.

echo [3/3] Abrindo página de teste...
start "" "testar_conexao.html"

echo.
echo ✅ Teste concluído!
echo.
echo 📋 Se a página de teste mostrar os destinos:
echo    • O backend está funcionando corretamente
echo    • O problema é no frontend principal
echo.
echo 💡 Soluções:
echo    • Use o servidor frontend: python servidor_frontend.py
echo    • Ou abra: http://localhost:8080/html.html
echo.
pause
