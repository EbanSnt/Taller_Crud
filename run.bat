@echo off

REM Cambia al directorio del proyecto Django
cd ruta\del\proyecto

REM Activa el entorno virtual
call venv\Scripts\activate

REM Inicia el servidor de desarrollo de Django en una nueva ventana de la consola
start cmd /k "python manage.py runserver"

REM Espera unos segundos para que el servidor inicie correctamente
timeout /nobreak /t 5 >nul

REM Abre el navegador predeterminado en la URL del servidor
start "" http://127.0.0.1:8000/home