# Matemática II Ciclo 02-2026 - Tarea Semanal 8.

Este proyecto contiene el script en Python para la resolución y graficación de los ejercicios de cálculo integral, correspondientes a la Unidad 2 de la asignatura Matemática II.

## Requisitos Previos
- Python 3.8 o superior instalado en tu sistema.
- Visual Studio Code (recomendado) u otro editor de código.

## Instrucciones de Ejecución

### 1. Abrir el proyecto
Abre la carpeta del proyecto en tu editor de código. Si usas Visual Studio Code, puedes abrir tu terminal en la carpeta del proyecto y ejecutar:
```bash
code .
bash```

### 2. Activar el Entorno Virtual
Para aislar las librerías del proyecto, es necesario activar el entorno virtual. Dependiendo de la terminal que estés utilizando en Windows, el comando varía:

Símbolo del Sistema (CMD):

DOS
venv\Scripts\activate
PowerShell:

PowerShell
.\venv\Scripts\Activate.ps1
Git Bash:

Bash
source venv/Scripts/activate
(Sabrás que está activado cuando veas (venv) al inicio de tu línea de comandos).

### 3. Instalar las Dependencias
Con el entorno virtual activado, instala las librerías matemáticas requeridas ejecutando:

Bash
pip install numpy matplotlib sympy
(Si generaste el archivo requirements.txt previamente, puedes usar el comando pip install -r requirements.txt).

### 4. Configuración y Ejecución en Visual Studio Code
Sigue estos pasos finales para ejecutar el archivo y generar las gráficas solicitadas en la tarea:

Abre el archivo main.py dentro de Visual Studio Code.

Presiona Ctrl + Shift + P para abrir la paleta de comandos.

Escribe y selecciona la opción Python: Select Interpreter.

Elige el intérprete que indica (venv) o busca la ruta ./venv/Scripts/python.exe. Esto asegura que VS Code reconozca que estamos usando las librerías correctas.

Ejecuta el archivo. Puedes hacerlo presionando el botón de Play (▷) en la esquina superior derecha del editor, o escribiendo el siguiente comando en la terminal integrada (asegurándote de que (venv) sigue activo):

Bash
python main.py
El programa comenzará a calcular las integrales en la consola y abrirá ventanas emergentes con la gráfica de cada ejercicio. Recuerda tomar las capturas de pantalla de la consola y de cada gráfica para anexarlas a tu documento de Word antes de enviarlo.