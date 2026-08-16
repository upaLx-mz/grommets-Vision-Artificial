![Logo](https://lh3.googleusercontent.com/d/1ZvJinUf3CMo1WGMyRXiLbw931KCM4xiF)



# Grommets Artificial

Sistema de visión artificial diseñado con el proposito de reconocer entre las piezas buenas "OK" y las malas "NOK", que hay al salir de la estacón 180 de la linea de ensamble del IBC de ZF.

Mediante un modelo de IA entrenado con imagenes obtenidas de la linea, se examinan los grommets montados para tomar una desición.


## Instalación

### 1. Python
Para correr el programa de detección se necesita Python en su versión 3.10. El instalable de Python se encuentra disponible en el siguiente enlace.

* [Python 3.10.10](https://www.python.org/downloads/release/python-31010/)

Una vez descargado el instalador correspondiente, se ejecuta el archivo y se instala Python de manera convencional, procurando que se agrege a las variables globales automaticamente.

### 2. Repositorio
 Descargar el repositorio de GitHub mediante el comando:

 ```bash
git clone https://github.com/upaLx-mz/grommets-Vision-Artificial.git
 ```
 ó mediante la descarga manual en GitHub.

### 3. Entorno virtual
  Abrir una terminal de Powershell en la carpeta del repositorio y crear un entorno virtual de Python con el siguiente comando (en caso de solo tener instalada la versión 3.10.10):

 ```PowerShell
python -m venv .venv
 ```

 Si se tienen instaladas mas versiones de Python utilizar el siguiente comando:

 ```PowerShell
py -3.10 -m venv .venv
 ```

 Una vez creado el entono virtual lo activamos con:

 ```PowerShell
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned); .venv\Scripts\Activate.ps1
 ```
 Si todo lo anterior se realizo correctamente en la terminal se debe observar algo como lo siguiente:
 ```bash
 (.venv) PS C:\Users\user\...
 ```

### 4. Librerias
 Por utlimo paso hay que instalar las librerias que usa el proyecto, para eso utilizamos el comando:

 ```PowerShell
pip install -r requirements.txt
 ```
## Uso
Para ejecutar el programa de visión artificial, hay que tener abierto nuestro programa de CODESYS y Factory IO antes y corriendo sin ningun problema.

Despues en la terminal ejecutamos el comando:

```bash
python -m src.main
```
Y listo nuestro programa se deberia encontrar corriendo sin alguna novedad y preparada para ejecutar el analisis mediante visión artificial.

## Tecnologias

* Python
* Factory IO
* Modbus
* CODESYS
