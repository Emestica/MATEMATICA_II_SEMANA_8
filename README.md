# Matemática II — Ciclo 02-2026

## Tarea Semanal 8

Este proyecto contiene el script en Python utilizado para la resolución y graficación de los ejercicios de cálculo integral correspondientes a la **Unidad 2** de la asignatura **Matemática II**.

## Requisitos previos

* **Python 3.8 o superior** instalado en el sistema.
* **Visual Studio Code** (recomendado) u otro editor de código.

## Instrucciones de ejecución

### 1. Abrir el proyecto

Abre la carpeta del proyecto en tu editor de código.

Si utilizas Visual Studio Code, puedes abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
code .
```

### 2. Activar el entorno virtual

Para aislar las librerías utilizadas por el proyecto, es necesario activar el entorno virtual.

Dependiendo de la terminal que estés utilizando en Windows, el comando varía:

**Símbolo del sistema (CMD):**

```cmd
venv\Scripts\activate
```

**PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Git Bash:**

```bash
source venv/Scripts/activate
```

Sabrás que el entorno virtual está activo cuando aparezca `(venv)` al inicio de la línea de comandos.

### 3. Instalar las dependencias

El proyecto incluye un archivo `requirements.txt` con todas las librerías necesarias para su ejecución.

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirements.txt
```

Este comando instalará automáticamente todas las dependencias especificadas en el proyecto.

> **Nota:** Si necesitas agregar o actualizar alguna librería utilizada por el proyecto, puedes modificar el archivo `requirements.txt` para mantener centralizadas las dependencias.

### 4. Configurar el intérprete de Python en Visual Studio Code

Para asegurarte de que Visual Studio Code utilice el entorno virtual del proyecto:

1. Abre el archivo `main.py` dentro de Visual Studio Code.
2. Presiona **Ctrl + Shift + P** para abrir la paleta de comandos.
3. Escribe y selecciona **Python: Select Interpreter**.
4. Selecciona el intérprete correspondiente al entorno virtual `(venv)` o busca la ruta:

```text
./venv/Scripts/python.exe
```

Esto permitirá que Visual Studio Code utilice correctamente las librerías instaladas en el entorno virtual.

### 5. Ejecutar el programa

Puedes ejecutar el programa de cualquiera de las siguientes maneras.

**Desde el botón de ejecución de Visual Studio Code:**

Presiona el botón **▶ Run Python File** ubicado en la esquina superior derecha del editor.

**Desde la terminal integrada:**

Asegúrate de que el entorno virtual esté activo y ejecuta:

```bash
python main.py
```

El programa comenzará a calcular las integrales y mostrará los resultados en la consola. Además, se abrirán ventanas con las gráficas correspondientes a cada ejercicio.

> **Nota:** Recuerda tomar capturas de pantalla de los resultados mostrados en la consola y de cada gráfica para anexarlas al documento de Word antes de realizar la entrega de la tarea.
