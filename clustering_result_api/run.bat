@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Starting clustering REST API...
echo GET http://127.0.0.1:8000/api/clustering/result
echo Docs http://127.0.0.1:8000/docs
python -m uvicorn app:app --host 0.0.0.0 --port 8000
pause
